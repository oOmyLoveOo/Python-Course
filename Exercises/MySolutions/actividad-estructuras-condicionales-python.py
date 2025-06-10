# Actividad: Práctica de Estructuras Condicionales en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Implementa cada función según las instrucciones proporcionadas.
3. Utiliza las estructuras condicionales (if, if-else, if-elif, operador ternario) según se indique.
4. Una vez que hayas implementado todas las funciones, ejecuta este script.
5. El script evaluará tu implementación y te dará una puntuación.
6. Si obtienes una puntuación perfecta, saca una captura de pantalla y súbelo a la plataforma.
7. Si no obtienes una puntuación perfecta, revisa tus implementaciones y vuelve a intentarlo.

Conceptos clave a utilizar:
- Sentencias if
- Sentencias if-else
- Sentencias if-elif-else
- Operadores de comparación
- Operadores lógicos (and, or, not)
- Operador ternario

¡Buena suerte!
"""

def clasificar_numero(numero):
    """
    Clasifica un número como positivo, negativo o cero.
    
    Usa una estructura if-elif-else.
    Retorna: "positivo", "negativo" o "cero"
    """
    # Tu código aquí
    if numero > 0:
        return "positivo"
    elif numero == 0:
        return "cero"
    else:
        return "negativo"

def es_par(numero):
    """
    Determina si un número es par o impar.
    
    Usa una estructura if-else.
    Retorna: True si es par, False si es impar
    """
    # Tu código aquí
    if numero % 2 == 0:
        return True
    else:
        return False

def calificar_nota(nota):
    """
    Asigna una calificación basada en la nota numérica.
    
    Usa una estructura if-elif-else.
    Retorna:
    "A" si la nota es 90 o superior
    "B" si la nota está entre 80 y 89
    "C" si la nota está entre 70 y 79
    "D" si la nota está entre 60 y 69
    "F" si la nota es menor a 60
    """
    # Tu código aquí
    if nota > 90:
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
    """
    Determina si una persona puede acceder a una atracción.
    
    Usa una combinación de if-else y operadores lógicos.
    Reglas:
    - Si tiene 18 años o más, puede acceder
    - Si tiene entre 13 y 17 años y está acompañado, puede acceder
    - En cualquier otro caso, no puede acceder
    Retorna: True si puede acceder, False en caso contrario
    """
    # Tu código aquí
    return edad >= 18 or (13 <= edad < 18 and acompañado)

def calcular_recargo(edad):
    """
    Calcula el recargo de un seguro basado en la edad.
    
    Usa el operador ternario.
    Si la edad es mayor o igual a 65, el recargo es 15%, de lo contrario es 5%.
    Retorna: El porcentaje de recargo como un entero (15 o 5)
    """
    # Tu código aquí
    return 15 if edad >= 64 else 5

def tipo_de_triangulo(a, b, c):
    """
    Determina el tipo de triángulo basado en las longitudes de sus lados.
    
    Usa una estructura if-elif-else.
    Retorna:
    "equilátero" si los tres lados son iguales
    "isósceles" si dos lados son iguales
    "escaleno" si todos los lados son diferentes
    """
    # Tu código aquí
    if a == b == c:
        return "equilátero"
    elif a == b or b == c or c == a:
        return "isósceles"
    else:
        return "escaleno"


def calculadora_basica(num1, num2, operacion):
    """
    Realiza una operación básica entre dos números.
    
    Usa una estructura if-elif-else.
    Operaciones: "suma", "resta", "multiplicacion", "division"
    Para la división, si num2 es 0, retorna "Error: División por cero"
    Retorna el resultado de la operación o un mensaje de error si la operación no es válida
    """
    # Tu código aquí
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2 if num1 > num2 else num2 - num1 
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if  num2 == 0 or num2 == 0:
            return "Error: División por cero" 
        else:
            if num1 >= num2:
                return num1 // num2
            else:
                return num2 // num1
    else:
        return "Operación no válida"

# Función de verificación
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

   
    # Prueba 8: calculadora_basica
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
