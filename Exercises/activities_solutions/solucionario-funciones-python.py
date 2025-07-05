# Actividad: Funciones en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando las operaciones de funciones apropiadas.
3. No modifiques los nombres de las funciones existentes.
4. Una vez que hayas completado todo, ejecuta este script.

¡Buena suerte!
"""

# Importaciones necesarias
import io
import sys
from contextlib import redirect_stdout
import time

# Parte 1: Funciones básicas y retornos
def calcular_potencia(base, exponente):
    """
    Calcula la potencia de base elevada a exponente y devuelve el resultado.
    """
    return base ** exponente

def retornar_multiples_valores(a, b):
    """
    Devuelve una tupla con: suma, resta, multiplicación y división de a y b.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)

# Parte 2: Funciones lambda
def obtener_funcion_filtro():
    """
    Devuelve una función lambda que filtra números pares.
    La función debe devolver True si el número es par, False en caso contrario.
    """
    return lambda x: x % 2 == 0

def aplicar_operacion(lista, operacion):
    """
    Aplica la función 'operacion' a cada elemento de la lista y devuelve una nueva lista.
    Pista: Usa map() y convierte el resultado a lista.
    """
    return list(map(operacion, lista))

# Parte 3: Args y Kwargs
def suma_todos(*args):
    """
    Suma todos los argumentos posicionales pasados a la función.
    Si no hay argumentos, devuelve 0.
    """
    return sum(args) if args else 0

def crear_persona(nombre, **kwargs):
    """
    Crea un diccionario con la información de una persona.
    El nombre es obligatorio, pero el resto de atributos son opcionales.
    """
    persona = {"nombre": nombre}
    persona.update(kwargs)
    return persona

# Parte 4: Scope y clausuras
contador = 0

def crear_incrementador(incremento):
    """
    Crea y devuelve una función que incrementa el contador global según el valor 'incremento'.
    """
    def incrementador():
        global contador
        contador += incremento
        return contador
    
    return incrementador

def crear_contador_local():
    """
    Crea y devuelve una función que mantiene un contador local.
    Cada vez que se llama a la función devuelta, el contador se incrementa en 1.
    """
    contador = 0
    
    def contador_local():
        nonlocal contador
        contador += 1
        return contador
    
    return contador_local

