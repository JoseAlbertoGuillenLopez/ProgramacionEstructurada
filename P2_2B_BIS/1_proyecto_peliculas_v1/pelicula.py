import os
os.system("cls")
peliculas=["pel1","pel2","pel3","pel1"]

def borrar():
    os.system("cls")

def esptecla():
    input("Teclea algo para continuar: ")

def agregar():
    opag="si"
    while opag=="si":
        agp=input("Agrega el nombre de la pelicula: ")
        peliculas.append(agp)
        opag=input("deseas agregar otra pelicula (si/no): ").lower()
    for i in peliculas:
        print(i)

def eliminar():
    oppel="si"
    while oppel=="si":
        agp=input("Escribe el nombre de la pelicula a eliminar: ")
        peliculas.remove(agp)
        oppel=input("deseas eliminar otra pelicula (si/no): ").lower()
    for i in peliculas:
        print(i)

def modificar():
    opmod="si"
    while opmod=="si":
        ind=int(input("Escribe el indice de la pelicula a modificar: "))
        mod=input("Escribe el nuevo nombre de la pelicula a modificar: ")
        peliculas.pop(ind)
        peliculas.insert(ind,mod)
        opmod=input("deseas modificar otra pelicula (si/no): ").lower()
    for i in peliculas:
        print (i)
        
def consultar():
    opcon="si"
    while opcon=="si":
        for i in peliculas:
            print (i)
        opcon=input("deseas consultar otra pelicula (si/no): ").lower()

def buscar():
    opbus="si"
    while opbus=="si":
        nom=input("Teclea el nombre de la pelicula para verificar si esta: ")
        cont=0
        res=""
        op=False
        for i in range(0,len(peliculas)):
            if peliculas[i]==nom:
                cont=cont+1
                res=res+f"{i}\t"
                op=True
            
        if op==True:
            print(f"Encontre la pelicula : {nom} {cont} veces en las posciciones {res}")
        else:
            print("No encontre la pelicula")

        opbus=input("deseas buscar otra pelicula (si/no): ").lower()

        '''cons= nom in peliculas
        if cons==True:
            print("pelicula encontrada")
        else:
            print("no esta")
        '''

def vaciar():
    opva="si"
    while opva=="si":
        peliculas.clear
        for i in peliculas:
            print (i)
        opva=input("deseas vaciar otra pelicula (si/no): ").lower()

