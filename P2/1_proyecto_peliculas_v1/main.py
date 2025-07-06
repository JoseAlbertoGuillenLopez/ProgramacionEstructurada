'''Crear un proyecto que perimita gestionar (administrar) peliculas, colocar un menu de opciones para agregar
eliminar, modificar y colsultar peliculas. 
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacener los nombres de peliculas'''
import os
import pelicula
os.system("cls")
opw=True
while opw==True:
    op=int(input("Teclea la opcion deseada para tu menu: \n 1)Agregar\n 2)Eliminar\n 3)Modificar\n 4)Consultar\n 5)Buscar\n 6)Vaciar\n 7)Salir\n \tElige una opcion:  "))
    
    match op:
        case 1:
            print("Agregar peliculas")
            pelicula.agregar()
            pelicula.esptecla()  
            pelicula.borrar()
        case 2:
            print("Elimiar peliculas")
            pelicula.eliminar()
            pelicula.esptecla()  
            pelicula.borrar()
        case 3:
            print("Modificar peliculas")
            pelicula.modificar()
            pelicula.esptecla()  
            pelicula.borrar()
        case 4:
            print("Consultar peliculas")
            pelicula.consultar()
            pelicula.esptecla()  
            pelicula.borrar()
        case 5:
            print("Buscar peliculas")
            pelicula.buscar()
            pelicula.esptecla()  
            pelicula.borrar()
        case 6:
            print("Vaciar peliculas")
            pelicula.vaciar()
            pelicula.esptecla()  
            pelicula.borrar()
        case 7:
            print("..:Terminaste de ejecutar:..")
            opw=False
        case _:
            print("..:Opcion no valida, intente de nuevo:..")
