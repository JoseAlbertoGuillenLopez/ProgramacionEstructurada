import datetime
from conexionBD import *

def crear(usuario_id,titulo,descripcion):
    try:
        fecha=datetime.datetime.now() 
        cursor.execute(
            "insert into notas (usuario_id,titulo,descripcion,fecha) values (%s,%s,%s,NOW())",(usuario_id,titulo,descripcion)
        )
        conexion.commit()
        return True
    except:
        return False
    

def mostrar(usuario_id):
    try:
        cursor.execute(
            "select * from notas where usuario_id=%s",(usuario_id,)
        )
        registro=cursor.fetchall()
        if registro:
            return registro 
        else:
            return None
    except:
        return None
    
def check(id):
    try:
        cursor.execute(
            "select * from notas where id=%s",(id,)
        )
        registro=cursor.fetchall()
        if registro:
            return registro 
        else:
            return None
    except:
        return None
    

def cambiar(id,titulo,descripcion):
    try:
        cursor.execute(
            "select * from notas where id=%s",(id,)
        )
        registro=cursor.fetchall()
        if registro:
            cursor.execute(
                "update notas set titulo=%s, descripcion=%s, fecha=NOW() where id=%s",(titulo,descripcion,id)
            )
            conexion.commit()
            return registro
        else:
            return None
    except:
        return False
    

def eliminar(id):
    try:
        cursor.execute(
            "delete from notas where id=%s",(id,)
        )
        conexion.commit()
        return True
    except:
        return False