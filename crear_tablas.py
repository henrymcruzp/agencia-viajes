# Importamos la conexión que hicimos en el otro archivo
from Conexion.conexion import obtener_conexion

def configurar_base_datos():
    # 1. Llamamos a tu conexión
    conexion = obtener_conexion()
    
    if conexion is not None:
        # 2. El 'cursor' es la herramienta que ejecuta los comandos de SQL
        cursor = conexion.cursor()
        
        # 3. Escribimos nuestro código SQL básico para crear la tabla
        # Usamos IF NOT EXISTS para que no dé error si la corremos dos veces
        sql = """
        CREATE TABLE IF NOT EXISTS destinos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            pais VARCHAR(50) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL
        )
        """
        
        try:
            # 4. Ejecutamos el SQL y guardamos los cambios (commit)
            cursor.execute(sql)
            conexion.commit()
            print("✅ ¡La tabla 'destinos' se creó correctamente en Aiven!")
            
        except Exception as e:
            print("❌ Ocurrió un error al crear la tabla:", e)
            
        finally:
            # 5. Siempre es buena práctica cerrar el cursor y la conexión al terminar
            cursor.close()
            conexion.close()

# Esto hace que la función se ejecute solo si corremos este archivo directamente
if __name__ == "__main__":
    configurar_base_datos()