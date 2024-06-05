import mydb.conexion as conexion
from manipulacion import columnas


def crear_usuario(nom, cognom1, cognom2, telefon, tabla):
    try:
        mycursor = conexion.mydb.cursor()
        sql = f"""INSERT INTO {tabla} ({columnas[tabla][0]}, {columnas[tabla][1]}, {columnas[tabla][2]}, {columnas[tabla][3]}) 
                VALUES (%s, %s, %s, %s )"""
        mycursor.execute(sql, [nom, cognom1, cognom2, telefon])
        conexion.mydb.commit()
        count=mycursor.rowcount
        mycursor.close()
        return count
    except Exception as e:
           print("Error al crear el usuario:", e)
    finally:
        if mycursor:
            conexion.desconnectar()

def eliminarUsuario(id, tabla):
    try:
        conexion.connectar()
        mycursor = conexion.mydb.cursor()
        sql = f"DELETE FROM {tabla} WHERE id = %s"
        mycursor.execute(sql, [id])
        conexion.mydb.commit()
        print("Usuario eliminado")
    except Exception as e:
        print("Error al eliminar usuario:", e)
    finally:
        if mycursor:
            conexion.desconnectar()


def modificar_usuario(id,campo1, campo2, campo3, campo4, tabla):
    try:
        mycursor = conexion.mydb.cursor()
        sql = f"""UPDATE {tabla} SET {columnas[tabla][0]}=%s, {columnas[tabla][1]}=%s, {columnas[tabla][2]}=%s, {columnas[tabla][3]}=%s where id=%s 
                """
        mycursor.execute(sql, [campo1, campo2, campo3, campo4, id])
        conexion.mydb.commit()
        count=mycursor.rowcount
        mycursor.close()
        return count
    except Exception as e:
           print("Error al modificar el usuario:", e)
    finally:
        if mycursor:
            conexion.desconnectar()


