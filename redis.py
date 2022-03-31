import redis
from sqlite3 import Error
import json
try:
    redis = redis.Redis(host='localhost', db=0)
    print("Conexion exitosa")
except Error:
    print("Conexion fallida")
print("DICCIONARIO DE SLANG 507")
print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES:")
print("1: Agregar")
print("2: Editar por ID")
print("3: Eliminar por ID")
print("4: Ver listado")
print("5: Buscar significado por ID")
seleccion = int(input(""))

if seleccion == 1:

    id_ = int(input("ID: "))
    palabra = input("Slang: ")
    definicion = input("definicion: ")

    try:
        redis.set(id_, json.dumps({"palabra":palabra,"definicion":definicion}))
        print("Insercion exitosa")
    except Error:
        print("Error en insercion")

elif seleccion == 2:

    try:
        id_ = int(input("ID a editar: "))
        editar_palabra = input("Cambiar palabra: ")
        editar_definicion = input("Nueva definicion: ")
        redis.set(id_, json.dumps({"palabra": editar_palabra, "definicion": editar_definicion}))
        print("Actualizacion exitosa")
    except Error:
        print("Error al actualizar datos")

elif seleccion == 3:

    try:

        remover = int(input("Eliminar por ID: "))
        id = remover
        redis.delete(id)
        print("Registro Eliminado")
    except Error:
        print("Error al eliminar")

elif seleccion == 4:
    try:
        id_ = redis.hgetall('id_')
        print(id_)


    except:
        print("Error al traer datos")

elif seleccion == 5:
    try:
        peticion = int(input("Buscar por ID: "))
        id = peticion
        print(redis.get(id))

    except Error:
        print("Error al traer datos")