from flask import Flask

app = Flask(__name__)

# RUTA 1: PORTADA
@app.route('/')
def home():
    return """
    <div style="text-align: center; font-family: Arial, sans-serif;">
        <h1>✈️ Agencia de Viajes 'Mundo Libre' 🌍</h1>
        <p>Bienvenido al inicio de tu próxima aventura.</p>
        <p>Escribe en la URL: <b>/viaje/Europa</b> para ver ofertas.</p>
    </div>
    """

# RUTA 2: DINÁMICA
@app.route('/viaje/<destino>')
def destino(destino):
    return f"<h1>Paquete turístico para: {destino}</h1><p>Buscando vuelos y hoteles disponibles...</p>"

if __name__ == '__main__':
    app.run(debug=True)