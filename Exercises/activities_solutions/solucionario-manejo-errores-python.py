# solucionario-actividad-sistema-gestion-tareas.py

import logging
from datetime import datetime, timedelta

logging.basicConfig(filename='sistema_tareas.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class TareaError(Exception):
    pass

class TareaNoEncontradaError(TareaError):
    pass

class FechaInvalidaError(TareaError):
    pass

class PrioridadInvalidaError(TareaError):
    pass

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = {}
        self.id_actual = 1

    def agregar_tarea(self, descripcion, fecha_vencimiento, prioridad):
        try:
            if fecha_vencimiento <= datetime.now():
                raise FechaInvalidaError("La fecha de vencimiento debe ser en el futuro.")
            
            if prioridad not in ['alta', 'media', 'baja']:
                raise PrioridadInvalidaError("La prioridad debe ser 'alta', 'media' o 'baja'.")
            
            nueva_tarea = {
                'id': self.id_actual,
                'descripcion': descripcion,
                'fecha_vencimiento': fecha_vencimiento,
                'prioridad': prioridad
            }
            self.tareas[self.id_actual] = nueva_tarea
            
            self.id_actual += 1
            return self.id_actual - 1
        except FechaInvalidaError as e:
            logging.error(f"Error al agregar tarea: {e}")
            raise
        except PrioridadInvalidaError as e:
            logging.error(f"Error al agregar tarea: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al agregar tarea: {e}")
            raise

    def modificar_tarea(self, id_tarea, **kwargs):
        try:
            if id_tarea not in self.tareas:
                raise TareaNoEncontradaError(f"No se encontró la tarea con ID {id_tarea}")
            
            for campo, valor in kwargs.items():
                if campo == 'fecha_vencimiento':
                    if valor <= datetime.now():
                        raise FechaInvalidaError("La fecha de vencimiento debe ser en el futuro.")
                elif campo == 'prioridad':
                    if valor not in ['alta', 'media', 'baja']:
                        raise PrioridadInvalidaError("La prioridad debe ser 'alta', 'media' o 'baja'.")
                
                self.tareas[id_tarea][campo] = valor
            
        except TareaNoEncontradaError as e:
            logging.error(f"Error al modificar tarea: {e}")
            raise
        except (FechaInvalidaError, PrioridadInvalidaError) as e:
            logging.error(f"Error al modificar tarea: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al modificar tarea: {e}")
            raise

    def eliminar_tarea(self, id_tarea):
        try:
            if id_tarea not in self.tareas:
                raise TareaNoEncontradaError(f"No se encontró la tarea con ID {id_tarea}")
            
            del self.tareas[id_tarea]
        except TareaNoEncontradaError as e:
            logging.error(f"Error al eliminar tarea: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al eliminar tarea: {e}")
            raise

    def obtener_tarea(self, id_tarea):
        try:
            if id_tarea not in self.tareas:
                raise TareaNoEncontradaError(f"No se encontró la tarea con ID {id_tarea}")
            
            return self.tareas[id_tarea]
        except TareaNoEncontradaError as e:
            logging.error(f"Error al obtener tarea: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al obtener tarea: {e}")
            raise

    def listar_tareas_vencidas(self):
        try:
            ahora = datetime.now()
            return [tarea for tarea in self.tareas.values() if tarea['fecha_vencimiento'] < ahora]
        except Exception as e:
            logging.error(f"Error al listar tareas vencidas: {e}")
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f"Error al salir del contexto: {exc_type}, {exc_val}")
        return False

def verificar_implementacion():
    with SistemaGestionTareas() as sistema:
        puntuacion = 0
        total_pruebas = 7

        print("Evaluando la implementación...\n")

        # Prueba 1: Agregar tarea
        try:
            id_tarea = sistema.agregar_tarea("Completar informe", datetime.now() + timedelta(days=7), "alta")
            assert id_tarea == 1
            print("✅ Prueba 1 pasada: Método agregar_tarea funciona correctamente")
            puntuacion += 1
        except Exception as e:
            print(f"❌ Prueba 1 fallida: Método agregar_tarea no funciona como se esperaba. Error: {e}")

        # Prueba 2: Agregar tarea con fecha inválida
        try:
            sistema.agregar_tarea("Tarea inválida", datetime.now() - timedelta(days=1), "media")
            print("❌ Prueba 2 fallida: Se permitió agregar una tarea con fecha pasada")
        except FechaInvalidaError:
            print("✅ Prueba 2 pasada: Se manejó correctamente la excepción de fecha inválida")
            puntuacion += 1
        except Exception as e:
            print(f"❌ Prueba 2 fallida: No se manejó correctamente la excepción de fecha inválida. Error: {e}")

        # Prueba 3: Modificar tarea
        try:
            sistema.modificar_tarea(1, descripcion="Completar informe urgente")
            tarea = sistema.obtener_tarea(1)
            assert tarea['descripcion'] == "Completar informe urgente"
            print("✅ Prueba 3 pasada: Método modificar_tarea funciona correctamente")
            puntuacion += 1
        except Exception as e:
            print(f"❌ Prueba 3 fallida: Método modificar_tarea no funciona como se esperaba. Error: {e}")

        # Prueba 4: Eliminar tarea
        try:
            sistema.eliminar_tarea(1)
            try:
                sistema.obtener_tarea(1)
                print("❌ Prueba 4 fallida: La tarea no se eliminó correctamente")
            except TareaNoEncontradaError:
                print("✅ Prueba 4 pasada: Método eliminar_tarea funciona correctamente")
                puntuacion += 1
        except Exception as e:
            print(f"❌ Prueba 4 fallida: Método eliminar_tarea no funciona como se esperaba. Error: {e}")

        # Prueba 5: Obtener tarea inexistente
        try:
            sistema.obtener_tarea(999)
            print("❌ Prueba 5 fallida: No se lanzó excepción al buscar una tarea inexistente")
        except TareaNoEncontradaError:
            print("✅ Prueba 5 pasada: Se manejó correctamente la excepción de tarea no encontrada")
            puntuacion += 1
        except Exception as e:
            print(f"❌ Prueba 5 fallida: No se manejó correctamente la excepción de tarea no encontrada. Error: {e}")

        # Prueba 6: Listar tareas vencidas
        try:
            sistema.agregar_tarea("Tarea vencida", datetime.now() + timedelta(seconds=1), "baja")
            import time
            time.sleep(2)  # Esperar a que la tarea se venza
            tareas_vencidas = sistema.listar_tareas_vencidas()
            assert len(tareas_vencidas) == 1
            print("✅ Prueba 6 pasada: Método listar_tareas_vencidas funciona correctamente")
            puntuacion += 1
        except Exception as e:
            print(f"❌ Prueba 6 fallida: Método listar_tareas_vencidas no funciona como se esperaba. Error: {e}")

        # Prueba 7: Verificar logging
        try:
            with open('sistema_tareas.log', 'r') as log_file:
                log_content = log_file.read()
                assert 'ERROR' in log_content
            print("✅ Prueba 7 pasada: El sistema de logging funciona correctamente")
            puntuacion += 1
        except Exception as e:
            print(f"❌ Prueba 7 fallida: El sistema de logging no funciona como se esperaba. Error: {e}")

        print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
        
        if puntuacion == total_pruebas:
            print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
            print("Has demostrado un excelente entendimiento de los conceptos avanzados de manejo de errores en Python.")
        else:
            print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

if __name__ == "__main__":
    verificar_implementacion()
