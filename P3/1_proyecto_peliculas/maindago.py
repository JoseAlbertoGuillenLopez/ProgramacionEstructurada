'''Crear un proyecto que perimita gestionar (administrar) peliculas, colocar un menu de opciones para agregar
eliminar, modificar y colsultar peliculas. 
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar diccionarios para almacener los siguientes atributos: nombre categoria clasificacion genero idioma
3.- Utilizar e implementar una base de datos para gestionar las peliculas'''

import os
import peliculadago
opcion=True
while opcion:
    peliculadago.borrarPantalla()
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1️⃣  Crear 📝 \n\t\t 2️⃣  Borrar 📛 \n\t\t 3️⃣  Mostrar 🔍 \n\t\t 4️⃣  Modificar  📝 \n\t\t 5️⃣  Buscar 🔍\n\t\t 6️⃣  Salir 🚪 ")
    opcion=input("\n\t\t  👉 Elige una opción: ").upper()

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
            peliculadago.modificarCaracteristicaPeliculas()
            peliculadago.esperarTecla()
        case "5":           
            peliculadago.buscarPeliculas()
            peliculadago.esperarTecla()             
        case "6":         
            opcion=False    
            peliculadago.borrarPantalla()
            print("\n\t🚪 Terminaste la ejecucion del SW 🚪")
        case _:           
            input("\n\tOpción invalida vuelva a intentarlo ... por favor") 