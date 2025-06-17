# Actividad: Operaciones CRUD y seguridad en Bases de Datos con Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función y clase.
2. Completa los espacios marcados con ___ usando los conceptos de bases de datos con Python.
3. No modifiques los nombres de las clases y métodos existentes, ni la estructura de los bloques try-except.
4. Una vez que hayas completado todo, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

import sqlite3
import hashlib
import os
import time

class GestorBD:
    def __init__(self, nombre_db='usuarios.db'):
        try:
            # PISTA: Debes inicializar la conexión a la base de datos, crear un cursor y 
            # crear la tabla 'usuarios' si no existe con los campos:
            # id (clave primaria), nombre, email (único) y password
            # Recuerda hacer commit para guardar los cambios
            ___
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
    
    def insertar_usuario(self, nombre, email, password):
        try:
            # PISTA: Debes ejecutar una consulta SQL para insertar un nuevo registro en la tabla usuarios
            # Utiliza placeholders (?) para evitar inyección SQL y prepara los parámetros como tupla
            # Recuerda hacer commit para guardar los cambios y retornar True si todo sale bien
            ___
        except sqlite3.IntegrityError:
            print("Error: El email ya existe en la base de datos.")
            return False
        except sqlite3.Error as e:
            print(f"Error al insertar usuario: {e}")
            return False

    def obtener_usuario(self, email):
        try:
            # PISTA: Debes ejecutar una consulta SELECT para obtener un usuario por su email
            # Utiliza fetchone() para obtener un solo resultado
            # Si el usuario existe, retorna un diccionario con sus datos (id, nombre, email, password)
            # Si no existe, retorna None
            ___
        except sqlite3.Error as e:
            print(f"Error al obtener usuario: {e}")
            return None

    def actualizar_usuario(self, email, nuevo_nombre):
        try:
            # PISTA: Debes ejecutar una consulta UPDATE para cambiar el nombre de un usuario
            # Utiliza placeholders para evitar inyección SQL
            # Recuerda hacer commit para guardar los cambios
            # Retorna True si se actualizó al menos una fila (rowcount > 0), False en caso contrario
            ___
        except sqlite3.Error as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    def eliminar_usuario(self, email):
        try:
            # PISTA: Debes ejecutar una consulta DELETE para eliminar un usuario por su email
            # Utiliza placeholders para evitar inyección SQL
            # Recuerda hacer commit para guardar los cambios
            # Retorna True si se eliminó al menos una fila (rowcount > 0), False en caso contrario
            ___
        except sqlite3.Error as e:
            print(f"Error al eliminar usuario: {e}")
            return False

    def cerrar_conexion(self):
        try:
            # PISTA: Debes cerrar la conexión a la base de datos
            ___
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexión: {e}")

def hash_password(password):
    # PISTA: Debes implementar una función que convierta la contraseña a un hash usando hashlib
    # Recuerda codificar el string a bytes usando .encode() antes de aplicar el hash
    # Retorna el hexadecimal del hash usando .hexdigest()
    ___

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 6
    nombre_db = 'test_usuarios.db'

    print("Evaluando la implementación...\n")

    try:
        gestor = GestorBD(nombre_db)
        print("✅ Prueba 1 pasada: La clase GestorBD se inicializa correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: La clase GestorBD no se inicializa como se esperaba")

    try:
        gestor = GestorBD(nombre_db)
        assert gestor.insertar_usuario("Juan Pérez", "juan@ejemplo.com", hash_password("password123")) == True
        print("✅ Prueba 2 pasada: El método insertar_usuario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: El método insertar_usuario no funciona como se esperaba")

    try:
        gestor = GestorBD(nombre_db)
        gestor.insertar_usuario("María López", "maria@ejemplo.com", hash_password("securepass"))
        usuario = gestor.obtener_usuario("maria@ejemplo.com")
        assert usuario['nombre'] == "María López"
        assert usuario['email'] == "maria@ejemplo.com"
        print("✅ Prueba 3 pasada: El método obtener_usuario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: El método obtener_usuario no funciona como se esperaba")

    try:
        gestor = GestorBD(nombre_db)
        gestor.insertar_usuario("Carlos Ruiz", "carlos@ejemplo.com", hash_password("pass1234"))
        assert gestor.actualizar_usuario("carlos@ejemplo.com", "Carlos Rodríguez") == True
        usuario_actualizado = gestor.obtener_usuario("carlos@ejemplo.com")
        assert usuario_actualizado['nombre'] == "Carlos Rodríguez"
        print("✅ Prueba 4 pasada: El método actualizar_usuario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: El método actualizar_usuario no funciona como se esperaba")

    try:
        gestor = GestorBD(nombre_db)
        gestor.insertar_usuario("Ana Martínez", "ana@ejemplo.com", hash_password("anapass"))
        assert gestor.eliminar_usuario("ana@ejemplo.com") == True
        assert gestor.obtener_usuario("ana@ejemplo.com") == None
        print("✅ Prueba 5 pasada: El método eliminar_usuario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: El método eliminar_usuario no funciona como se esperaba")

    try:
        gestor = GestorBD(nombre_db)
        email_malicioso = "usuario@ejemplo.com' --"
        gestor.insertar_usuario("Usuario Malicioso", email_malicioso, hash_password("hackpass"))
        assert gestor.obtener_usuario(email_malicioso) != None
        assert gestor.obtener_usuario("usuario@ejemplo.com") == None
        print("✅ Prueba 6 pasada: Las consultas son seguras contra inyección SQL")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Las consultas no son seguras contra inyección SQL")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de los conceptos de bases de datos y seguridad en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

    # Cerramos todas las conexiones
    gestor.cerrar_conexion()
    
    # Intentamos eliminar el archivo de la base de datos
    max_intentos = 5
    for intento in range(max_intentos):
        try:
            if os.path.exists(nombre_db):
                os.remove(nombre_db)
            break
        except PermissionError:
            if intento < max_intentos - 1:
                time.sleep(1)  # Esperamos un segundo antes de reintentar
            else:
                print(f"No se pudo eliminar el archivo {nombre_db}. Por favor, cierra todas las conexiones a la base de datos y elimina el archivo manualmente.")

if __name__ == "__main__":
    verificar_implementacion()
