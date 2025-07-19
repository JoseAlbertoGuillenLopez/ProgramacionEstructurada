#peliculas=["JUAN","JUANO","DIC","JUAN"]

#diccionario u objeto para almacenar los atributos(nombre,cacarteristica,clasificacion,genero,idioma)
#se ponen en singular

#investigar como poner mas peliculas dentro de un diccionario
#update no actualiza es solo un append

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
  "clasificacion":"NIN",
  "genero":"ANIMA",
  "idioma":"ESP"
}

import mysql.connector
from mysql.connector import Error

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print(" 🕒 Oprima cualquier tecla para continuar 🕒 ...")
  input()  

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="bd_peliculas"
    )
    return conexion
  except Error as e:
    print("El error que sucedio es:",e)
    return None




def crearPeliculas(): 
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: 📝 Alta de Peliculas 📝 ::.\n ")
    peliculas.update({"nombre":input("📝 Ingresa el nombre: ").upper().strip()})
    peliculas.update({"categoria":input("📝 Ingresa la categoria: ").upper().strip()})
    peliculas.update({"clasificacion":input("📝 Ingresa la clasificacion: ").upper().strip()})
    peliculas.update({"genero":input("📝 Ingresa el genero: ").upper().strip()})
    peliculas.update({"idioma":input("📝 Ingresa el idioma: ").upper().strip()})

    #### AGREGAR REGISTRO A LA BASE DE DATOS
    try:
      cursor=conexionBD.cursor()
      cursor.execute(
        "insert into peliculas (id, nombre, categoria, clasificacion, genero, idioma) values (NULL, %s, %s, %s, %s, %s)",(peliculas["nombre"],peliculas["categoria"],peliculas["clasificacion"],peliculas["genero"],peliculas["idioma"])
      )
      conexionBD.commit()
      print(".:: ✅ Operacion realizada con exito ✅ ::.")  
    except Error as e:
      print("Error al intentar insertar un registro en la base de datos")


def mostrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: 🔍 Mostrar o consultar la pelicula 🔍 ::.\n ")
    cursor=conexionBD.cursor()
    cursor.execute(
      "select * from peliculas"
    )
    registros=cursor.fetchall()
    if len(registros)>0:
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(F"-"*80)
      for i in registros:
        print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
    else:
      print("\t .:: ⚠️ No hay peliculas en el sistema ⚠️::.")



def modificarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: 🔄 Modificar pelicula 🔄 ::.\n ")
  conexion=conectar()
  if conexion!=None:
    cursor=conexion.cursor()
    cursor.execute(
      "select * from peliculas"
    )
    registros=cursor.fetchall()
    if registros:
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(F"-"*80)
      for i in registros:
        print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
    else:
        print(" ⚠️ No hay registros ⚠️ ")
    id=input("Teclea el id de la pelicula que quieras modificar: ")
    cursor.execute(
      "select * from peliculas where id=%s", (id,)
    )
    registro=cursor.fetchall()
    if registro:
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(F"-"*80)
      for i in registro:
        print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
      peliculas["nombre"]=input("Nuevo nombre: ").upper().strip()
      peliculas["categoria"]=input("Nueva categoría: ").upper().strip()
      peliculas["clasificacion"]=input("Nueva clasificación: ").upper().strip()
      peliculas["genero"]=input("Nuevo género: ").upper().strip()
      peliculas["idioma"]=input("Nuevo idioma: ").upper().strip()
      try:
        cursor.execute(
          "update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where id=%s",(peliculas["nombre"],peliculas["categoria"],peliculas["clasificacion"],peliculas["genero"],peliculas["idioma"],id)
        )
        conexion.commit()
        print(".:: ✅ Operacion realizada con exito ✅ ::.")
      except Error as e:
        print("⚠️  Error al actualizar el registro  ⚠️")
    else:
      print("⚠️  ID no encontrada  ⚠️")
    



def borrarPeliculas():
  borrarPantalla()
  print("\n\t.:: 📛 Borrar o quitar pelicula 📛 ::.\n ")
  conexion=conectar()
  if conexion!=None:
    cursor=conexion.cursor()
    cursor.execute(
      "select * from peliculas"
    )
    registros=cursor.fetchall()
    if len(registros)>0:
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(F"-"*80)
      for i in registros:
        print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
    else:
      print(" ⚠️ No hay registros ⚠️ ")
      
    id=input("Teclea el id de la pelicula a borrar: ").upper().strip()
    cursor.execute(
        "select * from peliculas where id=%s", (id,)
      )
    registro=cursor.fetchall()
    if registro:
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(F"-"*80)
      for i in registro:
        print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
      resp=input(f"⚠️ Deseas borrar la pelicula con id: {id} del sistema? (S/N) ⚠️ :").lower()
      if resp=="s":
        try:
          cursor.execute(
            "DELETE FROM peliculas WHERE id= %s", (id,)
            #, AL FINAL PORQUE ESTO LO HACE CON TUPLAS O LISTAS Y PARA TUPLAS SE OCUPAN 2 O MAS ELEMENTOS LO PUEDO HACER CON LISTA TAMBIEN SIN LA ,
          )
          conexion.commit()
          print(".:: ✅ Operacion realizada con exito ✅ ::.")
        except Error as e:
          print("⚠️  Error al eliminar el registro  ⚠️")
    else:
        print("⚠️  ID no encontrada  ⚠️") 



def buscarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: 🔍 Mostrar o consultar una sola pelicula 🔍 ::.\n ")
    cursor=conexionBD.cursor()
    nombre=input("Teclea el nombre de la pelicula a buscar: ").upper().strip()
    cursor.execute(
      "SELECT * FROM peliculas WHERE nombre=%s",(nombre,)
    )
    registros=cursor.fetchall()
    if len(registros)>0:
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(F"-"*80)
      for i in registros:
        print(f"{i[0]:<10}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")
    else:
      print("\t .:: ⚠️ Pelicula no encontrada en el sistema ⚠️::.")





