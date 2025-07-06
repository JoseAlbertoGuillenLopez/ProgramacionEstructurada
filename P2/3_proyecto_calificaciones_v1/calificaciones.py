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

def agregar_calificaciones(lista):
    borrarPantalla()
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
    print("\t✅ Accion realizada con exito ✅ ")


def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\t🔍.::Mostrar calificaciones calificaciones::.🔍")
    print("")
    if len(lista)>0:
        #print("Nombre\t\tCalf.1\tCalf.2\tCalf.3")
        print(f"{'👤 Nombre':<12}{'Calf.1':<10}{'Calf.2':<10}{'Calf.3':<10}")
        print(f"{'-'*42}")
        for fila in lista:
            print(F"{fila[0]:<14}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*42}")
        cuantos=len(lista)
        print(f"Son {cuantos} Alumnos 👤")

        #otra forma de imprimir
        '''for i in range(0, len(lista)):
            for j in range(0, len(lista[i])):
                print(lista[i][j])'''
        
    else:
        print("⚠️ No hay calificaciones registradas en el sistema ⚠️")

            
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

    borrarPantalla()
    print("\t📊.::PROMEDIOS::.📊")
    print("")
    if len(lista)>0:
        print(f"{'👤 Alumno':<15}{'📊 Promedio':<10}")
        print(f"{'-'*25}")
        promedio_grup=0
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grup=promedio_grup+promedio
        print(f"{'-'*25}")
        promedio_grup=promedio_grup/len(lista)
        print(f"\t 📊 El promedio grupal es: {promedio_grup}")
    else:
        print("⚠️ No hay calificaciones en el sistema ⚠️")




def buscarAlumno(lista):
    borrarPantalla()
    print("\t🔍.::Buscar Alumno::.🔍 ")
    nom=input("\n📝 Nombre:").upper().strip()
    print("")
    encont=False
    for i in lista:
        if nom==i[0]:
            cont=0
            print(f"{'👤 Nombre':<12}{'Calf.1':<10}{'Calf.2':<10}{'Calf.3':<10}")
            print(f"{'-'*39}")
            print(f"{i[0]:<14}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
            print(f"{'-'*39}")
            cont=cont+1
            encont=True
            print(f"\t👤 Son {cont} alumnos")
            break  
    if not encont:
        print(" ⚠️  No está este registro  ⚠️ ")

            




