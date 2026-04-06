from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from Conexion.conexion import obtener_conexion
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from fpdf import FPDF
import os

from modelos.user import User 
from services.destino_service import obtener_destinos, insertar_destino, actualizar_destino, eliminar_destino

app = Flask(__name__)
app.secret_key = 'clave_secreta_proyect' 

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        if usuario:
            return User(usuario['id_usuario'], usuario['nombre'], usuario['email'])
    return None

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        pw_hash = generate_password_hash(password)
        
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            if cursor.fetchone():
                flash("El email ya existe", "error")
            else:
                cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)", 
                               (nombre, email, pw_hash))
                conexion.commit()
                flash("Registro exitoso", "success")
                return redirect(url_for('login'))
            cursor.close()
            conexion.close()
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            usuario = cursor.fetchone()
            cursor.close()
            conexion.close()
            if usuario and check_password_hash(usuario['password'], password):
                user_obj = User(usuario['id_usuario'], usuario['nombre'], usuario['email'])
                login_user(user_obj)
                return redirect(url_for('index'))
            flash("Datos incorrectos", "error")
    return render_template('login.html')

@app.route('/')
@login_required
def index():
    destinos = obtener_destinos()
    return render_template('index.html', viajes=destinos, usuario=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/insertar', methods=['POST'])
@login_required
def insertar():
    insertar_destino(request.form['nombre_destino'], request.form['pais'], request.form['precio'], request.form.get('cupos', 0))
    return redirect(url_for('index'))

@app.route('/actualizar/<int:id_destino>', methods=['POST'])
@login_required
def actualizar(id_destino):
    nombre = request.form['nombre_destino']
    pais = request.form['pais']
    precio = request.form['precio']
    cupos = request.form.get('cupos', 0)
    
    actualizar_destino(id_destino, nombre, pais, precio, cupos)
    flash("Destino actualizado correctamente", "success")
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    eliminar_destino(id)
    return redirect(url_for('index'))

@app.route('/reporte_pdf')
@login_required
def reporte_pdf():
    destinos = obtener_destinos()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "Reporte de Destinos Turisticos", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Destino", 1)
    pdf.cell(50, 10, "Pais", 1)
    pdf.cell(40, 10, "Precio", 1)
    pdf.cell(40, 10, "Cupos", 1)
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for d in destinos:
        pdf.cell(60, 10, str(d.get('nombre_destino', 'N/A')), 1)
        pdf.cell(50, 10, str(d.get('pais', 'N/A')), 1)
        pdf.cell(40, 10, f"${d.get('precio', 0)}", 1)
        pdf.cell(40, 10, str(d.get('cupos', 0)), 1)
        pdf.ln()

    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=reporte_destinos.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)