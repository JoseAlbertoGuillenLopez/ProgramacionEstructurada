#Proyecto 3
'''Crear un proyecto que perimita gestionar (administrar) calificaciones, colocar un menu de opciones para agregar,
mostrar, calcular promedio de las calificaciones de un estudiante.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar lista (bidimencional) para almacener el nombre del alumno asi como sus 3 calificaciones'''

import os
import calificaciones

def main():
    #import os
    #import calificaciones
    
    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()           
            case "2":                  
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()   
            case "3":            
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()           
            case "4":         
                opcion=False    
                calificaciones.borrarPantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case _:           
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__=="__main__":
    main()