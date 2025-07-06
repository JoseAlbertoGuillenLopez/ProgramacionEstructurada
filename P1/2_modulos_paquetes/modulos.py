'''Un modulo es simplemente un archivo con extensiones py que contienen codigo de python, puede tener NADA
(para que se considere modulo debe de tener: funciones,clases,variables,etc.)'''
#un solo archivo con funciones es un modulo
import os


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


#caso 4
def solidatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom,telefono

#funciones para BORRAR PANTALLA Y ESPERAR TECLA

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("...Oprima una tecla para continuar... ")

def saludar(nombre):
    #recomendacion crear variables locales y trabajar con ellas (nom)
    nom=nombre
    return f"\t Hola, bienvendio {nom}!\n"