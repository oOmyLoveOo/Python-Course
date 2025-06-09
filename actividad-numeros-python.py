
"""
Instrucciones para el alumno:

1. Lee cuidadosamente los comentarios en cada función.
2. Implementa cada función según las instrucciones proporcionadas.
3. Utiliza los conceptos aprendidos sobre números en Python para completar las funciones.
4. Una vez que hayas implementado todas las funciones, ejecuta este script.
5. El script evaluará tu implementación y te dará una puntuación.
6. Si obtienes una puntuación perfecta, sube el documento a la plataforma.
7. Si no obtienes una puntuación perfecta, revisa tus implementaciones y vuelve a intentarlo.

Conceptos clave a utilizar:
- Números enteros y de punto flotante
- Operaciones aritméticas básicas
- División entera y módulo
- Formato de números grandes
- Asignación múltiple de variables
- Conversión entre tipos numéricos
- Funciones matemáticas como round() y abs()

Nota: La función operacion_enteros(a, b) debe implementar la operación a * b + 10.

¡Buena suerte!
"""

import math

def es_entero(numero):
    # Implementa esta función para verificar si un número es entero
    pass

def suma_flotantes(a, b):
    # Implementa esta función para sumar dos números flotantes
    pass

def division_entera_y_resto(a, b):
    # Implementa esta función para retornar la división entera y el resto
    pass

def formato_numero_grande(numero):
    # Implementa esta función para dar formato legible a un número grande
    pass

def asignacion_multiple():
    # Implementa esta función para asignar múltiples variables en una línea
    pass

def operacion_enteros(a, b):
    # Implementa esta función para realizar la operación a * b + 10
    pass

def conversion_tipos(numero_str):
    # Implementa esta función para convertir entre tipos numéricos
    pass

def redondeo_y_absoluto(numero):
    # Implementa esta función para redondear y obtener el valor absoluto
    pass

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando tu implementación...\n")

    # Prueba 1: es_entero
    try:
        assert es_entero(5) == True
        assert es_entero(5.5) == False
        print("✅ Prueba 1 pasada: es_entero funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: es_entero no funciona como se esperaba")

    # Prueba 2: suma_flotantes
    try:
        assert math.isclose(suma_flotantes(3.14, 2.86), 6.0, rel_tol=1e-9)
        print("✅ Prueba 2 pasada: suma_flotantes funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: suma_flotantes no funciona como se esperaba")

    # Prueba 3: division_entera_y_resto
    try:
        assert division_entera_y_resto(10, 3) == (3, 1)
        print("✅ Prueba 3 pasada: division_entera_y_resto funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: division_entera_y_resto no funciona como se esperaba")

    # Prueba 4: formato_numero_grande
    try:
        assert formato_numero_grande(1000000) == "1_000_000"
        print("✅ Prueba 4 pasada: formato_numero_grande funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: formato_numero_grande no funciona como se esperaba")

    # Prueba 5: asignacion_multiple
    try:
        a, b, c = asignacion_multiple()
        assert (a, b, c) == (1, 2, 3)
        print("✅ Prueba 5 pasada: asignacion_multiple funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: asignacion_multiple no funciona como se esperaba")

    # Prueba 6: operacion_enteros
    try:
        assert operacion_enteros(5, 3) == 25
        print("✅ Prueba 6 pasada: operacion_enteros funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: operacion_enteros no funciona como se esperaba")

    # Prueba 7: conversion_tipos
    try:
        entero, flotante = conversion_tipos("5.5")
        assert entero == 5 and math.isclose(flotante, 5.5, rel_tol=1e-9)
        print("✅ Prueba 7 pasada: conversion_tipos funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: conversion_tipos no funciona como se esperaba")

    # Prueba 8: redondeo_y_absoluto
    try:
        assert redondeo_y_absoluto(-4.6) == (-5, 4.6)
        print("✅ Prueba 8 pasada: redondeo_y_absoluto funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: redondeo_y_absoluto no funciona como se esperada")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Has completado todas las funciones correctamente.")
        print("Toma una captura de pantalla de este resultado y súbela a la plataforma en la tarea correspondiente.")
    else:
        print("\nSigue practicando y vuelve a intentarlo para obtener una puntuación perfecta.")

if __name__ == "__main__":
    verificar_implementacion()

