#diccionario u objeto para almacenar los atributos(nombre,cacarteristica,clasificacion,genero,idioma)
#se ponen en singular



'''peliculas={
  "nombre":"",
  "categoria":"",
  "clasifiacion":"",
  "genero":"",
  "idioma":""
}'''

peliculas={
  "nombre":"TOY",
  "categoria":"INFA",
  "clasifiacion":"NIN",
  "genero":"ANIMA",
  "idioma":"ESP"
}

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print(" 🕒 Oprima cualquier tecla para continuar 🕒 ...")
  input()  

def crearPeliculas():
  borrarPantalla()
  print("\n\t.:: 📝 Alta de Peliculas 📝 ::.\n ")
  peliculas.update({"nombre":input("📝 Ingresa el nombre: ").upper().strip()})
  peliculas.update({"categoria":input("📝 Ingresa la categoria: ").upper().strip()})
  peliculas.update({"clasifiacion":input("📝 Ingresa la clasificacion: ").upper().strip()})
  peliculas.update({"genero":input("📝 Ingresa el genero: ").upper().strip()})
  peliculas.update({"idioma":input("📝 Ingresa el idioma: ").upper().strip()})
  print("\n\t ::: ✅ Operacion con exito ✅ :::")

def mostrarPeliculas():
  borrarPantalla()
  print("\n\t.:: 🔍 Mostrar o consultar la pelicula 🔍 ::.\n ")
  if len(peliculas)>0:
    for i in peliculas:
      print(f"\t {i} : {peliculas[i]} ")
  else:
    print("\t .:: ⚠️ No hay peliculas en el sistema ⚠️::.")

def borrarPeliculas():
  borrarPantalla()
  print("\n\t.:: 📛 Borrar o quitar pelicula 📛 ::.\n ")
  resp=input("⚠️ Deseas borrar todas las peliculas del sistema? (S/N) ⚠️ :").lower()
  if resp=="s":
    peliculas.clear()
    print(".:: ✅ Operacion realizada con exito ✅ ::.")


def agregarCaracteristicaPeliculas():
  op=True
  while op:
    borrarPantalla()
    print("\n\t.:: 📝 Agregar caracteristicas a pelicula 📝  ::.\n ")
    atributo=input(" 📝 Ingresa la nueva caracteristica de la pelicula : ").lower().strip()
    valor=input("📝 Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    #2 formas para hacerlo
    #peliculas.update({atributo:valor})
    peliculas[atributo]=valor
    print(".:: ✅ Operacion realizada con exito ✅ ::.")
    op=input(" 🔄  Otra desea agragar otro s/n 🔄 :").lower()
    if op!="s":
      op=False

'''def modificarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: modificar caracteristicas a pelicula 📝  ::.\n ")
  for i in peliculas:
      print(f"\t {i} : {peliculas[i]} ")
  busatributo=input("Ingresa la caracteristica de la pelicula a modificar: ").lower().strip()
  if busatributo in peliculas:
    busvalor=input("Ingresa el valor de la caracteristica de la pelicula a modificar: ").upper().strip()
    if busvalor==peliculas[busatributo]:
      #print(peliculas[busatributo])
      atributo=input("Ingresa la nueva caracteristica de la pelicula: ").lower().strip()
      valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
      del peliculas[busatributo]
      peliculas[atributo]=valor
      #peliculas.update({atributo:valor})
      print(".::Operacion realizada con exito ✅ ::.")
    else:
      print("Valor no encontrado ⚠️ ")
  else:
    print("Caracteristica no encontrada ⚠️ ")'''

def modificarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: 🔄 modificar caracteristicas a pelicula 🔄  ::.\n ")
  if len(peliculas)>0:
    print("\n\t.:: Valores actuales ::.\n ")
    for i in peliculas:
      print(f"{i} : {peliculas[i]}")
      res=input(f"Quieres cambiar el valor {i} ? (Si/No): ").lower()
      if res=="si":
        peliculas.update({i:input(" 📝 tecla el nuevo valor: ").upper().strip()})
        input(".:: ✅ Operacion realizada con exito presione cualquier tecla ✅ ::.")
        borrarPantalla()
        
  else:
    print("⚠️ No hay peliculas en el sistema ⚠️")
  

'''def borrarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: Borrar caracteristicas a pelicula 📛 ::.\n ")
  for i in peliculas:
      print(f"\t {i} : {peliculas[i]} ")
  busatributo=input("Ingresa la caracteristica de la pelicula a borrar: ").lower().strip()
  if busatributo in peliculas:
    res=input("De verdad quieres borrarlo (s/n) ⚠️ : ").lower()
    if res=="s":
      del peliculas[busatributo]
      print(".::Operacion realizada con exito ✅ ::.")
  else:
    print("Caracteristica no encontrada ⚠️ ")'''


def borrarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: 📛 Borrar caracteristicas a pelicula 📛 ::.\n ")
  if len(peliculas)>0:
    print("\n\t.:: Valores actuales ::.\n ")
    for i in peliculas:
      print(f"{i} : {peliculas[i]}")
    resp=input("Quieres borrar una caracteristica de la pelicula? (Si/No): ").lower()
    if resp=="si":
      try:
        carac=input(" 📝 Teclea la caracteristica a borrar: ").lower().strip()
        peliculas.pop(carac)
        input(".:: ✅ Operacion realizada con exito presione cualquier tecla ✅ ::.")
        borrarPantalla()
      except KeyError:
        print(" ⚠️ Esta caracteristica no existe intente de nuevo ⚠️ ")

  else:
    print("⚠️ No hay peliculas en el sistema ⚠️")



