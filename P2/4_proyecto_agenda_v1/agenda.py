def borrarPantalla():
    import os 
    os.system("cls")

def esperarTecla():
    print(" 🕒 Oprima cualquier tecla para continuar 🕒 ...")
    input()  

def menu_principal():
    print("\n\t📝...::: Sistema de Gestión de Agenda de Contactos:::...📝\n\n\t\t 1️⃣  Agregar contacto \n\t\t 2️⃣  Mostrar todos los contactos \n\t\t 3️⃣  Buscar contacto por nombre \n\t\t 4️⃣  Modificar contacto \n\t\t 5️⃣  Eliminar contacto   \n\t\t 6️⃣  SALIR  ")
    opcion=input("\n\t\t  👉 Elige una opción (1-4): ").upper()
    return opcion




def agregar_contacto(agenda):
    borrarPantalla()
    print("\t📝.::Agregar contactos::.📝\n")
    nombre=input("👤 Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t⚠️ El contacto ya existe ⚠️")
    else:
        tel=input("📞 Telefono: ").strip()
        email=input("📧 E-mail: ").lower().strip()
        #agregar el atributo nombre al dict con los valores de tel y email en listas
        agenda[nombre]=[tel,email]
        print("\n\t\t ✅ Accion realizada con exito ✅")
        




def mostrar_contacto(agenda):
    borrarPantalla()
    print("\t🔍.::Mostrar Contactos::.🔍\n")
    if not agenda:
        print(" ⚠️ No exiten contactos ⚠️")
    else:
        for nombre,datos in agenda.items():
            print(f"\t{'👤 Nombre:'+nombre}\n\t{'📞 Telefono:'+datos[0]}\n\t{'📧 Telefono:'+datos[1]}\n")
            

def buscar_contacto(agenda):
    borrarPantalla()
    print("\t🔍 .:: Buscar Contacto ::. 🔍\n")
    if not agenda:
        print("⚠️ No existen contactos en la agenda \n")
    else:
        nombre=input("📝 Teclea el nombre del contacto a buscar: ").upper().strip()

        if nombre in agenda:
            print(f"\n📌 Nombre: {nombre}")
            print(f"📞 Teléfono: {agenda[nombre][0]}")
            print(f"📧 Correo: {agenda[nombre][1]}\n")
        else:
            print("\n⚠️ Nombre no encontrado ⚠️ \n")



def modificar_contacto(agenda):
    borrarPantalla()
    print("\t🔄 .:: Modificar Contacto ::. 🔄\n")
    if not agenda:
        print("⚠️ No existen contactos en la agenda \n")
    else:
        nombre=input("📝 Teclea el nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            res=input("🔄 ¿Quieres cambiar el número? (s/n): ").lower()
            if res=="s":
                tel=input("📞 Teclea el nuevo número: ")
                agenda[nombre][0]=tel
                print("✅ Número actualizado ✅\n")

            res2=input("🔄 ¿Quieres cambiar el correo? (s/n): ").lower()
            if res2=="s":
                email=input("📧 Teclea el nuevo correo: ")
                agenda[nombre][1]=email
                print("✅ Correo actualizado ✅\n")
        else:
            print("\n⚠️ Nombre no encontrado ⚠️\n")


def eliminar_contacto(agenda):
    borrarPantalla()
    print("\t📛 .:: Eliminar Contacto ::. 📛\n")
    if not agenda:
        print("⚠️ No existen contactos en la agenda ⚠️\n")
    else:
        nombre=input("📝 Teclea el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            res=input("📛 De verdad quieres borrarlo (s/n): ").lower()
            if res=="s":
                del agenda[nombre]
                print("✅ Correo eliminado ✅\n")
        else:
            print("\n⚠️ Nombre no encontrado ⚠️\n")
