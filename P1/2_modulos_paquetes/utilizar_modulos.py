#import * importa todos
import modulos

#primer forma de utilzar los modulos

modulos.borrarPantalla()
print(modulos.saludar("Jose Lopez"))



#segunda forma de modulos
from modulos import saludar,borrarPantalla
#borrarPantalla()
print(saludar("Juan lopez"))




nombre=input("ingresa el nombre del contacto: ")
tel=input("ingresa el telefono: ")
nom,tel=modulos.solidatos4(nombre,tel)
print(f"\tEl nombre es: {nom} \n\tel telefono es: {tel}")


