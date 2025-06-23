''' datos=[
    ["Ruben",1.0,2.0,3.0],
    ["Juan",7.0,8.0,9.0]
    ]'''

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    print(" 🕒 Oprima cualquier tecla para continuar 🕒 ...")
    input()  

def menu_principal():
    print("\n\t\t.:: Sistema de Gestión de calificaciones::.\n\t\t n1.- Agregar 📝 \n\t\t n2.- Mostrar 🔍 \n\t\t n3.- Calcular promedios 📝 \n\t\t n4.- SALIR 🚪 ")
    opcion=input("\n\t\t Elige una opción (1-4): ").upper()
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("Agregar calificaciones")
    nombre=input("Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"Calificacion {i}:"))
                if cal>=0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("Ingresa un numero valido ")
            except ValueError:
                print("Ingresa un valor numerico")
    lista.append([nombre]+calificaciones)
    print("Accion realizada con exito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar calificaciones calificaciones")
    if len(lista)>0:
        print("Nombre--Calf.1--Calf.2--Calf.3")
        for fila in lista:
            print(F"{fila[0]}--{fila[1]}--{fila[2]}--{fila[3]}")

        '''for i in range(0,len(fila)):
            for j in range(0,len(fila)):'''
        
    else:
        print("No hay calificaciones registradas en el sistema")
            
def calcular_promedios(lista):
    print("")


