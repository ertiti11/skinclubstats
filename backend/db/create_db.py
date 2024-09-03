import sqlite3

# Conectar a la base de datos (esto crea el archivo si no existe)
conn = sqlite3.connect('skins_database.sqlite')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Leer el archivo SQL y ejecutar sus contenidos
with open('newdb.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Ejecutar el script SQL
cursor.executescript(sql_script)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos y tablas creadas con éxito.")