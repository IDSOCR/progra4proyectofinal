import sqlite3

# Conexión a la base de datos (si no existe, se crea)
conexion = sqlite3.connect('mi_db.db')
cursor = conexion.cursor()

# Crear tabla de usuarios si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        fecha_registro TEXT NOT NULL,
        contraseña TEXT NOT NULL
    );
''')

conexion.commit()
conexion.close()

print("Base de datos creada y tabla 'usuarios' generada con éxito.")
