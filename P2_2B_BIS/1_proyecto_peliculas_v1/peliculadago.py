peliculas=["JUAN","JUANO","DICK","JUAN"]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print("\n\t.:: Alta de Peliculas ::. ")
  peliculas.append(input("Ingresa el nombre: ").upper().strip())
  input("\n\t :::Operacion con exito:::")

def consultarPeliculas():
  borrarPantalla()
  print("\n\t.:: Consultar Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
      print(f"{i+1}:{peliculas[i]}")
  else:
    print(f"\t No hay peliculas en el sistema")

def vaciarPeliculas():
  borrarPantalla()
  print("\n\t .::Borrar o quitar todas las peliculas::.")
  resp=input("¿Deseas borrar TODAS las peliculas del sistema? (Si/No)").lower()
  if resp=="si":
    peliculas.clear()
    input("\n\t :::Operacion con exito:::")

def borr():
  for i in range(0,len(peliculas)):
    peliculas=peliculas[i]=""

def buscarPeliculas():
  borrarPantalla()
  print("\n\t .::Buscar peliculas::.")
  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
  encontro=0
  if not(pelicula_buscar in peliculas):
    print("\n\t\t No se encuentra la pelicula a buscar")
  else:
    for i in range(0,len(peliculas)):
      if pelicula_buscar==peliculas[i]:
        print(f"la pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
        encontro=encontro+1
    if encontro>0:
      print(f"tenemos {encontro} peliculas ")
      input("\n\t :::Operacion con exito:::")

def eliminarPeliculas():
  borrarPantalla()
  peliborr=input("Teclea la pelicula a borrar: ").upper()
  if not(peliborr in peliculas):
    print("\n\t No enocntre la pelicula")
  else:
    resp="si"
    encontro=0
    while peliborr in peliculas and resp=="si":
      resp=input("Deseas borrar esta pelicula del sistema (si/no)").lower()
      if resp=="si":
        posi=peliculas.index(peliborr)
        print(f"La pelicula {peliborr} se borro y estaba en la posicion {posi+1}")
        peliculas.remove(peliborr)
        encontro=encontro+1
        input("\n\t :::Operacion con exito:::")
    print(f"Se borro {encontro} veces la pelicula con este nombre")

'''def eliminarPeliculas():
  borrarPantalla()
  print("\n\t::.Borrar Película.::")
  borr=input("Teclea la pelicula a borrar: ").upper()
  if borr in peliculas:
    i=0
    cont=0
    while i<len(peliculas):
      if peliculas[i]==borr:
        print("pelicula encontrada en la posicion",i)
        op=input("desea borar la peli: s/n").upper()
        if op=="S":
          peliculas.pop(i)
          input("exito pelicula borrada")
          cont=cont+1
          
      i=i+1
    print(f"la pelicula{borr} se borro {cont} veces")
      
  else:
    print("La pelicula no existe")'''





def modificarPeliculas():
  borrarPantalla()
  print("\n\t .::Modificar las peliculas::.")
  op=input("borrar por indice o nombre (i-n)").lower()
  if op=="n":
    pelimod=input("Teclea la pelicula a modificar: ").upper()
    if not(pelimod in peliculas):
      print("\n\t No enocntre la pelicula")
    else:
        resp="si"
        encontro=0
        while pelimod in peliculas and resp=="si":
          resp=input("Deseas cambiar esta pelicula esta pelicula del sistema (si/no)").lower()
          if resp=="si":
            posi=peliculas.index(pelimod)
            nuev=input("ingrese el nuevo cambio").upper()
            print(f"La pelicula {pelimod} se cambio y estaba en la posicion {posi+1}")
            peliculas.pop(posi)
            peliculas.insert(posi,nuev)
            #peliculas[posi]=pelimod
            encontro=encontro+1
            input("\n\t :::Operacion con exito:::")
        print(f"Se cambio {encontro} veces la pelicula con este nombre")
  else:
    for i in range(0,len(peliculas)):
      print(f"{i+1}={peliculas[i]}")
    idi=int(input("dame el indice: "))
    nuev=input("ingrese el nuevo cambio").upper()
    peliculas[idi-1]=nuev

'''def modificarPeliculas():
  borrarPantalla()
  print("\n\t::.modificar Película.::")
  opc=input("nombre o inidce: n-i").lower
  if opc=="n":
    borr=input("Teclea la pelicula a modificar: ").upper()
    if borr in peliculas:
      i=0
      cont=0
      while i<len(peliculas):
        if peliculas[i]==borr:
          print("pelicula encontrada en la posicion",i)
          op=input("desea cambiar la peli: s/n").upper()
          if op=="S":
            add=input("ingresa el nuevo cambio: ")
            peliculas.pop(i)
            peliculas.insert(i,add)
            cont=cont+1
            
        i=i+1
      print(f"la pelicula{borr} se cambio {cont} veces")
        
    else:
      print("La pelicula no existe")
  else:
    indi=int(input("teclea el inidce: "))
    cam=input("teclea el cambio: ")
    peliculas[indi-1]=cam
    print("exito")
'''