# Actividad: Uso Específico de Booleanos en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando True, False, and, or, o not.
3. No modifiques nada más en el código.
4. Una vez que hayas completado todas las funciones, ejecuta este script.
5. El script evaluará tu implementación y te dará una puntuación.

Conceptos clave a utilizar:
- Valores booleanos (True y False)
- Operadores lógicos (and, or, not)

¡Buena suerte!
"""

def operacion_and():
    """
    Completa la operación para que retorne True solo si ambos valores son True.
    """
    return True ___ True

def operacion_or():
    """
    Completa la operación para que retorne True si al menos uno de los valores es True.
    """
    return False ___ True

def operacion_not():
    """
    Completa la operación para que invierta el valor booleano dado.
    """
    return ___ False

def combinacion_and_or():
    """
    Completa la operación para que retorne True si (a y b) o c son True.
    """
    a, b, c = True, False, True
    return (a ___ b) ___ c

def combinacion_not_and():
    """
    Completa la operación para que retorne True si a es True y b no es True.
    """
    a, b = True, False
    return a ___ (___ b)

def tres_condiciones():
    """
    Completa la operación para que retorne True solo si las tres condiciones son True.
    """
    return True ___ True ___ True

def al_menos_dos_true():
    """
    Completa la operación para que retorne True si al menos dos de las tres condiciones son True.
    """
    a, b, c = True, False, True
    return (a ___ b) ___ (b ___ c) ___ (a ___ c)

def exactamente_dos_true():
    """
    Completa la operación para que retorne True si exactamente dos de las tres condiciones son True.
    """
    a, b, c = True, False, True
    return (a ___ b ___ (___c)) ___ (a ___ c ___ (___b)) ___ (b ___ c ___ (___a))

# Función de verificación
def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando la implementación...\n")

    # Prueba 1: operacion_and
    try:
        assert operacion_and() == True
        print("✅ Prueba 1 pasada: operacion_and funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: operacion_and no funciona como se esperaba")

    # Prueba 2: operacion_or
    try:
        assert operacion_or() == True
        print("✅ Prueba 2 pasada: operacion_or funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: operacion_or no funciona como se esperaba")

    # Prueba 3: operacion_not
    try:
        assert operacion_not() == True
        print("✅ Prueba 3 pasada: operacion_not funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: operacion_not no funciona como se esperaba")

    # Prueba 4: combinacion_and_or
    try:
        assert combinacion_and_or() == True
        print("✅ Prueba 4 pasada: combinacion_and_or funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: combinacion_and_or no funciona como se esperaba")

    # Prueba 5: combinacion_not_and
    try:
        assert combinacion_not_and() == True
        print("✅ Prueba 5 pasada: combinacion_not_and funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: combinacion_not_and no funciona como se esperaba")

    # Prueba 6: tres_condiciones
    try:
        assert tres_condiciones() == True
        print("✅ Prueba 6 pasada: tres_condiciones funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: tres_condiciones no funciona como se esperaba")

    # Prueba 7: al_menos_dos_true
    try:
        assert al_menos_dos_true() == True
        print("✅ Prueba 7 pasada: al_menos_dos_true funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: al_menos_dos_true no funciona como se esperaba")

    # Prueba 8: exactamente_dos_true
    try:
        assert exactamente_dos_true() == True
        print("✅ Prueba 8 pasada: exactamente_dos_true funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: exactamente_dos_true no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un excelente manejo de los booleanos y operadores lógicos en Python.")
    else:
        print("\nAlgunas funciones necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
