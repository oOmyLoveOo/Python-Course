# Solucionario: Práctica de Operadores Aritméticos en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def division_entera(a, b):
    return a // b

def modulo(a, b):
    return a % b

def potencia(base, exponente):
    return base ** exponente

def operacion_combinada(a, b, c, d):
    return (a + b) * c - d

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando tu implementación...\n")

    # Prueba 1: suma
    try:
        assert suma(5, 3) == 8
        print("✅ Prueba 1 pasada: suma funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: suma no funciona como se esperaba")

    # Prueba 2: resta
    try:
        assert resta(10, 4) == 6
        print("✅ Prueba 2 pasada: resta funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: resta no funciona como se esperaba")

    # Prueba 3: multiplicación
    try:
        assert multiplicacion(6, 7) == 42
        print("✅ Prueba 3 pasada: multiplicación funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: multiplicación no funciona como se esperaba")

    # Prueba 4: división
    try:
        assert division(20, 4) == 5.0
        print("✅ Prueba 4 pasada: división funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: división no funciona como se esperaba")

    # Prueba 5: división entera
    try:
        assert division_entera(22, 5) == 4
        print("✅ Prueba 5 pasada: división entera funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: división entera no funciona como se esperaba")

    # Prueba 6: módulo
    try:
        assert modulo(17, 3) == 2
        print("✅ Prueba 6 pasada: módulo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: módulo no funciona como se esperaba")

    # Prueba 7: potencia
    try:
        assert potencia(2, 4) == 16
        print("✅ Prueba 7 pasada: potencia funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: potencia no funciona como se esperaba")

    # Prueba 8: operación combinada
    try:
        assert operacion_combinada(2, 3, 4, 5) == 15
        print("✅ Prueba 8 pasada: operación combinada funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: operación combinada no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están implementadas correctamente.")
        print("Has demostrado un buen entendimiento de los operadores aritméticos en Python.")
    else:
        print("\nAlgunas funciones necesitan revisión. ¡Sigue practicando!")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()

