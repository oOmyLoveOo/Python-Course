# solucionario-actividad-excepciones-personalizadas.py

import logging

logging.basicConfig(filename='inventario.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class ErrorInventario(Exception):
    def __init__(self, mensaje, codigo_error):
        super().__init__(mensaje)
        self.codigo_error = codigo_error

class ProductoNoEncontrado(ErrorInventario):
    def __init__(self, mensaje, id_producto):
        super().__init__(mensaje, codigo_error="PROD_NOT_FOUND")
        self.id_producto = id_producto

class CantidadInvalida(ErrorInventario):
    def __init__(self, mensaje, cantidad):
        super().__init__(mensaje, codigo_error="INVALID_QUANTITY")
        self.cantidad = cantidad

class ProductoExistente(ErrorInventario):
    def __init__(self, mensaje, id_producto):
        super().__init__(mensaje, codigo_error="PROD_EXISTS")
        self.id_producto = id_producto

class CapacidadExcedida(ErrorInventario):
    def __init__(self, mensaje, cantidad_excedida):
        super().__init__(mensaje, codigo_error="CAPACITY_EXCEEDED")
        self.cantidad_excedida = cantidad_excedida

class SistemaInventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto, nombre, cantidad):
        try:
            if id_producto in self.productos:
                raise ProductoExistente(f"El producto con ID {id_producto} ya existe", id_producto)
            if cantidad < 0:
                raise CantidadInvalida(f"La cantidad {cantidad} es inválida", cantidad)
            self.productos[id_producto] = {"nombre": nombre, "cantidad": cantidad}
        except ErrorInventario as e:
            logging.error(f"Error al agregar producto: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al agregar producto: {e}")
            raise

    def retirar_producto(self, id_producto, cantidad):
        try:
            if id_producto not in self.productos:
                raise ProductoNoEncontrado(f"El producto con ID {id_producto} no existe", id_producto)
            if cantidad <= 0:
                raise CantidadInvalida(f"La cantidad a retirar {cantidad} es inválida", cantidad)
            if self.productos[id_producto]["cantidad"] < cantidad:
                raise CantidadInvalida(f"No hay suficiente cantidad disponible", cantidad)
            self.productos[id_producto]["cantidad"] -= cantidad
        except ErrorInventario as e:
            logging.error(f"Error al retirar producto: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al retirar producto: {e}")
            raise

    def obtener_cantidad(self, id_producto):
        try:
            if id_producto not in self.productos:
                raise ProductoNoEncontrado(f"El producto con ID {id_producto} no existe", id_producto)
            return self.productos[id_producto]["cantidad"]
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
