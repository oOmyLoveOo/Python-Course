# Actividad: Estructuras de Control en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada sección.
2. Completa los espacios marcados con ___ usando la estructura de control o bucle apropiado.
3. No modifiques los nombres de las funciones existentes.
4. Una vez que hayas completado todo, ejecuta este script.

¡Buena suerte!
"""

def es_par_impar(numero):
    """
    Determina si un número es par o impar.
    Retorna "Par" si es par, "Impar" si es impar.
    """
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def calificar_nota(puntuacion):
    """
    Califica una puntuación según la siguiente escala:
    0-59: "Suspenso"
    60-79: "Aprobado"
    80-89: "Notable"
    90-100: "Sobresaliente"
    Para cualquier otro valor: "Puntuación inválida"
    """
    if puntuacion >= 0 and puntuacion <= 59:
        return "Suspenso"
    elif puntuacion >= 60 and puntuacion <= 79:
        return "Aprobado"
    elif puntuacion >= 80 and puntuacion <= 89:
        return "Notable"
    elif puntuacion >= 90 and puntuacion <= 100:
        return "Sobresaliente"
    else:
        return "Puntuación inválida"

def suma_numeros_pares(n):
    """
    Calcula la suma de los números pares del 1 al n (inclusive).
    Usa un bucle while.
    """
    suma = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            suma += i
        i += 1
    return suma

def imprimir_patron(filas):
    """
    Imprime un patrón de asteriscos como el siguiente (para filas=4):
    *
    **
    ***
    ****
    Usa un bucle for.
    """
    for i in range(1, filas + 1):
        print("*" * i)

def encontrar_numero(numero_objetivo):
    """
    Simula un juego de adivinanza.
    Genera números del 1 al 100 hasta encontrar el número objetivo.
    Retorna la cantidad de intentos necesarios.
    Usa un bucle while.
    """
    import random
    intentos = 0
    numero_generado = 0
    
    if numero_generado != numero_objetivo:
        numero_generado = random.randint(1, 100)
        intentos += 1
    
    return intentos

def tabla_multiplicar(n):
    """
    Imprime la tabla de multiplicar del número n del 1 al 10.
    Usa un bucle for.
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def contar_vocales(frase):
    """
    Cuenta la cantidad de cada vocal en la frase.
    Retorna un diccionario con el conteo.
    Usa un bucle for y una estructura if-elif.
    """
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in frase.lower():
        if letra == 'a':
            vocales['a'] += 1
        elif letra == 'e':
            vocales['e'] += 1
        elif letra == 'i':
            vocales['i'] += 1
        elif letra == 'o':
            vocales['o'] += 1
        elif letra == 'u':
            vocales['u'] += 1
    
    return vocales

def fibonacci(n):
    """
    Genera los primeros n números de la secuencia de Fibonacci.
    Retorna una lista con la secuencia.
    Usa un bucle while.
    """
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando la implementación...\n")

    # Prueba 1: es_par_impar
    try:
        assert es_par_impar(4) == "Par" and es_par_impar(7) == "Impar"
        print("✅ Prueba 1 pasada: es_par_impar funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: es_par_impar no funciona como se esperaba")

    # Prueba 2: calificar_nota
    try:
        assert calificar_nota(75) == "Aprobado" and calificar_nota(95) == "Sobresaliente"
        assert calificar_nota(50) == "Suspenso" and calificar_nota(110) == "Puntuación inválida"
        print("✅ Prueba 2 pasada: calificar_nota funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: calificar_nota no funciona como se esperaba")

    # Prueba 3: suma_numeros_pares
    try:
        assert suma_numeros_pares(10) == 30
        print("✅ Prueba 3 pasada: suma_numeros_pares funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: suma_numeros_pares no funciona como se esperaba")

    # Prueba 4: imprimir_patron
    try:
        import io
        import sys
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        imprimir_patron(3)
        sys.stdout = sys.__stdout__
        assert capturedOutput.getvalue() == "*\n**\n***\n"
        print("✅ Prueba 4 pasada: imprimir_patron funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: imprimir_patron no funciona como se esperaba")

    # Prueba 5: encontrar_numero
    try:
        intentos = encontrar_numero(42)
        assert isinstance(intentos, int) and intentos > 0
        print("✅ Prueba 5 pasada: encontrar_numero funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: encontrar_numero no funciona como se esperaba")

    # Prueba 6: tabla_multiplicar
    try:
        import io
        import sys
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        tabla_multiplicar(3)
        sys.stdout = sys.__stdout__
        assert "3 x 1 = 3" in capturedOutput.getvalue() and "3 x 10 = 30" in capturedOutput.getvalue()
        print("✅ Prueba 6 pasada: tabla_multiplicar funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: tabla_multiplicar no funciona como se esperaba")

    # Prueba 7: contar_vocales
    try:
        resultado = contar_vocales("Hola Mundo")
        assert resultado == {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1}
        print("✅ Prueba 7 pasada: contar_vocales funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: contar_vocales no funciona como se esperaba")

    # Prueba 8: fibonacci
    try:
        assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
        print("✅ Prueba 8 pasada: fibonacci funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: fibonacci no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un excelente entendimiento de las estructuras de control en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
