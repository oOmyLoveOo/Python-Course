# Actividad Ampliada: Uso y Creación de Constantes en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada sección.
2. Completa los espacios marcados con ___ usando el valor o operación apropiada.
3. Crea tus propias constantes donde se te indique, siguiendo las convenciones de nombrado.
4. No modifiques los nombres de las constantes existentes ni de las funciones.
5. Una vez que hayas completado todo, ejecuta este script.

¡Buena suerte!
"""

import re

# Constantes predefinidas (no modificar)
PI = 3.14159
GRAVEDAD = 9.8
DIAS_SEMANA = 7
NOMBRE_CURSO = "PYTHON PROGRAMMING"
ES_LENGUAJE_COMPILADO = False

# Crea tus propias constantes aquí (al menos 3)
LIGHT = 299792458  # Velocidad de la luz en m/s
COULOMBS = 1.602176634e-19  # Carga del electrón en coulombs
CELSIUS = -273.15  # Cero absoluto en grados Celsius

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo usando la constante PI.
    Fórmula: área = PI * radio^2
    """
    return PI * radio ** 2

def calcular_energia_potencial(masa, altura):
    """
    Calcula la energía potencial usando la constante GRAVEDAD.
    Fórmula: energía = masa * GRAVEDAD * altura
    """
    return masa * GRAVEDAD * altura

def obtener_dias_en_semanas(semanas):
    """
    Calcula el número total de días en un número dado de semanas.
    """
    return semanas * DIAS_SEMANA

def formatear_nombre_curso():
    """
    Formatea el nombre del curso en minúsculas y reemplaza espacios por guiones bajos.
    """
    return NOMBRE_CURSO.lower().replace(' ', '_')

def es_lenguaje_interpretado():
    """
    Retorna el opuesto del valor de ES_LENGUAJE_COMPILADO.
    """
    return not ES_LENGUAJE_COMPILADO

def calcular_energia_electron(velocidad):
    """
    Calcula la energía cinética de un electrón.
    Utiliza las constantes que has creado.
    Fórmula: E = (1/2) * m * v^2
    """
    masa_electron = 9.1093837e-31  # kg
    return 0.5 * masa_electron * velocidad**2

def convertir_celsius_a_kelvin(temp_celsius):
    """
    Convierte una temperatura de Celsius a Kelvin.
    Utiliza la constante que has creado para el cero absoluto.
    Fórmula: K = C - cero_absoluto
    """
    return temp_celsius - CELSIUS

def es_nombre_constante_valido(nombre):
    """
    Verifica si el nombre de una constante es válido.
    Debe estar en mayúsculas y puede contener guiones bajos.
    """
    return re.match(r'^[A-Z][A-Z_0-9]*$', nombre) is not None

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando la implementación...\n")

    # Pruebas para las funciones originales
    # ... [Las pruebas originales permanecen iguales] ...

    try:
        energia = calcular_energia_electron(1000000)
        esperado = 2.8428150513147483
        assert abs(energia - esperado) < 1e-10
        print(f"✅ Prueba 6 pasada: calcular_energia_electron funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: calcular_energia_electron no funciona como se esperaba")
        print(f"   Resultado: {energia:.10e}, Esperado: {esperado:.10e}")

    # Prueba 7: convertir_celsius_a_kelvin
    try:
        assert abs(convertir_celsius_a_kelvin(0) - 273.15) < 0.01
        print("✅ Prueba 7 pasada: convertir_celsius_a_kelvin funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: convertir_celsius_a_kelvin no funciona como se esperaba")

    # Prueba 8: Verificar nombres de constantes creadas por el estudiante
    constantes_creadas = [name for name, value in globals().items() if name.isupper() and name not in ['PI', 'GRAVEDAD', 'DIAS_SEMANA', 'NOMBRE_CURSO', 'ES_LENGUAJE_COMPILADO']]
    if len(constantes_creadas) >= 3 and all(es_nombre_constante_valido(name) for name in constantes_creadas):
        print("✅ Prueba 8 pasada: Constantes creadas correctamente")
        puntuacion += 1
    else:
        print("❌ Prueba 8 fallida: Problemas con las constantes creadas")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones y constantes están correctamente implementadas.")
        print("Has demostrado un excelente entendimiento del uso y creación de constantes en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
