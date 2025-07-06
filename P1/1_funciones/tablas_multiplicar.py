'''Crear un programa que calcule e imprima la tabla de multiplicar de cualquier numero

Requisitos: 
1 sin estructuras de control (ciclos,selectivas)
2 sin funciones
'''

#primero con los requisitos dados

num=int(input("dame el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num}x1={multi}")
multi=num*2
print(f"{num}x2={multi}")
multi=num*3
print(f"{num}x3={multi}")
multi=num*4
print(f"{num}x4={multi}")
multi=num*5
print(f"{num}x5={multi}")
multi=num*6
print(f"{num}x6={multi}")
multi=num*7
print(f"{num}x7={multi}")
multi=num*8
print(f"{num}x8={multi}")
multi=num*9
print(f"{num}x9={multi}")
multi=num*10
print(f"{num}x10={multi}")


#otro solo sin funciones
num=int(input("dame el numero de la tabla de multiplicar: "))
for i in range(1,11,1):
    mult=num*i
    print(f"{num}x{i}={mult}")

#sin funciones con while
i=1
num=int(input("dame el numero de la tabla de multiplicar: "))
while i<=10:
    mult=num*i
    print(f"{num}x{i}={mult}")
    i=i+1

#otro sin requistos (con funciones que regrese valor y que tenga parametros)


def tabla (num):
    num=num
    res=""
    for i in range(1,11,1):
        mult=num*i
        res+=f"{num}x{i}={mult}\n"
    return res

num=int(input("Teclea el numero de la tabla de multi"))
print(f"tabla del numero {num}")
res=tabla(num)
print(f"{res}")

def tabla (num):
    num=num
    respuesta=""
    for i in range(1,11):
        mult=num*i
        respuesta=respuesta+f"{num}x{i}={mult}\n"
    return respuesta

num=int(input("Dame el numero de tu tabla:"))
resultado=tabla(num)
print(resultado)



