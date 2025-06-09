#crear una lista de numeros e imprimir el contenido forma 1
import os
num=[1,2,3,4,5]
print(num)
#forma 2
for i in num:
    print(i)

for i in range(0,len(num)):
    print("indice:",i,"valor",num[i])

input("tecla cualquier tecla para continuar")

#crear lista de pabalras y posteriormente buscar la coincidencia de una palabra
os.system("cls")
palab=["rojo","rojo","cafe","azul","negro"] 
palab2=["rojo","rojo","cafe","azul","negro"] 
palab[0]="rojo"
palab[1]="cafe"


#forma 1 
palabraabus=input("Teclea la palabra a buscar:")
res=palabraabus in palab


if res==True:
    print("palabra encontrada")
    veces=palab.count(palabraabus)
    print("se encontro",veces,"veces")
              
else:
    print("palabra no encontrada")
    

        

#forma 2 
cont=0
posi=""
encont=False
bus=input("Teclea la palabra a buscar:")
for i in range(0,len(palab2)):
    if palab2[i]==bus:
        cont+=1
        posi+=f"{i}\t"
        encont=True

if encont:
        print(f"si encontre la palabra {cont} veces en las posciones {posi}")
        
else:
    print("no encontre la palabra")
    
        
# forma 3
encont=False
palabraabus=input("Teclea la palabra a buscar:")
for i in palab:
    if i==palabraabus:
        encont=True

if encont==True:
        print("si encontre la palabra")
        
else:
    print("no encontre la palabra")
    

#añadir elementos a una lista
nume=[]
opc=True

while opc==True:
    add=float(input("Teclea el numero entero o decimal: "))
    nume.append(add)
    res=input("deseas volver a agregar si/no: ").lower()
    if res=="si":
         opc=True
    else:
         opc=False

print(nume)


#crear una lista multidimencional que sea una agenda 3 registros con 2 columnas
agenda=[
     ["carlos","6181123"],
     ["alberto","61826342"],
     ["martin","619363282"],
     ]
#forma 1
print(agenda)
#forma 2
for i in agenda:
     print(i)
#forma 3
for reng in range(0,3):
     for colu in range(0,2):
          print(agenda[reng][colu])
#otra forma por lineas
cadena=""
for reng in range(0,3):
     for colu in range(0,2):
          cadena=cadena+f"{agenda[reng][colu]}\t"
     cadena=cadena+"\n"
print(cadena)

