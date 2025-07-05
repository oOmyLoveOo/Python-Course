# solucionario-actividad-avanzada-bases-datos-python.py

import sqlite3
import hashlib
from datetime import datetime, timedelta
import os
import time

class GestorBiblioteca:
    def __init__(self, nombre_db='biblioteca.db'):
        try:
            self.conexion = sqlite3.connect(nombre_db)
            self.cursor = self.conexion.cursor()
            self.crear_tablas()
            self.crear_indices()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")

    def crear_tablas(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    cantidad INTEGER NOT NULL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS prestamos (
                    id INTEGER PRIMARY KEY,
                    libro_id INTEGER,
                    usuario_id INTEGER,
                    fecha_prestamo DATE NOT NULL,
                    fecha_devolucion DATE,
                    FOREIGN KEY (libro_id) REFERENCES libros (id),
                    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
                )
            ''')
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")

    def crear_indices(self):
        try:
            self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_libros_isbn ON libros (isbn)')
            self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_usuarios_email ON usuarios (email)')
            self.cursor.execute('CREATE INDEX IF NOT EXISTS idx_prestamos_fecha ON prestamos (fecha_prestamo, fecha_devolucion)')
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al crear los índices: {e}")

    def agregar_libro(self, titulo, autor, isbn, cantidad):
        try:
            self.cursor.execute('''
                INSERT INTO libros (titulo, autor, isbn, cantidad)
                VALUES (?, ?, ?, ?)
            ''', (titulo, autor, isbn, cantidad))
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: El ISBN ya existe en la base de datos.")
            return False
        except sqlite3.Error as e:
            print(f"Error al agregar libro: {e}")
            return False

    def registrar_usuario(self, nombre, email, password):
        try:
            password_hash = hash_password(password)
            self.cursor.execute('''
                INSERT INTO usuarios (nombre, email, password)
                VALUES (?, ?, ?)
            ''', (nombre, email, password_hash))
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: El email ya existe en la base de datos.")
            return False
        except sqlite3.Error as e:
            print(f"Error al registrar usuario: {e}")
            return False

    def prestar_libro(self, isbn, email):
        try:
            self.conexion.execute("BEGIN TRANSACTION")
            self.cursor.execute("SELECT id, cantidad FROM libros WHERE isbn = ?", (isbn,))
            libro = self.cursor.fetchone()
            if not libro or libro[1] <= 0:
                raise ValueError("Libro no disponible")
            
            self.cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
            usuario = self.cursor.fetchone()
            if not usuario:
                raise ValueError("Usuario no encontrado")
            
            self.cursor.execute('''
                INSERT INTO prestamos (libro_id, usuario_id, fecha_prestamo)
                VALUES (?, ?, date('now'))
            ''', (libro[0], usuario[0]))
            
            self.cursor.execute("UPDATE libros SET cantidad = cantidad - 1 WHERE id = ?", (libro[0],))
            self.conexion.commit()
            return True
        except sqlite3.Error as e:
            self.conexion.rollback()
            print(f"Error al prestar libro: {e}")
            return False
        except ValueError as e:
            self.conexion.rollback()
            print(f"Error al prestar libro: {e}")
            return False

    def devolver_libro(self, isbn, email):
        try:
            self.conexion.execute("BEGIN TRANSACTION")
            self.cursor.execute('''
                SELECT p.id, l.id 
                FROM prestamos p
                JOIN libros l ON p.libro_id = l.id
                JOIN usuarios u ON p.usuario_id = u.id
                WHERE l.isbn = ? AND u.email = ? AND p.fecha_devolucion IS NULL
            ''', (isbn, email))
            prestamo = self.cursor.fetchone()
            if not prestamo:
                raise ValueError("Préstamo no encontrado")
            
            self.cursor.execute('''
                UPDATE prestamos 
                SET fecha_devolucion = date('now')
                WHERE id = ?
            ''', (prestamo[0],))
            
            self.cursor.execute("UPDATE libros SET cantidad = cantidad + 1 WHERE id = ?", (prestamo[1],))
            self.conexion.commit()
            return True
        except sqlite3.Error as e:
            self.conexion.rollback()
            print(f"Error al devolver libro: {e}")
            return False
        except ValueError as e:
            self.conexion.rollback()
            print(f"Error al devolver libro: {e}")
            return False

    def libros_prestados_por_usuario(self, email):
        try:
            self.cursor.execute('''
                SELECT l.titulo, l.autor, l.isbn, p.fecha_prestamo
                FROM prestamos p
                JOIN libros l ON p.libro_id = l.id
                JOIN usuarios u ON p.usuario_id = u.id
                WHERE u.email = ? AND p.fecha_devolucion IS NULL
            ''', (email,))
            return [{'titulo': row[0], 'autor': row[1], 'isbn': row[2], 'fecha_prestamo': row[3]} 
                    for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al obtener libros prestados: {e}")
            return []

    def usuarios_con_prestamos_vencidos(self):
        try:
            fecha_limite = (datetime.now() - timedelta(days=14)).strftime('%Y-%m-%d')
            self.cursor.execute('''
                SELECT DISTINCT u.nombre, u.email
                FROM usuarios u
                JOIN prestamos p ON u.id = p.usuario_id
                WHERE p.fecha_prestamo <= ? AND p.fecha_devolucion IS NULL
            ''', (fecha_limite,))
            return [{'nombre': row[0], 'email': row[1]} for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al obtener usuarios con préstamos vencidos: {e}")
            return []

    def cerrar_conexion(self):
        try:
            self.conexion.close()
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexión: {e}")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verificar_implementacion():
    nombre_db = 'test_biblioteca.db'
    gestor = GestorBiblioteca(nombre_db)
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando la implementación...\n")

    # Prueba 1: Agregar libro
    try:
        assert gestor.agregar_libro("1984", "George Orwell", "9780451524935", 5) == True
        assert gestor.agregar_libro("To Kill a Mockingbird", "Harper Lee", "9780446310789", 3) == True
        print("✅ Prueba 1 pasada: Método agregar_libro funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: Método agregar_libro no funciona como se esperaba")

    # Prueba 2: Registrar usuario
    try:
        assert gestor.registrar_usuario("Alice Johnson", "alice@example.com", "password123") == True
        assert gestor.registrar_usuario("Bob Smith", "bob@example.com", "securepass") == True
        print("✅ Prueba 2 pasada: Método registrar_usuario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: Método registrar_usuario no funciona como se esperaba")

    # Prueba 3: Prestar libro
    try:
        assert gestor.prestar_libro("9780451524935", "alice@example.com") == True
        print("✅ Prueba 3 pasada: Método prestar_libro funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: Método prestar_libro no funciona como se esperaba")

    # Prueba 4: Devolver libro
    try:
        assert gestor.devolver_libro("9780451524935", "alice@example.com") == True
        print("✅ Prueba 4 pasada: Método devolver_libro funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: Método devolver_libro no funciona como se esperaba")

    # Prueba 5: Libros prestados por usuario
    try:
        gestor.prestar_libro("9780451524935", "bob@example.com")
        libros_prestados = gestor.libros_prestados_por_usuario("bob@example.com")
        assert len(libros_prestados) == 1 and libros_prestados[0]['titulo'] == "1984"
        print("✅ Prueba 5 pasada: Método libros_prestados_por_usuario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: Método libros_prestados_por_usuario no funciona como se esperada")

    # Prueba 6: Usuarios con préstamos vencidos
    try:
        # Simular un préstamo vencido
        gestor.cursor.execute("""
            INSERT INTO prestamos (libro_id, usuario_id, fecha_prestamo, fecha_devolucion)
            VALUES (
                (SELECT id FROM libros WHERE isbn = '9780446310789'),
                (SELECT id FROM usuarios WHERE email = 'alice@example.com'),
                date('now', '-15 days'),
                NULL
            )
        """)
        gestor.conexion.commit()
        
        usuarios_vencidos = gestor.usuarios_con_prestamos_vencidos()
        assert len(usuarios_vencidos) == 1 and usuarios_vencidos[0]['email'] == "alice@example.com"
        print("✅ Prueba 6 pasada: Método usuarios_con_prestamos_vencidos funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Método usuarios_con_prestamos_vencidos no funciona como se esperaba")

    # Prueba 7: Prevención de inyección SQL
    try:
        titulo_malicioso = "Libro Malicioso' OR '1'='1"
        gestor.agregar_libro(titulo_malicioso, "Autor Malicioso", "1234567890", 1)
        gestor.cursor.execute("SELECT * FROM libros WHERE titulo = ?", (titulo_malicioso,))
        assert len(gestor.cursor.fetchall()) == 1
        print("✅ Prueba 7 pasada: Las consultas son seguras contra inyección SQL")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: Las consultas no son seguras contra inyección SQL")

    # Prueba 8: Verificar la creación de índices
    try:
        gestor.cursor.execute("PRAGMA index_list(libros)")
        indices_libros = gestor.cursor.fetchall()
        gestor.cursor.execute("PRAGMA index_list(usuarios)")
        indices_usuarios = gestor.cursor.fetchall()
        assert len(indices_libros) >= 1 and len(indices_usuarios) >= 1
        print("✅ Prueba 8 pasada: Los índices se han creado correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: No se han creado los índices esperados")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un excelente entendimiento de los conceptos avanzados de bases de datos en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

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
