from Conexion.conexion import obtener_conexion

def obtener_destinos():
    conexion = obtener_conexion()
    destinos = []
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM destinos")
        destinos = cursor.fetchall()
        cursor.close()
        conexion.close()
    return destinos

def insertar_destino(nombre, pais, precio, cupos):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO destinos (nombre_destino, pais, precio, cupos) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, pais, precio, cupos))
        conexion.commit()
        cursor.close()
        conexion.close()

def actualizar_destino(id_destino, nombre, pais, precio, cupos):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        sql = "UPDATE destinos SET nombre_destino=%s, pais=%s, precio=%s, cupos=%s WHERE id_destino=%s"
        cursor.execute(sql, (nombre, pais, precio, cupos, id_destino))
        conexion.commit()
        cursor.close()
        conexion.close()

def eliminar_destino(id_destino):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM destinos WHERE id_destino = %s", (id_destino,))
        conexion.commit()
        cursor.close()
        conexion.close()