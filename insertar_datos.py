# Traemos la conexión que ya configuramos antes
from Conexion.conexion import obtener_conexion

def cargar_datos():
    # Iniciamos la conexión
    conexion = obtener_conexion()
    
    if conexion:
        cursor = conexion.cursor()
        
        # El comando SQL para insertar (los %s son espacios para los datos)
        sql = "INSERT INTO destinos (nombre, pais, precio) VALUES (%s, %s, %s)"
        
        # Los datos de tu Agencia de Viajes
        datos_viajes = [
            ("Islas Galápagos", "Ecuador", 850.50),
            ("Machu Picchu", "Perú", 620.00),
            ("Cancún", "México", 780.00),
            ("Punta Cana", "República Dominicana", 900.00)
        ]
        
        try:
            # Insertamos todos los viajes de un solo golpe
            cursor.executemany(sql, datos_viajes)
            
            # ¡IMPORTANTE! El commit guarda los cambios permanentemente
            conexion.commit()
            
            print(f"✅ ¡Éxito! Se insertaron {cursor.rowcount} destinos en Aiven.")
            
        except Exception as e:
            print("❌ Hubo un error al insertar:", e)
            
        finally:
            # Cerramos todo para no dejar la puerta abierta
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    cargar_datos()