import funciones

def main():
    datos = [
        ["JUAN","6181234567",50,6699.00,"25/05/06","Efectivo"],
        ["FERNANDO","6181234567",10,6900.00,"20/10/08","Transferencia"]
    ]
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_principlal()
        match opcion:
            case "1":
                funciones.agregar_registro(datos)
                funciones.esperarTecla()
            case "2":
                funciones.eliminar_registro(datos)
                funciones.esperarTecla() 
            case "3":
                funciones.modificar_registro(datos)
                funciones.esperarTecla()    
            case "4":
                funciones.consultar_registro(datos)
                funciones.esperarTecla()    
            case "5":
                funciones.mostrar_registro(datos)
                funciones.esperarTecla()    
            case "6":
                opcion=False    
                funciones.borrarPantalla()
                print("\n\t\t 🥺​ Terminaste la ejecucion del SW 🥺​ ")
            case _: 
                input("\n\t\t 🚫 Opción invalida vuelva a intentarlo 🚫")

if __name__=="__main__":
    main()
    