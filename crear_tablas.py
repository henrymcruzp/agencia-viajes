from Conexion.conexion import obtener_conexion

def configurar_base_datos():
    conexion = obtener_conexion()
    
    if conexion is not None:
        cursor = conexion.cursor()
        
        # SQL para la tabla de Destinos (Semana anterior)
        sql_destinos = """
        CREATE TABLE IF NOT EXISTS destinos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            pais VARCHAR(50) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL
        )
        """
        
        # SQL para la tabla de Usuarios (REQUISITO SEMANA 13)
        sql_usuarios = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        
        try:
            # Creamos la tabla de destinos
            cursor.execute(sql_destinos)
            print("✅ Tabla 'destinos' verificada/creada.")
            
            # Creamos la tabla de usuarios
            cursor.execute(sql_usuarios)
            print("✅ Tabla 'usuarios' verificada/creada correctamente.")
            
            conexion.commit()
            
        except Exception as e:
            print("❌ Ocurrió un error al crear las tablas:", e)
            
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    configurar_base_datos()