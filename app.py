from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'clave_secreta_innovaweb'  # Para sesiones (puedes cambiarla por seguridad)

# Función para conectarse a la base de datos
def get_db_connection():
    conn = sqlite3.connect('mi_db.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta principal
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', usuario=session['username'])
    return redirect(url_for('login'))

# Ruta de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (username, nombre, email, fecha_registro, contraseña) VALUES (?, ?, ?, ?, ?)",
                           (username, nombre, email, fecha, password))
            conn.commit()
            flash('Registro exitoso. Inicia sesión.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El nombre de usuario ya existe.', 'danger')
        finally:
            conn.close()

    return render_template('register.html')

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND contraseña = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = user['username']
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('login'))

# Iniciar la app
if __name__ == '__main__':
    app.run(debug=True)
