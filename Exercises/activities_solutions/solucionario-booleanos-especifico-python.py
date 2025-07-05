def operacion_and():
    return True and True

def operacion_or():
    return False or True

def operacion_not():
    return not False

def combinacion_and_or():
    a, b, c = True, False, True
    return (a and b) or c

def combinacion_not_and():
    a, b = True, False
    return a and (not b)

def tres_condiciones():
    return True and True and True

def al_menos_dos_true():
    a, b, c = True, False, True
    return (a and b) or (b and c) or (a and c)

def exactamente_dos_true():
    a, b, c = True, False, True
    return (a and b and (not c)) or (a and c and (not b)) or (b and c and (not a))

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
