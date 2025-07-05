# Actividad: Desarrollo de Excepciones Personalizadas en un Sistema de Gestión de Inventario

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada clase y función.
2. Completa los espacios marcados con ___ utilizando los conceptos de excepciones personalizadas.
3. Presta especial atención a la creación de una jerarquía de excepciones y al uso de __init__ con super().
4. Implementa las excepciones y el manejo de errores en las funciones proporcionadas.
5. Una vez completado, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

import logging

# Configuración básica de logging
logging.basicConfig(filename='inventario.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Excepción base para el sistema de inventario
class ErrorInventario(Exception):
    """
    Excepción base para el sistema de inventario.
    
    Tu tarea:
    - Implementa el método __init__ que acepta un mensaje y un código de error
    - Utiliza super() para inicializar la clase base Exception
    - Agrega un atributo para el código de error
    """
    def __init__(self, mensaje, codigo_error):
        ___

# Excepción para cuando un producto no se encuentra
class ProductoNoEncontrado(ErrorInventario):
    """
    Se lanza cuando un producto no se encuentra en el inventario.
    
    Tu tarea:
    - Implementa el método __init__ que acepta un mensaje y el ID del producto
    - Utiliza super() para inicializar la clase base ErrorInventario
    - Agrega un atributo para el ID del producto
    """
    def __init__(self, mensaje, id_producto):
        ___

# Excepción para cuando la cantidad de un producto es inválida
class CantidadInvalida(ErrorInventario):
    """
    Se lanza cuando se intenta agregar o retirar una cantidad inválida de un producto.
    
    Tu tarea:
    - Implementa el método __init__ que acepta un mensaje y la cantidad inválida
    - Utiliza super() para inicializar la clase base ErrorInventario
    - Agrega un atributo para la cantidad inválida
    """
    def __init__(self, mensaje, cantidad):
        ___

# Implementa al menos dos excepciones más que hereden de ErrorInventario
# Por ejemplo: ProductoExistente, CapacidadExcedida, etc.

___

class SistemaInventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto, nombre, cantidad):
        """
        Agrega un nuevo producto al inventario.
        
        Tu tarea:
        - Implementa el método para agregar un producto
        - Lanza una excepción personalizada si el producto ya existe
        - Lanza una excepción si la cantidad es inválida (por ejemplo, negativa)
        - Utiliza logging para registrar errores
        """
        try:
            ___
        except ErrorInventario as e:
            logging.error(f"Error al agregar producto: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al agregar producto: {e}")
            raise

    def retirar_producto(self, id_producto, cantidad):
        """
        Retira una cantidad de un producto del inventario.
        
        Tu tarea:
        - Implementa el método para retirar una cantidad de un producto
        - Lanza una excepción si el producto no existe
        - Lanza una excepción si la cantidad a retirar es inválida o mayor que la disponible
        - Utiliza logging para registrar errores
        """
        try:
            ___
        except ErrorInventario as e:
            logging.error(f"Error al retirar producto: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al retirar producto: {e}")
            raise

    def obtener_cantidad(self, id_producto):
        """
        Obtiene la cantidad disponible de un producto.
        
        Tu tarea:
        - Implementa el método para obtener la cantidad de un producto
        - Lanza una excepción si el producto no existe
        - Utiliza logging para registrar errores
        """
        try:
            ___
        except ErrorInventario as e:
            logging.error(f"Error al obtener cantidad de producto: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al obtener cantidad de producto: {e}")
            raise

def verificar_implementacion():
    inventario = SistemaInventario()
    puntuacion = 0
    total_pruebas = 5

    print("Evaluando la implementación...\n")

    # Prueba 1: Agregar producto
    try:
        inventario.agregar_producto("001", "Laptop", 10)
        print("✅ Prueba 1 pasada: Método agregar_producto funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 1 fallida: {e}")

    # Prueba 2: Agregar producto existente
    try:
        inventario.agregar_producto("001", "Laptop", 5)
        print("❌ Prueba 2 fallida: Se permitió agregar un producto existente")
    except ErrorInventario as e:
        print("✅ Prueba 2 pasada: Se manejó correctamente la excepción de producto existente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 2 fallida: {e}")

    # Prueba 3: Retirar producto
    try:
        inventario.retirar_producto("001", 3)
        cantidad = inventario.obtener_cantidad("001")
        assert cantidad == 7, f"La cantidad esperada era 7, pero se obtuvo {cantidad}"
        print("✅ Prueba 3 pasada: Método retirar_producto funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 3 fallida: {e}")

    # Prueba 4: Retirar cantidad inválida
    try:
        inventario.retirar_producto("001", 20)
        print("❌ Prueba 4 fallida: Se permitió retirar más cantidad de la disponible")
    except CantidadInvalida:
        print("✅ Prueba 4 pasada: Se manejó correctamente la excepción de cantidad inválida")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 4 fallida: {e}")

    # Prueba 5: Obtener cantidad de producto inexistente
    try:
        inventario.obtener_cantidad("999")
        print("❌ Prueba 5 fallida: Se permitió obtener la cantidad de un producto inexistente")
    except ProductoNoEncontrado:
        print("✅ Prueba 5 pasada: Se manejó correctamente la excepción de producto no encontrado")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 5 fallida: {e}")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un excelente entendimiento de las excepciones personalizadas en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

if __name__ == "__main__":
    verificar_implementacion()
