import math

def es_entero(numero):
    return isinstance(numero, int)

def suma_flotantes(a, b):
    return a + b

def division_entera_y_resto(a, b):
    return a // b, a % b

def formato_numero_grande(numero):
    return f"{numero:_}"

def asignacion_multiple():
    return 1, 2, 3

def operacion_enteros(a, b):
    return a * b + 10  # Corregido: la operación correcta es a * b + 10

def conversion_tipos(numero_str):
    flotante = float(numero_str)
    entero = int(flotante)
    return entero, flotante

def redondeo_y_absoluto(numero):
    return round(numero), abs(numero)

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


