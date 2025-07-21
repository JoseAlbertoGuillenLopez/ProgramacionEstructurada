#Proyecto 4
'''Crear un proyecto que perimita gestionar (administrar) una agenda, colocar un menu de opciones para agregar,
mostrar y buscar contactos
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar un diccionario con listas para la resolucion'''

import os 
import agenda 

def main():

    agragar_contactos={
        "JUAN":["6181234567","juan@gmail.com"],
        "RUBEN":["6181234567","ruben@gmail.com"]
    }

    opcion=True
    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menu_principal()
        match opcion:
            case "1":
                agenda.agregar_contacto(agragar_contactos)
                agenda.esperarTecla()           
            case "2":                  
                agenda.mostrar_contacto(agragar_contactos)
                agenda.esperarTecla()   
            case "3":            
                agenda.buscar_contacto(agragar_contactos)
                agenda.esperarTecla()           
            case "4":
                agenda.modificar_contacto(agragar_contactos)
                agenda.esperarTecla()             
            case "5":
                agenda.eliminar_contacto(agragar_contactos)
                agenda.esperarTecla()   
            case "6":
                opcion=False    
                agenda.borrarPantalla()
                print("\n\t 🚪.::Terminaste la ejecucion del SW::.🚪")  
            case _:           
                input("\n\t⚠️ Opción invalida vuelva a intentarlo ... por favor⚠️ ")

if __name__=="__main__":
    main()