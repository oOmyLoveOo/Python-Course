# Actividad Avanzada: Sistema de gestión de tareas con manejo de errores avanzado

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función y clase.
2. Completa los espacios marcados con ___ usando los conceptos avanzados de tratamiento de errores en Python.
3. Presta especial atención a las excepciones personalizadas, logging, y manejo de errores en diferentes contextos.
4. Implementa medidas de seguridad y buenas prácticas en el manejo de errores.
5. Utiliza los ejemplos y guías proporcionados para cada método como referencia.
6. Una vez completado, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

import logging
from datetime import datetime, timedelta

# Configuración básica de logging
logging.basicConfig(filename='sistema_tareas.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class TareaError(Exception):
    """Clase base para excepciones personalizadas relacionadas con tareas."""
    pass

class TareaNoEncontradaError(TareaError):
    """Se lanza cuando no se encuentra una tarea específica."""
    pass

class FechaInvalidaError(TareaError):
    """Se lanza cuando se proporciona una fecha inválida."""
    pass

class PrioridadInvalidaError(TareaError):
    """Se lanza cuando se proporciona una prioridad inválida."""
    pass

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = {}
        self.id_actual = 1

    def agregar_tarea(self, descripcion, fecha_vencimiento, prioridad):
        """
        Agrega una nueva tarea al sistema.
        Maneja posibles errores de fecha y prioridad inválidas.

        Ejemplo de uso:
        try:
            id_tarea = sistema.agregar_tarea("Completar informe", datetime.now() + timedelta(days=7), "alta")
            print(f"Tarea agregada con ID: {id_tarea}")
        except FechaInvalidaError:
            print("La fecha proporcionada es inválida.")
        except PrioridadInvalidaError:
            print("La prioridad proporcionada es inválida.")

        Tu tarea:
        - Implementa las validaciones necesarias
        - Agrega la tarea al diccionario self.tareas si es válida
        - Incrementa self.id_actual y devuelve el ID de la nueva tarea
        - Utiliza logging para registrar errores
        """
        try:
            ___

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
        """
        Modifica una tarea existente.
        Permite cambiar descripción, fecha de vencimiento y/o prioridad.

        Ejemplo de uso:
        try:
            sistema.modificar_tarea(1, descripcion="Nueva descripción", prioridad="media")
            print("Tarea modificada exitosamente.")
        except TareaNoEncontradaError:
            print("No se encontró la tarea especificada.")
        except FechaInvalidaError:
            print("La nueva fecha proporcionada es inválida.")
        except PrioridadInvalidaError:
            print("La nueva prioridad proporcionada es inválida.")

        Tu tarea:
        - Verifica si la tarea existe
        - Actualiza los campos proporcionados en kwargs
        - Valida los nuevos valores (fecha y prioridad)
        - Utiliza logging para registrar errores
        """
        try:
            ___

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
        """
        Elimina una tarea del sistema.

        Ejemplo de uso:
        try:
            sistema.eliminar_tarea(1)
            print("Tarea eliminada exitosamente.")
        except TareaNoEncontradaError:
            print("No se encontró la tarea especificada.")

        Tu tarea:
        - Verifica si la tarea existe
        - Elimina la tarea del diccionario self.tareas
        - Utiliza logging para registrar errores
        """
        try:
            ___

        except TareaNoEncontradaError as e:
            logging.error(f"Error al eliminar tarea: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al eliminar tarea: {e}")
            raise

    def obtener_tarea(self, id_tarea):
        """
        Obtiene una tarea específica por su ID.

        Ejemplo de uso:
        try:
            tarea = sistema.obtener_tarea(1)
            print(f"Tarea encontrada: {tarea}")
        except TareaNoEncontradaError:
            print("No se encontró la tarea especificada.")

        Tu tarea:
        - Verifica si la tarea existe
        - Devuelve la tarea si se encuentra
        - Utiliza logging para registrar errores
        """
        try:
            ___

        except TareaNoEncontradaError as e:
            logging.error(f"Error al obtener tarea: {e}")
            raise
        except Exception as e:
            logging.critical(f"Error inesperado al obtener tarea: {e}")
            raise

    def listar_tareas_vencidas(self):
        """
        Retorna una lista de tareas vencidas.

        Ejemplo de uso:
        try:
            tareas_vencidas = sistema.listar_tareas_vencidas()
            print(f"Tareas vencidas: {tareas_vencidas}")
        except Exception as e:
            print(f"Error al listar tareas vencidas: {e}")

        Tu tarea:
        - Filtra las tareas cuya fecha de vencimiento es anterior a la fecha actual
        - Devuelve la lista de tareas vencidas
        - Utiliza logging para registrar errores
        """
        try:
            ___

        except Exception as e:
            logging.error(f"Error al listar tareas vencidas: {e}")
            raise

    def __enter__(self):
        """
        Método para soporte del manejo de contexto.
        
        Ejemplo de uso:
        with SistemaGestionTareas() as sistema:
            # Usar el sistema...

        Tu tarea:
        - Implementa este método para permitir el uso del context manager
        """
        ___

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método para soporte del manejo de contexto y limpieza de recursos.
        
        Tu tarea:
        - Implementa la lógica de limpieza necesaria
        - Utiliza logging para registrar errores si ocurren
        """
        if exc_type is not None:
            logging.error(f"Error al salir del contexto: {exc_type}, {exc_val}")
        ___
        return False  # Permite que la excepción se propague

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
