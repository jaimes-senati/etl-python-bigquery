-- MySQL: Empleados
CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,                -- Identificador del empleado
    nombre VARCHAR(255) NOT NULL,                      -- Nombres del empleado
    apellidos VARCHAR(255) NOT NULL,                   -- Apellidos del empleado
    fecha_nacimiento DATE NOT NULL,                    -- Fecha de nacimiento del empleado
    id_distrito INT,                                  -- Identificador del distrito del empleado
    id_cargo INT                                      -- Identificador del cargo del empleado
);

-- SQLServer: Distritos
CREATE TABLE distritos (
    id INT IDENTITY(1,1) PRIMARY KEY,                -- Identificador del distrito, auto incrementable
    nombre VARCHAR(255) NOT NULL                      -- Nombre del distrito
);

-- Excel: Cargos
CREATE TABLE cargos (
    id INT AUTO_INCREMENT PRIMARY KEY,                -- Identificador del cargo
    nombre VARCHAR(255) NOT NULL                      -- Nombre del cargo
);


INSERT INTO distritos (nombre) VALUES
('Distrito 1'),
('Distrito 2'),
('Distrito 3'),
('Distrito 4'),
('Distrito 5');

INSERT INTO cargos (nombre) VALUES
('Gerente'),
('Supervisor'),
('Asistente'),
('Analista'),
('Vendedor');


INSERT INTO empleados (nombre, apellidos, fecha_nacimiento, id_distrito, id_cargo) VALUES
('Juan', 'Pérez', '1990-01-15', 1, 1),
('María', 'González', '1985-03-22', 2, 2),
('Carlos', 'López', '1988-11-05', 3, 3),
('Ana', 'Martínez', '1992-07-19', 4, 4),
('Luis', 'Rodríguez', '1980-09-14', 5, 5),
('Patricia', 'Hernández', '1995-12-25', 1, 1),
('Jorge', 'Díaz', '1987-02-10', 2, 2),
('Laura', 'García', '1991-08-30', 3, 3),
('Raúl', 'Sánchez', '1986-05-11', 4, 4),
('Isabel', 'Fernández', '1993-10-03', 5, 5),
('Pedro', 'Jiménez', '1990-04-12', 1, 1),
('Marta', 'Ruiz', '1989-06-09', 2, 2),
('David', 'Pérez', '1983-01-20', 3, 3),
('José', 'Moreno', '1994-11-18', 4, 4),
('Elena', 'Gómez', '1997-02-28', 5, 5),
('Fernando', 'Vázquez', '1982-07-09', 1, 1),
('Sofía', 'Álvarez', '1996-05-13', 2, 2),
('Carmen', 'Castro', '1981-08-22', 3, 3),
('Ricardo', 'Torres', '1990-09-14', 4, 4),
('Raquel', 'Jiménez', '1987-11-30', 5, 5),
('Fernando', 'Hernández', '1993-07-19', 1, 1),
('Beatriz', 'Molina', '1995-10-05', 2, 2),
('Miguel', 'González', '1988-03-10', 3, 3),
('Lucía', 'Martínez', '1989-02-02', 4, 4),
('Juan Carlos', 'Ríos', '1991-01-28', 5, 5),
('Antonio', 'Jiménez', '1994-08-03', 1, 1),
('Cristina', 'Gómez', '1997-06-30', 2, 2),
('Sergio', 'Ramírez', '1992-09-22', 3, 3),
('Carolina', 'Pérez', '1986-10-18', 4, 4),
('Esteban', 'Fernández', '1990-04-07', 5, 5);
