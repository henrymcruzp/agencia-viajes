from flask import Flask, render_template

app = Flask(__name__)

# RUTA 1: PORTADA
@app.route('/')
def home():
    # Ahora renderiza la plantilla en lugar de texto plano
    return render_template('index.html')

# RUTA 2: ACERCA DE (Requerida por la tarea)
@app.route('/about')
def about():
    return render_template('about.html')

# RUTA 3: DINÁMICA (Tu ruta personalizada)
@app.route('/viaje/<destino>')
def destino(destino):
    # Pasamos la variable 'destino' a la plantilla HTML
    return render_template('destino.html', lugar=destino)

if __name__ == '__main__':
    app.run(debug=True)