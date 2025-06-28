#nombre,tel,nprendas,total,fecha,metodopago

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t\t🔃 Oprima cualquier tecla para continuar ...")

def menu_principlal():
    print("\n\t\t..::: Sistema de Gestión de Ropa :::..." \
    "\n\n\t\t\t1️  Agregar Registro " \
    "\n\t\t\t2️⃣​  Eliminar Registro " \
    "\n\t\t\t3️⃣​  Modificar Registro " \
    "\n\t\t\t4️⃣​  Consultar Registro " \
    "\n\t\t\t5️⃣​  Mostrar Registros" \
    "\n\t\t\t6️⃣​  SALIR ")
    opcion=input("\n\t\t\t👉 ​Elige una opción (1-6): ").upper()
    return opcion

def agregar_registro(lista):
    try:
        estado=True
        borrarPantalla()
        print("\n\t\t\t.::📑​ Agregar Registro 📑​::.")
        nombre=input("\n\t\t\t.::🧑​ Nombre del Cliente : ").upper().strip()
        while estado:
            try:
                tel=int(input("\t\t\t📞 Telefono: "))
                if len(str(tel))==10:
                    estado=False
                else:
                    print("\n\t\t\t.::🚫 Ingresa un numero de telefono valido 🚫::.")
            except ValueError:
                print("\n\t\t\t.::🚫 Ingresa un valor numerico 🚫::.")
        estado=True
        while estado:
            try:
                nprendas=int(input("\t\t\t👕 Numero de Prendas: "))
                if nprendas>0:
                    estado=False
                else:
                    print("\n\t\t\t.::🚫 Ingresa un numero de prendas valido 🚫::.")
            except ValueError:
                print("\n\t\t\t.::🚫 Ingresa un valor numerico 🚫::.")
        estado=True
        while estado:
            try:
                total=float(input("\t\t\t💰 Total a Pagar: "))
                if total>=0:
                    estado =False
                else:
                    print("\n\t\t\t.::🚫 Ingresa un valor positivo para el total 🚫::.")
            except ValueError:
                print("\n\t\t\t.::🚫 Ingresa un valor numerico 🚫::.")
        estado=True
        fecha=input("\t\t\t📅 Fecha (DD/MM/AAAA): ")
        while estado:
            metodopago=input("\t\t\t💳 Metodo de Pago: 1)Efectivo 2)Transferencia: ").strip()
            if metodopago=="1":
                metodopago="Efectivo"
                estado=False
            elif metodopago=="2":
                metodopago="Transferencia"
                estado=False
            else:
                print("\n\t\t\t.::🚫 Ingresa una opcion valida 🚫::.")
        lista.append([nombre,tel,nprendas,total,fecha,metodopago])
        print("\n\t\t\t.:: ✔️  Registro agregado con exito  ✔️ ::.")
    except ValueError:
        print("\n\t\t\t.::🚫 Ingresa un valor valido 🚫::.")

def eliminar_registro(lista):
    borrarPantalla()
    print("\n\t\t\t.::🗑️​ Eliminar Registro 🗑️​::.")
    if len(lista)>0:
        nombre=input("\n\t\t\t.::🧑​ Nombre del Cliente a eliminar: ").upper().strip()
        encontrado=False
        cont=-1
        for fila in lista:
            cont=cont+1
            if fila[0]==nombre:
                resp=input("De verdad quieres borrarlo (Si/No): ").lower().strip()
                if resp=="si":
                    lista.pop(cont)
                    encontrado=True
                    print(f"\n\t\t\t.:: ✔️  Registro de {nombre} eliminado con exito  ✔️ ::.")
                else:
                    print("\n\t\t\t.:: ❌  Operacion cancelada ❌ ::.")
        if not encontrado:
            print(f"\n\t\t\t.::🚫 No se encontró un registro con el nombre {nombre} 🚫::.")
    else:
        print("\t\t\t.::🚫 No existen registros en el sistema 🚫::.")

