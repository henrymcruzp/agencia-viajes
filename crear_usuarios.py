from Conexion.conexion import obtener_conexion

def crear_tabla_usuarios():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            mail VARCHAR(100),
            password VARCHAR(100)
        )
        """
        cursor.execute(sql)
        conexion.commit()
        print("✅ Tabla 'usuarios' creada (Requisito obligatorio cumplido)")
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    crear_tabla_usuarios()