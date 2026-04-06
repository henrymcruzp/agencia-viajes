import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="bd-agencia-viajes-henrym-55a8.g.aivencloud.com",
            user="avnadmin",
            password="AVNS_7I8aRf86TR7fNZd7POO",
            port=26128,
            database="defaultdb"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a MySQL: {err}")
        return None
