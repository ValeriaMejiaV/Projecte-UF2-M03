import  mysql.connector

def connectar():
    global mydb
    print("Obrint connexió a la BD...")
    mydb = mysql.connector.connect(
      host="shared.daw.cat",
      user="1dd14",
      password="1ASIXdaw*14",
      port="3306",
      database="1dd14_gestor_negocis"
    )

def desconnectar():
    mydb.close()