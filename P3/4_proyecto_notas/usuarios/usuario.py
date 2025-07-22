from conexionBD import *
import datetime 
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
            "insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)",(nombre,apellidos,email,contrasena,fecha)
        )
        conexion.commit()
        return True

    except:
        return False 


def iniciar_sesion(email,contrasena):
    try:
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
            "select * from usuarios where email=%s and password=%s",(email,contrasena)
        )
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        return None