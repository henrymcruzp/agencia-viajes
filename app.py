from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from inventario.bd import guardar_en_archivos, leer_archivos

app = Flask(__name__)

# Configuración de la Base de Datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Base de datos (Requisito de la tarea)
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

# Crear la base de datos automáticamente al inicio
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nuevo_producto', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])

        # 1. Guardar en SQLite (Base de datos)
        nuevo_prod = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        db.session.add(nuevo_prod)
        db.session.commit()

        # 2. Guardar en Archivos (TXT, JSON, CSV)
        guardar_en_archivos(nombre, precio, cantidad)

        return redirect(url_for('datos'))
    return render_template('producto_form.html')

@app.route('/datos')
def datos():
    # Leer de SQLite
    productos_db = Producto.query.all()
    # Leer de archivos
    datos_txt, datos_json, datos_csv = leer_archivos()
    
    return render_template('datos.html', 
                           productos_db=productos_db,
                           datos_txt=datos_txt,
                           datos_json=datos_json,
                           datos_csv=datos_csv)

if __name__ == '__main__':
    app.run(debug=True)