import funciones 
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado==True:
                print(f"\n\t{nombre} {apellidos} Se registro correctamente con el email: {email}")
            else:
                print(f"\n\t ...Por favor intentelo de nuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()

        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            registro=usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print("\n\t Email o contraseña incorrectas, vuelva a intentarlo")
                funciones.esperarTecla()
        
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla()  

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            resultado=nota.crear(usuario_id,titulo,descripcion)
            if resultado==True:
                print(f"\n\tLa nota {titulo} se registro correctamente")
            else:
                print(f"\n\t ...Por favor intentelo de nuevo, no fue posible registrar la nota")
            funciones.esperarTecla()    



        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo 
            resultado=nota.mostrar(usuario_id)
            if resultado:
                print(F"\n\t Mostrar Notas\n")
                print(f"{'ID':<10}{'TITULO':<15}{'DESCRIPCION':<20}{'FECHA'}")
                print(f"{'-'*60}")
                for i in resultado:
                    print(f"{i[0]:<10}{i[2]:<15}{i[3]:<20}{i[4]}")
            else:
                print(f"\n\t ...No exiten notas para mostrarte")
            funciones.esperarTecla()



        elif opcion=='3' or opcion=="CAMBIAR":
            funciones.borrarPantalla() 
            resultado=nota.mostrar(usuario_id)
            if resultado:
                print(F"\n\t Mostrar Notas\n")
                print(f"{'ID':<10}{'TITULO':<15}{'DESCRIPCION':<20}{'FECHA'}")
                print(f"{'-'*60}")
                for i in resultado:
                    print(f"{i[0]:<10}{i[2]:<15}{i[3]:<20}{i[4]}")

                print(f"\n \t .:: {nombre} {apellidos}, vamos a cambiar un Nota ::. \n")
                id=input("\t \t ID de la nota a actualizar: ")
                titulo=input("\t Nuevo título: ")
                descripcion=input("\t Nueva descripción: ")

                check=nota.check(id)
                if check!=None:
                    op=input("¿De verdad quieres cambiar la nota? (si/no): ").lower().strip()
                    if op=="si":
                        resultado=nota.cambiar(id, titulo,descripcion)
                        if resultado:
                            print(f"\n\tLa nota {titulo} se actualizó correctamente")
                else:
                    input(f"\n\tNo existe una nota con ese ID")
                funciones.esperarTecla()
            else:
                print(f"\n\t ...No exiten notas para mostrarte")
                funciones.esperarTecla()


            
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            resultado=nota.mostrar(usuario_id)
            if resultado:
                print(F"\n\t Mostrar Notas\n")
                print(f"{'ID':<10}{'TITULO':<15}{'DESCRIPCION':<20}{'FECHA'}")
                print(f"{'-'*60}")
                for i in resultado:
                    print(f"{i[0]:<10}{i[2]:<15}{i[3]:<20}{i[4]}")

                print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                id=input("\t \t ID de la nota a eliminar: ")
                #Agregar codigo
                check=nota.check(id)
                if check!=None:
                    op=input("¿De verdad quieres cambiar la nota? (si/no): ").lower().strip()
                    if op=="si":
                        resultado=nota.eliminar(id)
                        print(f"\n\tLa nota {id} se elimino correctamente")
                else:
                    input(f"\n\tNo existe una nota con ese ID")
                funciones.esperarTecla()
            else:
                print(f"\n\t ...No exiten notas para mostrarte")
                funciones.esperarTecla()



#mostrar si hay reg o no, si hay que muestre, luego deseas cambiar o eliminar, luego valide id


        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


