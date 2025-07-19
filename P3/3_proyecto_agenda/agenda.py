import mysql.connector
from mysql.connector import Error

def borrarPantalla(): 
    import os 
    os.system("cls")

def esperarTecla():
    print(" 🕒 Oprima cualquier tecla para continuar 🕒 ...")
    input()  

def menu_principal():
    print("\n\t📝...::: Sistema de Gestión de Agenda de Contactos:::...📝\n\n\t\t 1️⃣  Agregar contacto \n\t\t 2️⃣  Mostrar todos los contactos \n\t\t 3️⃣  Buscar contacto por nombre \n\t\t 4️⃣  Modificar contacto \n\t\t 5️⃣  Eliminar contacto   \n\t\t 6️⃣  SALIR  ")
    opcion=input("\n\t\t  👉 Elige una opción (1-6): ").upper()
    return opcion


def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda_yo" 
        )
        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
    return None



def agregar_contacto(agenda):
    borrarPantalla()
    print("\t📝.::Agregar contactos::.📝\n")
    conexion=conectar()
    if conexion!=None:
        nombre=input("👤 Nombre del contacto: ").upper().strip()
        cursor=conexion.cursor()
        cursor.execute(
            "select * from agenda where nombre=%s", (nombre,)
        )
        registro=cursor.fetchone()
        if not registro:
            tel=input("📞 Telefono: ").strip()
            email=input("📧 E-mail: ").lower().strip()
            #agregar el atributo nombre al dict con los valores de tel y email en listas
            agenda[nombre]=[tel,email]
            try: 
                cursor.execute(
                    "insert into agenda (id, nombre, numero, correo) values (NULL, %s, %s, %s)", (nombre, tel, email)
                )
                conexion.commit()
                print("\n\t\t ✅ Accion realizada con exito ✅")
            except Error as e:
                print("⚠️  Error al insertar  ⚠️")
        else:
            print("⚠️  El nombre ya existe  ⚠️")
        




def mostrar_contacto(agenda):
    borrarPantalla()
    print("\t🔍.::Mostrar Contactos::.🔍\n") 
    conexion=conectar()
    if conexion!=None:
        cursor=conexion.cursor()
        cursor.execute(
            "select * from agenda"
        )
        registros=cursor.fetchall()
        if len(registros)>0:
            print(f"{'ID':<10}{'nombre':<15}{'numero':<15}{'correo':<15}")
            print(F"-"*50)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}")
        else:
            print("\t .:: ⚠️ No hay peliculas en el sistema ⚠️::.") 
    
            

def buscar_contacto(agenda):
    borrarPantalla()
    print("\t🔍 .:: Buscar Contacto ::. 🔍\n")
    conexion=conectar()
    if conexion!=None:
        cursor=conexion.cursor()
        nombre=input("📝 Teclea el nombre del contacto a buscar: ").upper().strip()
        cursor.execute(
            "select * from agenda where nombre=%s", (nombre,)
        )
        registro=cursor.fetchall()
        if registro:
            for i in registro:
                print(f"ID: {i[0]}")
                print(f"Nombre: {i[1]}")
                print(f"Numero: {i[2]}")
                print(f"Correo: {i[3]}")
                print("-------------------------------")
        else:
            print("⚠️  Nombre no encontrado  ⚠️")



def modificar_contacto(agenda):
    borrarPantalla()
    print("\t🔄 .:: Modificar Contacto ::. 🔄\n")
    conexion=conectar()
    if conexion!=None:
        cursor=conexion.cursor()
        cursor.execute(
            "select * from agenda"
        )
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'nombre':<15}{'numero':<15}{'correo':<15}")
            print(F"-"*50)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}")
        else:
            print(" ⚠️ No hay registros ⚠️ ")
        id=int(input("Teclea el id del registro que quieras modificar: "))
        cursor.execute(
        "select * from agenda where id=%s", (id,)
        )
        registro=cursor.fetchone()
        if registro:
            nombre =input("Nuevo nombre: ").upper().strip()
            numero=input("Nuevo numero: ").upper().strip()
            correo=input("Nuevo correo: ").upper().strip()
            try:
                cursor.execute(
                    "update agenda set nombre=%s, numero=%s, correo=%s where id=%s",(nombre,numero,correo,id)
                )
                conexion.commit()
                print(".:: ✅ Operacion realizada con exito ✅ ::.")
            except Error as e:
                print("⚠️  Error al modificar  ⚠️")
        else:
            print("⚠️  ID no encontrada  ⚠️")


def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t.:: 📛 Borrar o quitar contacto 📛 ::.\n ")
    conexion=conectar()
    if conexion!=None:
        cursor=conexion.cursor()
        cursor.execute(
            "select * from agenda"
        )
        registros=cursor.fetchall()
        if len(registros)>0:
            print(f"{'ID':<10}{'nombre':<15}{'numero':<15}{'correo':<15}")
            print(F"-"*50)
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}")
        else:
            print(" ⚠️ No hay registros ⚠️ ")
            
        id=int(input("Teclea el indice del registro a borrar: "))
        cursor.execute(
            "select * from agenda where id=%s", (id,)
            )
        registro=cursor.fetchone()
        if registro:
            resp=input("⚠️ Deseas borrar  del sistema? (S/N) ⚠️ :").lower()
            if resp=="s":
                try:
                    cursor.execute(
                        "DELETE FROM agenda WHERE id = %s", (id,)
                        #, AL FINAL PORQUE ESTO LO HACE CON TUPLAS O LISTAS Y PARA TUPLAS SE OCUPAN 2 O MAS ELEMENTOS LO PUEDO HACER CON LISTA TAMBIEN SIN LA ,
                    )   
                    conexion.commit()
                    print(".:: ✅ Operacion realizada con exito ✅ ::.")
                except Error as e:
                    print("⚠️  Error al eliminar  ⚠️")
        else:
            print("⚠️  ID no encontrada  ⚠️")
