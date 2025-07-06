'''Crear un proyecto que perimita gestionar (administrar) peliculas, colocar un menu de opciones para agregar
eliminar, modificar y colsultar peliculas. 
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar diccionarios para almacener los siguientes atributos: nombre categoria clasificacion genero idioma'''

import os
import peliculadago
opcion=True
while opcion:
    peliculadago.borrarPantalla()
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear 📝 \n\t\t 2.- Borrar 📛 \n\t\t 3.- Mostrar 🔍 \n\t\t 4.- Agregar caracteristicas 📝 \n\t\t 5.- Modificar caracteristica 🔄 \n\t\t 6.- Eliminar cacracteristica 📛 \n\t\t 7.- SALIR 🚪 ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculadago.crearPeliculas()
            peliculadago.esperarTecla()           
        case "2":                  
            peliculadago.borrarPeliculas()
            peliculadago.esperarTecla()   
        case "3":            
            peliculadago.mostrarPeliculas()
            peliculadago.esperarTecla()           
        case "4":            
            peliculadago.agregarCaracteristicaPeliculas()
            peliculadago.esperarTecla()          
        case "5":
            peliculadago.modificarCaracteristicaPeliculas()
            peliculadago.esperarTecla()
        case "6":        
            peliculadago.borrarCaracteristicaPeliculas()
            peliculadago.esperarTecla()
        case "7":         
            opcion=False    
            peliculadago.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:           
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")