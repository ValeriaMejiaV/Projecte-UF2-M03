import mydb.conexion as conexion
from manipulacion import columnas
def mostrar(id, tabla):
    try: 
        conexion.connectar()
        persona=[]
        mycursor = conexion.mydb.cursor()
        sql=(f"SELECT * FROM {tabla} where id= %s")
        mycursor.execute(sql, [id])
        persona=mycursor.fetchall()
        return persona
    except Exception as e:
           print("Error al mostrar el usuario:", e)
    finally:
        if mycursor:
            conexion.desconnectar()


def obtener_usuario(tabla):
    try:
        conexion.connectar()
        clientes=[]
        mycursor = conexion.mydb.cursor()
        mycursor.execute(f"SELECT * FROM {tabla}")  
        clientes = mycursor.fetchall()
        mycursor.close()
        return clientes
    except Exception as e:
           print("Error al crear el usuario:", e)
    finally:
        if mycursor:
            conexion.desconnectar()




#"empresa", "cif", "adreca", "mail"]
def resultado(usuario,tabla):
    if tabla=='client':
        campo='Telefon'
        for usuario in usuario:
            print(f'''
    {usuario[1]} {usuario[2]}, {usuario[3]}
        id={usuario[0]}
        {campo}={usuario[4]}''')
    elif tabla=='empleat':
        campo='Departamento'
        for usuario in usuario:
            print(f'''
    {usuario[1]} {usuario[2]}, {usuario[3]}
        id={usuario[0]}
        {campo}={usuario[4]}''')
    elif tabla=='proveidor':
        for usuario in usuario:
            print(f'''
    {usuario[1]}
        id={usuario[0]}
        cif={usuario[2]}
        adreca={usuario[3]}
        mail={usuario[4]}''')
   
    
    