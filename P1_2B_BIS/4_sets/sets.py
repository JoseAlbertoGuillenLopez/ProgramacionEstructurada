'''Set es una coleccion desordenada, /inmutable/=si cambia en realidad y no indexada=no indexa listas respecto a posiciones. 
No duplica miembros y no hay posiciones, lugares aleatorios'''
import os
os.system("cls")

personas={"ramiro","choche","lupe"}
print(personas)
personas.add("choche")
print(personas)
personas.remove("choche")
print(personas)
personas.clear()
print(personas)

varios={3.12,3,True,"hola"}
print(varios)


#ejemplo crear un programa que solicite los emails de los alumnos de la utd ,
#  almacenar en una lista y posterirmente mostar en pantalla los mails sin ducplicados

op="si"
emails=[]
while op=="si":
    emails.append(input("Dame el correo: "))

    op=input("Deseas solicitar otro mail: si/no: ").lower()

print(emails)
new=set(emails)
print(new)
#sin duplicados

        
