'''Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en
lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido a los objetos

Tambien se conoce como arreglo asosiativo u Objeto JSON

El diccionario es una coleccion ordenada y modificable. No hay miembros duplicados (tipo de cosas, propiedades)'''
# lista de paisses paises=["Mexico","Brasil","Canada","España"]
import os
os.system("cls")

#los nombres son un objeto
#cada pais tiene caracteristicas
#no nombres iguales de dict
#nombre,capital,poblacion,idioma=atributos
#con lo que lo filleo es el valor del atributo
#pais_mexico,brasil,canada=objeto o dict


pais_mexico={"nombre":"Mexico",
        "capital":"CDMX",
        "poblacion":12000000,
        "idioma":"español",
        "estatus":True}
#"nombre":"hola" no se pueden repetir los mismos atributos !!

pais_brasil={"nombre":"Mexico",
        "capital":"Brasilia",
        "poblacion":10000000,
        "idioma":"portugues",
        "estatus":True}

pais_canada={"nombre":"Mexico",
        "capital":"ottawa",
        "poblacion":900000,
        "idioma":["ingles","frences"],
        "estatus":False}
#los objetos generalmente los declaro en singular
alumno1={"nombre":"Daniel",
         "apellido_paterno":"Hernandez",
         "apellido_materno":"Gonzalez",
         "carrera":"TI",
         "matricula":"123456",
         "area":"software multiplataforma",
         "modalidasd":"bilingue",
         "semestre":"2"}

#mostrar el contendio de un diccionario
print(alumno1)
for i in alumno1:
    print(f"{i} : {alumno1[i]}")

alumno1["telefono"]="618123456"
for i in alumno1:
    print(f"{i} : {alumno1[i]}")


#para mas caracteristicas una lista

