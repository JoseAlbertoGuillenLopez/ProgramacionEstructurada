import mysql.connector
from mysql.connector import Error

def borrarPantalla(): 
    import os 
    os.system("cls")

def esperarTecla():
    print(" 🕒 Oprima cualquier tecla para continuar 🕒 ...")
    input()  

def menu_principal():
    print("\n\t📝.:: Sistema de Gestión de calificaciones::.📝\n\n\t\t 1️⃣  Agregar \n\t\t 2️⃣  Mostrar  \n\t\t 3️⃣  Calcular promedios  \n\t\t 4️⃣  Buscar alumno \n\t\t 5️⃣  SALIR  ")
    opcion=input("\n\t\t  👉 Elige una opción (1-5): ").upper()
    return opcion

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print("El error que ocurrio fue: ",e)
        return None

def agregar_calificaciones(lista):
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\t📝.::Agregar calificaciones::.📝\n")
        nombre=input("📝 Nombre del alumno: ").upper().strip()
        calificaciones=[]
        for i in range(1,4):
            continua=True
            while continua:
                try:
                    cal=float(input(f"📝 Calificacion {i}:"))
                    if cal>=0 and cal<11:
                        calificaciones.append(cal)
                        continua=False
                    else:
                        print(" ⚠️ Ingresa un numero valido ⚠️ ")
                except ValueError:
                    print("⚠️ Ingresa un valor numerico ⚠️")
        lista.append([nombre]+calificaciones)

        try:
            cursor=conexion.cursor() 
            cursor.execute(
                "insert into calificaciones (id,nombre,cal1,cal2,cal3) values (NULL,%s,%s,%s,%s)", (nombre,calificaciones[0],calificaciones[1],calificaciones[2])
            )
            conexion.commit()
            print("\t✅ Accion realizada con exito ✅ ")
        except Error as e:
            print("⚠️  Error al insertar registro  ⚠️") 


def mostrar_calificaciones(lista):
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\t🔍.::Mostrar calificaciones calificaciones::.🔍")
        cursor=conexion.cursor()
        cursor.execute(
            "select * from calificaciones"
        )
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'nombre':<20}{'calificacion 1':<20}{'calificacion 2':<20}{'calificacion 3':<20}")
            print(F"{'-'*85}")
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<20}{i[2]:<20}{i[3]:<20}{i[4]:<20}")
            num=len(registros)
            print(f"\nSon {num} Alumnos 👤")
        else:
            print("\t .:: ⚠️ No hay peliculas en el sistema ⚠️::.")


    

            
def calcular_promedios2(lista):
    '''borrarPantalla()
    print(".::PROMEDIOS::.")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calf.1':<10}{'Calf.2':<10}{'Calf.3':<10}{'Promedio':<10}")
        print(f"{'-'*55}")
        contador=0
        for fila in lista:
            prom=float(fila[1]+fila[2]+fila[3])/3
            contador=contador+prom
            print(F"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}{prom}")
            
        print(f"{'-'*55}")
        contador=contador/len(lista)
        print(f"\n El promedio total es {contador}")
    else:
        print("No hay calificaciones en el sistema")'''

    borrarPantalla()
    print("\t.::PROMEDIOS::.")
    if len(lista)>0:
        print(f"{'👤 Alumno':<15}{'📊 Promedio':<10}")
        print(f"{'-'*25}")
        promedio_grup=0
        for fila in lista:
            nombre=fila[0]
            i=1
            suma=0
            promedio=0
            while i<=3:
                suma+=fila[i]
                i=i+1
            promedio=suma/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grup+=promedio
        print(f"{'-'*25}")
        promedio_grup=promedio_grup/len(lista)
        print(f"El promedio grupal es: {promedio_grup}")
    else:
        print("No hay calificaciones en el sistema")

def calcular_promedios1(lista):
    #fila[1:] todos los valores desde la posi 1 hasta el final
    #sum(fila[1:])/3
    conexion=conectar()
    if conexion!=None:
        borrarPantalla()
        print("\t📊.::PROMEDIOS::.📊")
        print("")
        cursor=conexion.cursor()

        cursor.execute(
            "select * from calificaciones"
        )
        registros=cursor.fetchall()

        if registros:
            print(f"{'ID':<10}{'Nombre':<20}{'Promedio':<20}")
            print(F"{'-'*40}")
            for i in registros:
                #ot=(i[2]+i[3]+i[4])/3
                suma=sum(i[2:])/3
                print(f"{i[0]:<10}{i[1]:<20}{suma:<20}")
            num=len(registros)
            print(f"\nSon {num} Alumnos 👤")
        else:
            print("\t .:: ⚠️ No hay peliculas en el sistema ⚠️::.")
        




def buscarAlumno(lista):
    borrarPantalla()
    conexion=conectar()
    if conexion!=None:
        print("\t🔍.::Buscar Alumno::.🔍 ")
        nom=input("\n📝 Nombre: ").upper().strip()
        cursor=conexion.cursor()
        cursor.execute(
            "select * from calificaciones where nombre=%s",(nom,)
        )
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'nombre':<20}{'calificacion 1':<20}{'calificacion 2':<20}{'calificacion 3':<20}")
            print(F"{'-'*85}")
            for i in registros:
                print(f"{i[0]:<10}{i[1]:<20}{i[2]:<20}{i[3]:<20}{i[4]:<20}")
            num=len(registros)
            print(f"\nSon {num} Alumnos 👤")
        else:
            print("⚠️  Nombre no encontrado  ⚠️")

        

#prom grupal, cuantos alumnos son en buscar