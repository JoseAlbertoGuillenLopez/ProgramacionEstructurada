'''
Conjunto de ordenes agrupadas bajo un orden en particular como un programa mas pequeño que 
cumple una funcion especifica, la funcion se puede reutilizar con invocarla 

sintaxis:
def nombrefuncion (parametros):
    bloque de codigo
nombrefuncion(parametros)


FUNCIONES TIPO PROCEDIMEINTO:
1 funcion que no recibe parametros ni regresa valor
3 funciones que reciben parametros y no regresan valor


FUNCIONES TIPO FUNCION (las que mas se usan):
2 funcion que so recibe parametros si regresa valor
3 funciones que no reciben parametros y regresan valor
'''
#las funciones no se pueden llamar igual

#caso 1
def solidatos1():
    nom=input("Teclea tu nombre: ")
    tel=input("Teclea tu numero: ")
    print(f" funcion1: El nombre es: {nom} y el telfono es: {tel}")

#caso 3

def solidatos3(nombre,tel):
    nom=nombre
    telefono=tel
    print(f"funcion 3: El nombre es: {nom} y el telfono es: {telefono}")



#caso 2
def solidatos2():
    nom=input("Teclea tu nombre: ")
    tel=input("Teclea tu numero: ")
    return nom,tel
    #resp=f"El nombre es: {nom} y el telfono es: {tel}"


#caso 4
def solidatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom,telefono


#llamar funciones

solidatos1()

nombre=input("Nombre: ")
tel=input("telefono: ")
solidatos3(nombre,tel)


nombre2,tel2=solidatos2()
print(f"nombre: {nombre2} \n telefono {tel2}")


nombre=input("Nombre: ")
tel=input("telefono: ")
nombre,tel=solidatos4(nombre,tel)
print(f"nombre: {nombre} \n telefono: {tel}")