def modificar_registro(lista):
    borrarPantalla()
    print("\n\t\t\t.::✏️​ Modificar Registro ✏️​::.")
    if len(lista) > 0:
        nombre=input("\n\t\t\t.::🧑​ Nombre del Cliente a modificar: ").upper().strip()
        encontrado=False
        for fila in lista:
            if fila[0] == nombre:
                encontrado=True
                print(f"\n\t\t\t.:: 📝 Datos actuales de {nombre} ::.")
                print(f"\t\t\t{'Nombre':<15}{'Telefono':<15}{'N. Prendas':<12}{'Total':<10}{'Fecha':<12}{'Metodo Pago':<15}")
                print(f"\t\t\t{'-' * 80}")
                print(f"\t\t\t{fila[0]:<15}{fila[1]:<15}{fila[2]:<12}{fila[3]:<10}{fila[4]:<12}{fila[5]:<15}")
                print(f"\t\t\t{'-' * 80}")
                
                nuevo_nombre=input("\t\t\tNuevo Nombre (dejar en blanco para no cambiar): ").upper().strip()
                if nuevo_nombre!="":
                    fila[0]=nuevo_nombre
                
                nuevo_tel=input("\t\t\tNuevo Telefono (dejar en blanco para no cambiar): ").strip()
                if nuevo_tel!="":
                    fila[1]=nuevo_tel
                
                try:
                    nuevo_nprendas=input("\t\t\tNuevo Numero de Prendas (dejar en blanco para no cambiar): ").strip()
                    if nuevo_nprendas!= "":
                        fila[2]=int(nuevo_nprendas)
                except ValueError:
                    print("\n\t\t\t.::🚫 Ingresa un valor numerico valido 🚫::.")
                
                try:
                    nuevo_total=input("\t\t\tNuevo Total a Pagar (dejar en blanco para no cambiar): ").strip()
                    if nuevo_total!="":
                        fila[3]=float(nuevo_total)
                except ValueError:
                    print("\n\t\t\t.::🚫 Ingresa un valor numerico valido 🚫::.")
                
                nueva_fecha=input("\t\t\tNueva Fecha (DD/MM/AAAA, dejar en blanco para no cambiar): ").strip()
                if nueva_fecha!="":
                    fila[4]= nueva_fecha
                estado=True
                while estado:
                    nuevo_metodopago=input("\t\t\tNuevo Metodo de Pago (1)Efectivo 2)Transferencia (dejar en blanco para no cambiar): ").strip()
                    if nuevo_metodopago=="1":
                        fila[5]="Efectivo"
                        estado=False
                    elif nuevo_metodopago=="2":
                        fila[5]="Transferencia"
                        estado=False
                    elif nuevo_metodopago=="":
                        estado=False
                    else:
                        print("\n\t\t\t.::🚫 Ingresa una opcion valida 🚫::.")
                print(f"\n\t\t\t.:: ✔️  Registro de {nombre} modificado con exito  ✔️ ::.")
        if not encontrado:
            print(f"\n\t\t\t.::🚫 No se encontró un registro con el nombre {nombre} 🚫::.`")
    else:
        print("\t\t\t.::🚫 No existen registros en el sistema 🚫::.")


def consultar_registro(lista):
    borrarPantalla()
    print("\n\t\t\t\t🔍.::Buscar Registro::.🔍")
    if len(lista) > 0:
        nom=input("\n\t📝 Nombre: ").upper().strip()
        encont=False
        for fila in lista:
            if nom==fila[0]:
                cont=0
                print(f"\n\t\t{'Nombre':<15}{'Telefono':<15}{'N. Prendas':<12}{'Total':<10}{'Fecha':<12}{'Metodo Pago':<15}")
                print(f"\t\t{'-'*80}")
                print(f"\t\t{fila[0]:<15}{fila[1]:<15}{fila[2]:<12}{fila[3]:<10}{fila[4]:<12}{fila[5]:<15}")
                print(f"\t\t{'-'*80}")
                cont=cont+1
                encont=True
                print(f"\t\t\t👤 Son {cont} registro(s)")
        if encont==True:
            print("\t\t\t.:: ✔️ Registro encontrado ✔️ ::.")
        if encont==False:
            print("\t\t\t ⚠️  No está este registro  ⚠️ ")
    else:
        print("\t\t\t.::🚫 No existen registros en el sistema 🚫::.")

def mostrar_registro(lista):
    borrarPantalla()
    print("\n\t\t\t\t.::🔎​ Mostrar Registros 🔎​::\n")
    if len(lista)>0:
        print(f"\t\t{'Nombre':<15}{'Telefono':<15}{'N. Prendas':<12}{'Total':<10}{'Fecha':<12}{'Metodo Pago':<15}")
        print(f"\t\t{'-' * 80}")
        for fila in lista:
            print(f"\t\t{fila[0]:<15}{fila[1]:<15}{fila[2]:<12}{fila[3]:<10}{fila[4]:<12}{fila[5]:<15}")
            print(f"\t\t{'-' * 80}")
        cuantos=len(lista)
        print(f"\t\t\tSon {cuantos} registro(s)")
        print("\t\t\t.:: ✔️ Registros mostrados con exito ✔️ ::.")
    else:
        print("\t\t\t.::🚫No existen registros en el sistema🚫::.")

