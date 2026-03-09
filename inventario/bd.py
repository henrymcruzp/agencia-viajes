import os
import json
import csv

# Crea la carpeta 'data' automáticamente si no existe
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

TXT_FILE = os.path.join(DATA_DIR, 'datos.txt')
JSON_FILE = os.path.join(DATA_DIR, 'datos.json')
CSV_FILE = os.path.join(DATA_DIR, 'datos.csv')

def guardar_en_archivos(nombre, precio, cantidad):
    # 1. Guardar en TXT
    with open(TXT_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{nombre},{precio},{cantidad}\n")

    # 2. Guardar en JSON
    datos_json = []
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                datos_json = json.load(f)
            except:
                pass
    datos_json.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(datos_json, f, indent=4)

    # 3. Guardar en CSV
    archivo_existe = os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not archivo_existe:
            writer.writerow(['Nombre', 'Precio', 'Cantidad'])
        writer.writerow([nombre, precio, cantidad])

def leer_archivos():
    # Leer TXT
    datos_txt = []
    if os.path.exists(TXT_FILE):
        with open(TXT_FILE, 'r', encoding='utf-8') as f:
            datos_txt = f.readlines()

    # Leer JSON
    datos_json = []
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                datos_json = json.load(f)
            except:
                pass

    # Leer CSV
    datos_csv = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            datos_csv = list(reader)

    return datos_txt, datos_json, datos_csv