import mysql.connector
import os
from dotenv import load_dotenv

# Esto carga los datos que pusimos en el archivo .env
load_dotenv()

def obtener_conexion():
    try:
        # Nos conectamos a MySQL usando las variables
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        return conexion
        
    except Exception as e:
        print("Hubo un error al conectar a la base de datos:", e)
        return None