# Parte 5: Decoradores
def registrar_llamada(funcion):
    """
    Decorador que registra cuando se llama a una función.
    Debe imprimir "Llamando a {nombre_funcion}" antes de ejecutar la función
    y "Llamada a {nombre_funcion} completada" después de ejecutarla.
    """
    def wrapper(*args, **kwargs):
        print(f"Llamando a {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"Llamada a {funcion.__name__} completada")
        return resultado
    
    return wrapper

def medir_tiempo(funcion):
    """
    Decorador que mide el tiempo de ejecución de una función.
    Debe imprimir "La función {nombre_funcion} tardó {tiempo} segundos en ejecutarse".
    """
    import time
    
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        tiempo = fin - inicio
        print(f"La función {funcion.__name__} tardó {tiempo:.6f} segundos en ejecutarse")
        return resultado
    
    return wrapper

# Ejemplo de uso de decoradores
@registrar_llamada
def saludar(nombre):
    """
    Función simple que saluda a alguien.
    """
    return f"¡Hola, {nombre}!"

@medir_tiempo
def fibonacci(n):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 10

    print("Evaluando la implementación...\n")

    # Prueba 1: calcular_potencia
    try:
        assert calcular_potencia(2, 3) == 8
        assert calcular_potencia(5, 0) == 1
        print("✅ Prueba 1 pasada: calcular_potencia funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 1 fallida: calcular_potencia no funciona como se esperaba. Error: {e}")

    # Prueba 2: retornar_multiples_valores
    try:
        resultado = retornar_multiples_valores(10, 5)
        assert isinstance(resultado, tuple)
        assert len(resultado) == 4
        assert resultado == (15, 5, 50, 2)
        print("✅ Prueba 2 pasada: retornar_multiples_valores funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 2 fallida: retornar_multiples_valores no funciona como se esperaba. Error: {e}")

    # Prueba 3: obtener_funcion_filtro
    try:
        filtro = obtener_funcion_filtro()
        assert filtro(2) == True
        assert filtro(3) == False
        print("✅ Prueba 3 pasada: obtener_funcion_filtro funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 3 fallida: obtener_funcion_filtro no funciona como se esperaba. Error: {e}")

    # Prueba 4: aplicar_operacion
    try:
        resultado = aplicar_operacion([1, 2, 3], lambda x: x * 2)
        assert resultado == [2, 4, 6]
        print("✅ Prueba 4 pasada: aplicar_operacion funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 4 fallida: aplicar_operacion no funciona como se esperaba. Error: {e}")

    # Prueba 5: suma_todos
    try:
        assert suma_todos() == 0
        assert suma_todos(1, 2, 3) == 6
        print("✅ Prueba 5 pasada: suma_todos funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 5 fallida: suma_todos no funciona como se esperaba. Error: {e}")

    # Prueba 6: crear_persona
    try:
        persona = crear_persona("Juan", edad=30, profesion="Programador")
        assert persona == {"nombre": "Juan", "edad": 30, "profesion": "Programador"}
        print("✅ Prueba 6 pasada: crear_persona funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 6 fallida: crear_persona no funciona como se esperada. Error: {e}")

    # Prueba 7: crear_incrementador
    try:
        global contador
        contador = 0
        incrementar = crear_incrementador(5)
        assert incrementar() == 5
        assert incrementar() == 10
        assert contador == 10
        print("✅ Prueba 7 pasada: crear_incrementador funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 7 fallida: crear_incrementador no funciona como se esperaba. Error: {e}")

    # Prueba 8: crear_contador_local
    try:
        contador1 = crear_contador_local()
        contador2 = crear_contador_local()
        assert contador1() == 1
        assert contador1() == 2
        assert contador2() == 1
        print("✅ Prueba 8 pasada: crear_contador_local funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 8 fallida: crear_contador_local no funciona como se esperaba. Error: {e}")

    # Prueba 9: registrar_llamada
    try:
        # Clase para duplicar la salida (terminal y captura)
        class TeeOutput:
            def __init__(self, original_stdout):
                self.original_stdout = original_stdout
                self.captura = io.StringIO()
                
            def write(self, mensaje):
                self.original_stdout.write(mensaje)
                self.captura.write(mensaje)
                
            def flush(self):
                self.original_stdout.flush()
                
            def getvalue(self):
                return self.captura.getvalue()
        
        # Crear capturador que muestra en terminal y guarda para verificar
        original_stdout = sys.stdout
        tee = TeeOutput(original_stdout)
        sys.stdout = tee
        
        try:
            print("\n--- Prueba 9: Ejecutando decorador registrar_llamada ---")
            resultado = saludar("Mundo")
        finally:
            # Restaurar stdout original
            sys.stdout = original_stdout
        
        # Obtener lo que se imprimió
        salida = tee.getvalue().strip()
        
        # Verificar el resultado y la salida
        assert resultado == "¡Hola, Mundo!"
        assert "Llamando a saludar" in salida, "No se encontró el mensaje 'Llamando a saludar'"
        assert "Llamada a saludar completada" in salida, "No se encontró el mensaje 'Llamada a saludar completada'"
        print("✅ Prueba 9 pasada: registrar_llamada funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 9 fallida: registrar_llamada no funciona como se esperaba. Error: {e}")

    # Prueba 10: medir_tiempo
    try:
        # Crear capturador que muestra en terminal y guarda para verificar
        original_stdout = sys.stdout
        tee = TeeOutput(original_stdout)
        sys.stdout = tee
        
        try:
            print("\n--- Prueba 10: Ejecutando decorador medir_tiempo ---")
            resultado = fibonacci(5)
        finally:
            # Restaurar stdout original
            sys.stdout = original_stdout
        
        # Obtener lo que se imprimió
        salida = tee.getvalue().strip()
        
        # Verificar el resultado y la salida
        assert resultado == 5
        assert "La función fibonacci tardó" in salida, "No se encontró el mensaje 'La función fibonacci tardó'"
        assert "segundos en ejecutarse" in salida, "No se encontró el mensaje 'segundos en ejecutarse'"
        print("✅ Prueba 10 pasada: medir_tiempo funciona correctamente")
        puntuacion += 1
    except Exception as e:
        print(f"❌ Prueba 10 fallida: medir_tiempo no funciona como se esperada. Error: {e}")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de las funciones avanzadas en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
    