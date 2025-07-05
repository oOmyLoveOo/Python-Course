def clasificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

def es_par(numero):
    return numero % 2 == 0

def calificar_nota(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

def verificar_acceso(edad, acompañado):
    return edad >= 18 or (13 <= edad < 18 and acompañado)

def calcular_recargo(edad):
    return 15 if edad >= 65 else 5

def tipo_de_triangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or b == c or a == c:
        return "isósceles"
    else:
        return "escaleno"


def calculadora_basica(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return "Error: División por cero" if num2 == 0 else num1 / num2
    else:
        return "Operación no válida"

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 7

    print("Evaluando la implementación...\n")

    # Prueba 1: clasificar_numero
    try:
        assert clasificar_numero(5) == "positivo"
        assert clasificar_numero(-3) == "negativo"
        assert clasificar_numero(0) == "cero"
        print("✅ Prueba 1 pasada: clasificar_numero funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: clasificar_numero no funciona como se esperaba")

    # Prueba 2: es_par
    try:
        assert es_par(4) == True
        assert es_par(7) == False
        print("✅ Prueba 2 pasada: es_par funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: es_par no funciona como se esperaba")

    # Prueba 3: calificar_nota
    try:
        assert calificar_nota(95) == "A"
        assert calificar_nota(85) == "B"
        assert calificar_nota(75) == "C"
        assert calificar_nota(65) == "D"
        assert calificar_nota(55) == "F"
        print("✅ Prueba 3 pasada: calificar_nota funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: calificar_nota no funciona como se esperaba")

    # Prueba 4: verificar_acceso
    try:
        assert verificar_acceso(20, False) == True
        assert verificar_acceso(15, True) == True
        assert verificar_acceso(15, False) == False
        assert verificar_acceso(12, True) == False
        print("✅ Prueba 4 pasada: verificar_acceso funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: verificar_acceso no funciona como se esperaba")

    # Prueba 5: calcular_recargo
    try:
        assert calcular_recargo(70) == 15
        assert calcular_recargo(50) == 5
        print("✅ Prueba 5 pasada: calcular_recargo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: calcular_recargo no funciona como se esperaba")

    # Prueba 6: tipo_de_triangulo
    try:
        assert tipo_de_triangulo(5, 5, 5) == "equilátero"
        assert tipo_de_triangulo(5, 5, 6) == "isósceles"
        assert tipo_de_triangulo(3, 4, 5) == "escaleno"
        print("✅ Prueba 6 pasada: tipo_de_triangulo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: tipo_de_triangulo no funciona como se esperaba")

    
    # Prueba 7: calculadora_basica
    try:
        assert calculadora_basica(5, 3, "suma") == 8
        assert calculadora_basica(5, 3, "resta") == 2
        assert calculadora_basica(5, 3, "multiplicacion") == 15
        assert calculadora_basica(6, 3, "division") == 2
        assert calculadora_basica(5, 0, "division") == "Error: División por cero"
        assert calculadora_basica(5, 3, "potencia") == "Operación no válida"
        print("✅ Prueba 7 pasada: calculadora_basica funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: calculadora_basica no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un excelente manejo de las estructuras condicionales en Python.")
    else:
        print("\nAlgunas funciones necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
