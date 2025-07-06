'''List (Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se
hace con un indice numerico.

Nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable. PERMITE MIEBROS DUPLICADOS
'''


#funciones mas comunes en la listas
import os
os.system("cls")


paises=["Mexico","Brasil","España","Canada"]
numeros=[23,12,100,34]

#ordenar ascendentemente
print(paises)
print(numeros)
numeros.sort ()
paises.sort()
print(numeros)
print(paises)

#añadir o ingresar elementos a una lista forma 1
paises.append("Honduras")
#2
paises.insert(1,"Honduras")
print(paises)

#eliminar o borrar elemetos de una lista forma 1
paises.pop(1)
print(paises)
#2 quita solo la primera aparicion 
paises.remove("Honduras")
print(paises)



#Buscar un elemento dentro de la lista forma 1
"Brasil" in paises
resp="Brasil" in paises
print(resp)
#otra forma
if resp==True:
    print("pais encontrado")
else:
    print("no esta")

#contar espacios arreglos
long=len(paises)
print(long)


#sin funcion forma 2
paisabuscar=input("Dame el pais a buscar:")

for i in range(0,len(paises)):
    if paises[i]==paisabuscar:
        print("si encontre el pais")
        
    else:
        print("no encontre el pais")
        



#Buscar contas veces aárece un valor dentro de una lista
cont=numeros.count(12)
#2 formas
print(cont)
print(f"Este numero 12 aparece: {numeros.count(12)} veces")
numeros.append(12)
print(f"Este numero 12 aparece: {numeros.count(12)} veces")


#Identificar o conocer el indice de un valor, si hay varios solo muestra el primero
indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#valor de un indice ahora muestra otro porque se elimino antes
print(paises[2])


#RECORRER LOS VALORES DE UNA LISTA para abajo forma 1 forma que imprimer valores
for i in paises:
    print(i)
#forma 2 forma que imprime indices
for i in range(0,len(paises)):
    #solo imprime indices: print(i)
    print(f" El valor {i} es: {paises[i]}")

#unir listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)