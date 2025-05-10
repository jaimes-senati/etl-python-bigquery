# ETL con Python, MySQL, SQL Server, Excel y Google BigQuery

Este proyecto implementa un proceso ETL (Extracción, Transformación y Carga) que unifica datos provenientes de tres fuentes distintas: MySQL, SQL Server y Excel. Luego, los datos transformados se cargan en Google BigQuery para su posterior análisis con herramientas como Power BI.

## 🚀 Requisitos

- Python 3.10 o superior
- Acceso a bases de datos MySQL y SQL Server
- Cuenta de Google Cloud con BigQuery habilitado

## 🛠️ Pasos para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/proyecto-etl.git
cd proyecto-etl
```

### 2. Crear y activar entorno virtual

```bash
python -m venv .venv
```

En windows:
```bash
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copiar el archivo de ejemplo:

```bash
copy .env.example .env
```

Edita el archivo .env y completa los siguientes datos:
- Credenciales de conexión a MySQL
- Credenciales de conexión a SQL Server
- Nombre del proyecto, dataset y tabla de BigQuery
- Ruta del archivo JSON de credenciales de Google

### 5. Obtener credenciales de Google Cloud
1. Accede a Google Cloud Console
2. Crea o selecciona un proyecto.
3. Habilita la API de BigQuery.
4. Ve a IAM y administrador > Cuentas de servicio
5. Crea una cuenta de servicio con el rol BigQuery Admin
6. Genera una clave (formato JSON) y descárgala
7. Renombra el archivo descargado como credentials.json
8. Colócalo en la raíz del proyecto (mismo nivel que app.py)

### 6. Crear tablas en bases de datos
Ejecuta el archivo SQL incluido en el repositorio para crear las tablas necesarias en tus bases de datos MySQL y SQL Server.

### 7. Ejecutar la aplicación

```bash
python app.py
```

La aplicación se iniciará en modo desarrollo en `http://localhost:5000`.

### 8. Configurar BigQuery
- En BigQuery, crea un Dataset.
- Dentro del dataset, crea una tabla con el esquema apropiado.
- Copia el nombre del proyecto, dataset y tabla en el archivo .env.

