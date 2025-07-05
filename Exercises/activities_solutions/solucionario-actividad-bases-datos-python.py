# solucionario-actividad-bases-datos-python.py

import sqlite3
import hashlib
import os
import time

class GestorBD:
    def __init__(self, nombre_db='usuarios.db'):
        try:
            self.conexion = sqlite3.connect(nombre_db)
            self.cursor = self.conexion.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    email TEXT UNIQUE,
                    password TEXT
                )
            ''')
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
    
    def insertar_usuario(self, nombre, email, password):
        try:
            self.cursor.execute('''
                INSERT INTO usuarios (nombre, email, password)
                VALUES (?, ?, ?)
            ''', (nombre, email, password))
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: El email ya existe en la base de datos.")
            return False
        except sqlite3.Error as e:
            print(f"Error al insertar usuario: {e}")
            return False

    def obtener_usuario(self, email):
        try:
            self.cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
            usuario = self.cursor.fetchone()
            if usuario:
                return {
                    'id': usuario[0],
                    'nombre': usuario[1],
                    'email': usuario[2],
                    'password': usuario[3]
                }
            return None
        except sqlite3.Error as e:
            print(f"Error al obtener usuario: {e}")
            return None

    def actualizar_usuario(self, email, nuevo_nombre):
        try:
            self.cursor.execute('''
                UPDATE usuarios
                SET nombre = ?
                WHERE email = ?
            ''', (nuevo_nombre, email))
            self.conexion.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    def eliminar_usuario(self, email):
        try:
            self.cursor.execute('DELETE FROM usuarios WHERE email = ?', (email,))
            self.conexion.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al eliminar usuario: {e}")
            return False

    def cerrar_conexion(self):
        try:
            self.conexion.close()
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexión: {e}")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

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
