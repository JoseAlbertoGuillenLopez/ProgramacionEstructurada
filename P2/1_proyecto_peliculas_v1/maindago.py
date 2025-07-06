import os
import peliculadago
opcion=True
while opcion:
    peliculadago.borrarPantalla()
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculadago.agregarPeliculas()
            peliculadago.esperarTecla()           
        case "2":                  
            peliculadago.eliminarPeliculas()
            peliculadago.esperarTecla()   
        case "3":            
            peliculadago.modificarPeliculas()
            peliculadago.esperarTecla()           
        case "4":            
            peliculadago.consultarPeliculas()
            peliculadago.esperarTecla()          
        case "5":
            peliculadago.buscarPeliculas()
            peliculadago.esperarTecla()
        case "6":        
            peliculadago.vaciarPeliculas()
            peliculadago.esperarTecla()
        case "7":         
            opcion=False    
            peliculadago.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:           
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")