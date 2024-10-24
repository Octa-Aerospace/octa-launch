#!/bin/bash

# Configuración inicial
echo "[ - ] Comenzando la configuración de MySQL..."

# # Crear el usuario 'octasat' y otorgarle privilegios
echo "[ - ] Creando usuario y otorgando privilegios..."
mysql -u root <<EOF
CREATE USER 'octasat'@'localhost' IDENTIFIED BY 'octasat';
GRANT ALL PRIVILEGES ON *.* TO 'octasat'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EOF

echo "[ ok ] Usuario creado y configurado."

# Crear la base de datos 'OctaSatDB' y la tabla 'telemetry_data'
mysql -u octasat -poctasat <<EOF
SET GLOBAL time_zone = '+00:00';
CREATE DATABASE IF NOT EXISTS OctaSatDB;
USE OctaSatDB;

CREATE TABLE telemetry_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    latitude DECIMAL(10, 7),
    longitude DECIMAL(10, 7),
    altitude FLOAT,
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    accel_x FLOAT DEFAULT 0,
    accel_y FLOAT DEFAULT 0,
    accel_z FLOAT DEFAULT 0,
    gyro_x FLOAT DEFAULT 0,
    gyro_y FLOAT DEFAULT 0,
    gyro_z FLOAT DEFAULT 0,
    mag_x FLOAT DEFAULT 0,
    mag_y FLOAT DEFAULT 0,
    mag_z FLOAT DEFAULT 0
);
EOF

echo "[ ok ] Base de datos y tablas creadas."

# Verificar en qué puerto está corriendo MySQL
port=$(mysql -u octasat -poctasat -e "SHOW VARIABLES LIKE 'port';" -s -N | cut -f 2)
echo "[ ok ] MySQL está corriendo en el puerto: $port"

echo "[ ok ] Puedes acceder a MySQL en la URL: localhost:$port"
echo "\nConfiguración completa."
