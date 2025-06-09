# Solucionario: Actividad Ampliada de Constantes en Python

import re

# Constantes predefinidas (no modificar)
PI = 3.14159
GRAVEDAD = 9.8
DIAS_SEMANA = 7
NOMBRE_CURSO = "PYTHON PROGRAMMING"
ES_LENGUAJE_COMPILADO = False

# Constantes creadas por el estudiante
VELOCIDAD_LUZ = 299792458  # Velocidad de la luz en m/s
CARGA_ELECTRON = 1.602176634e-19  # Carga del electrón en coulombs
CERO_ABSOLUTO = -273.15  # Cero absoluto en grados Celsius

def calcular_area_circulo(radio):
    return PI * radio ** 2

def calcular_energia_potencial(masa, altura):
    return masa * GRAVEDAD * altura

def obtener_dias_en_semanas(semanas):
    return semanas * DIAS_SEMANA

def formatear_nombre_curso():
    return NOMBRE_CURSO.lower().replace(' ', '_')

def es_lenguaje_interpretado():
    return not ES_LENGUAJE_COMPILADO

def calcular_energia_electron(velocidad):
    masa_electron = 9.1093837e-31  # kg
    return 0.5 * masa_electron * velocidad**2 / CARGA_ELECTRON

def convertir_celsius_a_kelvin(temp_celsius):
    return temp_celsius - CERO_ABSOLUTO

def es_nombre_constante_valido(nombre):
    return re.match(r'^[A-Z][A-Z_0-9]*$', nombre) is not None

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando la implementación...\n")

    # Prueba 1: calcular_area_circulo
    try:
        assert abs(calcular_area_circulo(5) - 78.53975) < 0.0001
        print("✅ Prueba 1 pasada: calcular_area_circulo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: calcular_area_circulo no funciona como se esperaba")

    # Prueba 2: calcular_energia_potencial
    try:
        assert calcular_energia_potencial(10, 5) == 490
        print("✅ Prueba 2 pasada: calcular_energia_potencial funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: calcular_energia_potencial no funciona como se esperaba")

    # Prueba 3: obtener_dias_en_semanas
    try:
        assert obtener_dias_en_semanas(3) == 21
        print("✅ Prueba 3 pasada: obtener_dias_en_semanas funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: obtener_dias_en_semanas no funciona como se esperaba")

    # Prueba 4: formatear_nombre_curso
    try:
        assert formatear_nombre_curso() == "python_programming"
        print("✅ Prueba 4 pasada: formatear_nombre_curso funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: formatear_nombre_curso no funciona como se esperaba")

    # Prueba 5: es_lenguaje_interpretado
    try:
        assert es_lenguaje_interpretado() == True
        print("✅ Prueba 5 pasada: es_lenguaje_interpretado funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: es_lenguaje_interpretado no funciona como se esperaba")

    # Prueba 6: calcular_energia_electron
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
