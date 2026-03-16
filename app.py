from flask import Flask, render_template, request, redirect, url_for
from Conexion.conexion import obtener_conexion

app = Flask(__name__)

# --- GESTIÓN DE DESTINOS (TU PROYECTO) ---

@app.route('/')
def index():
    conexion = obtener_conexion()
    destinos = []
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM destinos")
        destinos = cursor.fetchall()
        cursor.close()
        conexion.close()
    return render_template('index.html', viajes=destinos)

@app.route('/insertar', methods=['POST'])
def insertar():
    nombre = request.form['nombre']
    pais = request.form['pais']
    precio = request.form['precio']
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO destinos (nombre, pais, precio) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, pais, precio))
        conexion.commit()
        cursor.close()
        conexion.close()
    return redirect(url_for('index'))

@app.route('/modificar/<int:id>', methods=['POST'])
def modificar(id):
    nombre = request.form['nombre']
    pais = request.form['pais']
    precio = request.form['precio']
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "UPDATE destinos SET nombre=%s, pais=%s, precio=%s WHERE id=%s"
        cursor.execute(sql, (nombre, pais, precio, id))
        conexion.commit()
        cursor.close()
        conexion.close()
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM destinos WHERE id = %s", (id,))
        conexion.commit()
        cursor.close()
        conexion.close()
    return redirect(url_for('index'))

# --- REQUISITO PUNTO 3 (TABLA USUARIOS) ---

@app.route('/usuarios')
def lista_usuarios():
    conexion = obtener_conexion()
    usuarios = []
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id_usuario, nombre, mail FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
    return f"Tabla Usuarios (Punto 3): {str(usuarios)} <br><br> <a href='/crear_admin'>[Click aquí para insertar un usuario de prueba]</a>"

@app.route('/crear_admin')
def crear_admin():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre, mail, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, ("Admin_Agencia", "admin@viajes.com", "12345"))
        conexion.commit()
        cursor.close()
        conexion.close()
    return "✅ Usuario de prueba creado. Regresa a <a href='/usuarios'>/usuarios</a> para verificar."

import os

if __name__ == '__main__':
    # Render usa la variable de entorno PORT, si no existe usa el 5000
    port = int(os.environ.get('PORT', 5000))
    # Importante: host='0.0.0.0' para que sea visible en la web
    app.run(host='0.0.0.0', port=port, debug=True)