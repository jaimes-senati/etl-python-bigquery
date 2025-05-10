from flask import Flask, jsonify
import mysql.connector
import pyodbc
import pandas as pd
from dotenv import load_dotenv
from google.cloud import bigquery
import os
from collections import defaultdict

load_dotenv()

app = Flask(__name__)

mysql_config = {
    'host': os.getenv('MYSQL_HOST'),
    'port': int(os.getenv('MYSQL_PORT')),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_NAME')
}

sqlserver_config = {
    'driver': os.getenv('SQLSERVER_DRIVER'),
    'server': os.getenv('SQLSERVER_HOST'),
    'port': os.getenv('SQLSERVER_PORT'),
    'user': os.getenv('SQLSERVER_USER'),
    'password': os.getenv('SQLSERVER_PASSWORD'),
    'database': os.getenv('SQLSERVER_DATABASE')
}

@app.route('/unification')
def unificar_datos():
    try:
        # 1. Obtener empleados desde MySQL
        mysql_conn = mysql.connector.connect(**mysql_config)
        mysql_cursor = mysql_conn.cursor(dictionary=True)
        mysql_cursor.execute("SELECT * FROM empleados;")
        empleados = mysql_cursor.fetchall()
        mysql_cursor.close()
        mysql_conn.close()
        empleados_df = pd.DataFrame(empleados)

        # 2. Obtener cargos desde Excel
        excel_path = os.path.join('data', 'cargos.xlsx')
        cargos_df = pd.read_excel(excel_path)

        # 3. Obtener distritos desde SQL Server
        conn_str = (
            f"DRIVER={{{sqlserver_config['driver']}}};"
            f"SERVER={sqlserver_config['server']},{sqlserver_config['port']};"
            f"UID={sqlserver_config['user']};"
            f"PWD={sqlserver_config['password']};"
            f"DATABASE={sqlserver_config['database']}"
        )
        sqlserver_conn = pyodbc.connect(conn_str)
        distrito_cursor = sqlserver_conn.cursor()
        distrito_cursor.execute("SELECT id, nombre FROM distritos;")
        distritos = [{'id': row.id, 'nombre': row.nombre} for row in distrito_cursor.fetchall()]
        distrito_cursor.close()
        sqlserver_conn.close()
        distritos_df = pd.DataFrame(distritos)

        # 4. Unir los datos
        df_unificado = empleados_df.merge(cargos_df, left_on='id_cargo', right_on='id', suffixes=('', '_cargo'))
        df_unificado = df_unificado.merge(distritos_df, left_on='id_distrito', right_on='id', suffixes=('', '_distrito'))

        # 5. Limpiar columnas (opcional)
        df_unificado = df_unificado.rename(columns={
            'nombre': 'nombre_empleado',
            'nombre_cargo': 'cargo',
            'nombre_distrito': 'distrito'
        })
        
        df_unificado = df_unificado.loc[:, ~df_unificado.columns.duplicated()]

        # 6. Subir a BigQuery
        client = bigquery.Client()
        table_id = f"{os.getenv('BQ_PROJECT_ID')}.{os.getenv('BQ_DATASET_ID')}.{os.getenv('BQ_TABLE_ID')}"
        job = client.load_table_from_dataframe(df_unificado, table_id, job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE"))
        job.result()

        return jsonify({'status': 'Datos unificados y cargados en BigQuery correctamente'})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/dashboard', methods=['GET'])
def obtener_datos_dashboard():
    query = f"""
        SELECT 
            id, 
            fecha_nacimiento, 
            id_distrito, 
            distrito, 
            id_cargo, 
            cargo 
        FROM `{os.getenv('BQ_PROJECT_ID')}.{os.getenv('BQ_DATASET_ID')}.{os.getenv('BQ_TABLE_ID')}`
    """
    
    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()

    total_empleados = 0
    distritos_unicos = set()
    cargos_unicos = set()
    timeline = defaultdict(int)

    for row in results:
        total_empleados += 1

        if row.id_distrito is not None:
            distritos_unicos.add(row.id_distrito)
        
        if row.id_cargo is not None:
            cargos_unicos.add(row.id_cargo)

        if row.fecha_nacimiento:
            year = row.fecha_nacimiento.year
            timeline[year] += 1

    timeline_ordenado = sorted(timeline.items())
    timeline_data = [{"year": year, "cantidad": cantidad} for year, cantidad in timeline_ordenado]

    return jsonify({
        "total_empleados": total_empleados,
        "total_distritos": len(distritos_unicos),
        "total_cargos": len(cargos_unicos),
        "empleados_por_anio": timeline_data
    })

if __name__ == '__main__':
    app.run(debug=True)
