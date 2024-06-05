import mydb.conexion as conexion
from manipulacion.crud import crear_usuario
from manipulacion.crud import eliminarUsuario 
from manipulacion.crud import modificar_usuario 
from manipulacion.Mostrar import obtener_usuario
from manipulacion.Mostrar import mostrar 
from manipulacion.Mostrar import resultado 

menuPrincipal='''
      Menu Principal 
      ----------------
      0. Salir
      1. Clientes
      2. Proveedores
      3. Trabajadores
      '''
menuSecundario='''
      Que accion deseas realizar? 
      ---------------------------
      0.Salir
      1. Crear 
      2. Modificar 
      3. Eliminar 
      4. Mostrar
      5. Listar

'''

try:
    conexion.connectar()
except Exception as e:
    print("ERROR obrint la connexió de DB")    
else:
      opcion=None
      salir=0
      
      while opcion != salir:
            print(menuPrincipal)

            ok = False
            while not ok:
                  try:
                        opcion = int(input("\nIntroduce una opción: "))
                  except:
                        print("No has introducido una opcion valida")
                  else:
                        ok = True
                  if opcion==1:
                        ####CLIENTES####
                        print('''
Clients
-------------------''')
                        
                        bucleCliente=False
                        while not bucleCliente:
                              tabla="client"
                              print(menuSecundario)
                              accion=int(input("\nIntrodueix una opció: "))
                              if accion == 1:
                                    print('Crear un cliente nuevo')
                                    
                                    nom=str(input('Introduce el nombre del nuevo cliente:'))
                                    cognom1=str(input('Ahora introduce el primer apellido del cliente:'))
                                    cognom2=str(input('Ahora introduce el segundo apellido del cliente:'))
                                    telefon=int(input('Ahora introduce el telefono del cliente:'))
                                    try:
                                          count=crear_usuario(nom,cognom1, cognom2, telefon, tabla)
                                          print(count, "usuario insertado!")
                                    except Exception as e:
                                          print("ERROR: No se ha podido insertar.")
                                          print(e)

                              elif accion == 2:
                                    try:
                                          print('Modificar un cliente ')
                                          
                                          id=int(input('Introduce el id de a quien quieres ver:'))
                                          info=mostrar(id, tabla)
                                          nom=info[0][1]
                                          cognom1=info[0][2]
                                          cognom2=info[0][3]
                                          telefon=info[0][4]
                                          print(f'''
                                                Nombre: {nom}
                                                Apellidos: {cognom1}, {cognom2}
                                                Telefono: {telefon}''')
                                          campo=str(input('Que deseas cambiar?:'))
                                          if campo=='Nombre' or campo=='nombre':
                                                nuevo_nom=str(input('Que nombre deseas poner?:'))
                                                if nom!=None:
                                                      nom=nuevo_nom
                                          elif campo=='Apellidos' or campo=='apellidos':
                                                cognom=str(input(f'Que apellido deseas cambiar? {cognom1} / {cognom2}:'))
                                                if cognom==cognom1:
                                                      nuevo_cognom1=str(input(f'Por que apellido deseas cambiar {info[0][2]}?: '))
                                                      if nuevo_cognom1!=None:
                                                            cognom1=nuevo_cognom1
                                                elif cognom==cognom2:
                                                      nuevo_cognom2=str(input(f'Por que apellido deseas cambiar {info[0][3]}?: '))
                                                      if nuevo_cognom2!=None:
                                                            cognom2=nuevo_cognom2
                                          elif campo=='Telefono' or campo=='telefono':
                                                nuevo_telefon=str(input('Que telefono deseas poner?:'))
                                                if nuevo_telefon!=None:
                                                      telefon=nuevo_telefon
                                          else:
                                                print('Opcio incorrecta.')
                                          info=modificar_usuario(id,nom, cognom1, cognom2, telefon, tabla)
                                          print(info)
                                    
                                    
                                    except Exception as e:
                                          print(f"Error al modificar el cliente:{e}")
                              elif accion == 3:
                                    try:
                                          print('Eliminar un cliente ')
                                          id=int(input('Introduce el id de a quien quieres ver:'))
                                          info=mostrar(id, tabla)
                                          confirmacion=str(input(f'Estas seguro de que quieres eliminar a {info[0][1]}?S/N:'))
                                          if confirmacion=='s' or confirmacion=='S':
                                                print('Eliminando...')
                                                info=eliminarUsuario(id, tabla)
                                                print(info)
                                          elif confirmacion=='n' or confirmacion=='N':
                                                print('Cancelando operacion')
                                    except Exception as e:
                                          print(f"Error al eliminar el cliente:{e}")
                              elif accion == 4:
                                    try:
                                          print('Mostrar un cliente ')
                                          id=int(input('Introduce el id de a quien quieres ver:'))
                                          info=mostrar(id, tabla)
                                          print(f'''
                                                Nombre: {info[0][1]}
                                                Apellidos: {info[0][2]}, {info[0][3]}
                                                Telefono: {info[0][4]}''')
                                    except Exception as e:
                                          print(f"Error al mostrar el cliente:{e}")
                              elif accion == 5:
                                    print('Listar los clientes')
                                    usuarios=obtener_usuario(tabla)
                                    info=resultado(usuarios, tabla)
                                          
                              elif accion == 0:
                                    print('Fuera de cliente')
                                    bucleCliente=True


                  elif opcion==2:
                        ######PROVEEDORES####
                        print('''
Proveedores
-------------------''')
                        
                        bucleProveedores=False
                        while not bucleProveedores:
                              tabla="proveidor"
                              print(menuSecundario)

                              accion=int(input("\nIntrodueix una opció: "))
                              if accion == 1:
                                    print('Crear un proveedor nuevo')
                                    empresa=str(input('Introduce el nombre de la empresa:'))
                                    cif=str(input('Ahora introduce el cif la empresa:'))
                                    direccion=str(input('Ahora introduce la direccion de la empresa:'))
                                    email=str(input('Ahora introduce el email de la empresa:'))
                                    try:
                                          count=crear_usuario(empresa,cif, direccion, email, tabla)
                                          print(count, "usuario insertado!")
                                    except Exception as e:
                                          print("ERROR: No se ha podido insertar la empresa.")
                                          print(e)

                              elif accion == 2:
                                    print('Modificar un proveedor ')
                                    try:
                                          usuarios=obtener_usuario(tabla)
                                          info=resultado(usuarios, tabla)
                                          id=int(input('Introduce el id del proveedor al que deseas ver:'))
                                          info=mostrar(id, tabla)
                                          empresa=info[0][1]
                                          cif=info[0][2]
                                          adreca=info[0][3]
                                          email=info[0][4]
                                          print(f'''
                                                Empresa: {empresa}
                                                CIF: {cif}
                                                Adreça: {adreca}
                                                E-mail: {email}''')
                                          campo=str(input('Que deseas cambiar?:'))
                                          if campo=='Empresa' or campo=='empresa':
                                                nuevo_nom_empresa=str(input('Que nombre deseas poner?:'))
                                                if nuevo_nom_empresa!=None:
                                                      empresa=nuevo_nom_empresa
                                          elif campo=='CIF' or campo=='cif':
                                                nuevo_cif=str(input(f'Por que cif deseas cambiar {cif}? :'))
                                                if nuevo_cif!=None:
                                                      cif=nuevo_cif
                                          elif campo=='Adreça' or campo=='adreça':
                                                nueva_adreca=str(input('Que adreça deseas poner?:'))
                                                if nueva_adreca!=None:
                                                      adreca=nueva_adreca
                                          elif campo=='email' or campo=='e-mail' or campo=='E-mail':
                                                nuevo_email=str(input('Que E-mail deseas poner?:'))
                                                if nuevo_email!=None:
                                                      email=nuevo_email
                                          else:
                                                print('Opcio incorrecta.')
                                          info=modificar_usuario(id,empresa, cif, adreca, email, tabla)
                                          print(info)
                                    
                                    
                                    except Exception as e:
                                          print(f"Error al modificar el usuario:{e}")
                              elif accion == 3:
                                    print('Eliminar un proveedor ')
                                    try:
                                          usuarios=obtener_usuario(tabla)
                                          info=resultado(usuarios, tabla)
                                          usuarios=obtener_usuario(tabla)
                                          info=resultado(usuarios, tabla)
                                          id=int(input('Introduce el id de del trabajador al que deseas eliminar:'))
                                          info=mostrar(id, tabla)
                                          confirmacion=str(input(f'Estas seguro de que quieres eliminar a {info[0][1]}?S/N:'))
                                          if confirmacion=='s' or confirmacion=='S':
                                                print('Eliminando...')
                                                info=eliminarUsuario(id, tabla)
                                                print(info)
                                          elif confirmacion=='n' or confirmacion=='N':
                                                print('Cancelando operacion')
                                    except Exception as e:
                                          print(f"Error al eliminar el usuario:{e}")
                              elif accion == 4:
                                    print('Mostrar un proveedor ')
                                    try:
                                          # usuarios=Listado.obtener_usuario(tabla)
                                          # resultado=Mostrar.resultado(usuarios, tabla)
                                          nombre=str(input('Introduce el nombre del proveedor al que quieres ver:'))
                                          info=mostrar(nombre, tabla)
                                          empresa=info[0][1]
                                          cif=info[0][2]
                                          adreca=info[0][3]
                                          email=info[0][4]
                                          print(f'''
                                                Empresa: {empresa}
                                                CIF: {cif}
                                                Adreça: {adreca}
                                                E-mail: {email}''')
                                    except Exception as e:
                                          print(f"Error al mostrar el usuario:{e}")
                              elif accion == 5:
                                    print('Listar los proveedor')
                                    usuarios=obtener_usuario(tabla)
                                    info=resultado(usuarios, tabla)
                              elif accion == 0:
                                    print('Fuera de proveedor')
                                    bucleProveedores=True
                        

                  
                  elif opcion==3:
                        ######TRABAJADORES#####
                        print('''
Trabajadores
-------------------''')
                       
                        bucleTrabajadores=False
                        while not bucleTrabajadores:
                              tabla="empleat"
                              print(menuSecundario)
                              accion=int(input("\nIntrodueix una opció: "))
                              if accion == 1:
                                    print('Crear un trabajadores nuevo')
                                    nom=str(input('Introduce el nombre del nuevo cliente:'))
                                    cognom1=str(input('Ahora introduce el primer apellido del cliente:'))
                                    cognom2=str(input('Ahora introduce el segundo apellido del cliente:'))
                                    departament=str(input('Ahora introduce el departamento del cliente:'))
                                    try:
                                          count=crear_usuario(nom,cognom1, cognom2, departament, tabla)
                                          print(count, "usuario insertado!")
                                    except Exception as e:
                                          print("ERROR: No se ha podido insertar el usuario")
                                          print(e)
                              elif accion == 2:
                                    try:

                                          print('Modificar un trabajador ')
                                          usuarios=obtener_usuario(tabla)
                                          info=resultado(usuarios, tabla)
                                          id=int(input('Introduce el id del trabajador al que deseas ver:'))
                                          info=mostrar(id, tabla)
                                          nom=info[0][1]
                                          cognom1=info[0][2]
                                          cognom2=info[0][3]
                                          departament=info[0][4]
                                          print(f'''
                                                Nombre: {nom}
                                                Apellidos: {cognom1}, {cognom2}
                                                Departamento: {departament}''')
                                          campo=str(input('Que deseas cambiar?:'))
                                          if campo=='Nombre' or campo=='nombre':
                                                nuevo_nom=str(input('Que nombre deseas poner?:'))
                                                if nom!=None:
                                                      nom=nuevo_nom
                                          elif campo=='Apellidos' or campo=='apellidos':
                                                cognom=str(input(f'Que apellido deseas cambiar? {cognom1} / {cognom2}:'))
                                                if cognom==cognom1:
                                                      nuevo_cognom1=str(input(f'Por que apellido deseas cambiar {info[0][2]}?: '))
                                                      if nuevo_cognom1!=None:
                                                            cognom1=nuevo_cognom1
                                                elif cognom==cognom2:
                                                      nuevo_cognom2=str(input(f'Por que apellido deseas cambiar {info[0][3]}?: '))
                                                      if nuevo_cognom2!=None:
                                                            cognom2=nuevo_cognom2
                                          elif campo=='Departamento' or campo=='departamento':
                                                nuevo_departament=str(input('Que departamento deseas poner?:'))
                                                if nuevo_departament!=None:
                                                      departament=nuevo_departament
                                          else:
                                                print('Opcio incorrecta.')
                                          info=modificar_usuario(id,nom, cognom1, cognom2, departament, tabla)
                                          print(info)
                                    
                                    
                                    except Exception as e:
                                          print(f"Error al modificar el usuario:{e}")
                              elif accion == 3:
                                    try:
                                          print('Eliminar un trabajador ')
                                          usuarios=obtener_usuario(tabla)
                                          info=resultado(usuarios, tabla)
                                          id=int(input('Introduce el id de del trabajador al que deseas eliminar:'))
                                          info=mostrar(id, tabla)
                                          confirmacion=str(input(f'Estas seguro de que quieres eliminar a {info[0][1]}?S/N:'))
                                          if confirmacion=='s' or confirmacion=='S':
                                                print('Eliminando...')
                                                info=eliminarUsuario(id, tabla)
                                                print(info)
                                          elif confirmacion=='n' or confirmacion=='N':
                                                print('Cancelando operacion')
                                    except Exception as e:
                                          print(f"Error al eliminar el usuario:{e}")
                              elif accion == 4:
                                    try:
                                          print('Mostrar un cliente ')

                                          id=int(input('Introduce el id del trabajador al que quieres ver:'))
                                          info=mostrar(id, tabla)
                                          print(f'''
                                                Nombre: {info[0][1]}
                                                Apellidos: {info[0][2]}, {info[0][3]}
                                                Telefono: {info[0][4]}''')
                                    except Exception as e:
                                          print(f"Error al mostrar el usuario:{e}")
                              elif accion == 5:
                                    print('Listar los trabajador')
                                    usuarios=obtener_usuario(tabla)
                                    info=resultado(usuarios, tabla)
                                    
                              elif accion == 0:
                                    print('Fuera de trabajador')
                                    bucleTrabajadores=True
                  else:
                        print('Opcion incorrecta')
finally:
      conexion.desconnectar()