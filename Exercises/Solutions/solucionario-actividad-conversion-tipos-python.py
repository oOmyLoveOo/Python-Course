# Solucionario-Actividad-Conversion-Tipos-Python



def convertir_a_entero(valor):
    """
    Convierte el valor dado a un entero y lo retorna.
    Si no es posible, retorna None.
    
    Ejemplos:
    >>> convertir_a_entero("10")
    10
    >>> convertir_a_entero("abc")
    None
    """
    try:
        return int(valor)
    except ValueError:
        return None

def convertir_a_float(valor):
    """
    Convierte el valor dado a un float y lo retorna.
    Si no es posible, retorna None.
    
    Ejemplos:
    >>> convertir_a_float("3.14")
    3.14
    >>> convertir_a_float("10")
    10.0
    >>> convertir_a_float("abc")
    None
    """
    try:
        return float(valor)
    except ValueError:
        return None

def convertir_a_boolean(valor):
    """
    Convierte el valor dado a un booleano y lo retorna.
    
    Ejemplos:
    >>> convertir_a_boolean(1)
    True
    >>> convertir_a_boolean(0)
    False
    >>> convertir_a_boolean("True")
    True
    """
    return bool(valor)

def convertir_a_string(valor):
    """
    Convierte el valor dado a una string y la retorna.
    
    Ejemplos:
    >>> convertir_a_string(123)
    "123"
    >>> convertir_a_string(3.14)
    "3.14"
    >>> convertir_a_string(True)
    "True"
    """
    return str(valor)

def convertir_a_lista(valor):
    """
    Convierte el valor dado a una lista y la retorna.
    Si el valor es una string, cada carácter debe ser un elemento de la lista.
    
    Ejemplos:
    >>> convertir_a_lista("hello")
    ['h', 'e', 'l', 'l', 'o']
    >>> convertir_a_lista((1, 2, 3))
    [1, 2, 3]
    """
    return list(valor)

def convertir_a_tupla(valor):
    """
    Convierte el valor dado a una tupla y la retorna.
    
    Ejemplos:
    >>> convertir_a_tupla([1, 2, 3])
    (1, 2, 3)
    >>> convertir_a_tupla("abc")
    ('a', 'b', 'c')
    """
    return tuple(valor)

def convertir_a_set(valor):
    """
    Convierte el valor dado a un set y lo retorna.
    
    Ejemplos:
    >>> convertir_a_set([1, 2, 2, 3])
    {1, 2, 3}
    >>> convertir_a_set("hello")
    {'h', 'e', 'l', 'o'}
    """
    return set(valor)

def convertir_a_diccionario(claves, valores):
    """
    Convierte las listas de claves y valores a un diccionario y lo retorna.
    
    Ejemplo:
    >>> convertir_a_diccionario(['a', 'b', 'c'], [1, 2, 3])
    {'a': 1, 'b': 2, 'c': 3}
    """
    return dict(zip(claves, valores))

def conversion_implicita(a, b):
    """
    Realiza una suma que implica una conversión implícita y retorna el resultado.
    
    Ejemplo:
    >>> conversion_implicita(3, 4.5)
    7.5
    """
    return a + b

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 9

    print("Evaluando la implementación...\n")

    # Prueba 1: convertir_a_entero
    try:
        assert convertir_a_entero("10") == 10
        assert convertir_a_entero("abc") == None
        print("✅ Prueba 1 pasada: convertir_a_entero funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: convertir_a_entero no funciona como se esperaba")

    # Prueba 2: convertir_a_float
    try:
        assert convertir_a_float("3.14") == 3.14
        assert convertir_a_float("10") == 10.0
        assert convertir_a_float("abc") == None
        print("✅ Prueba 2 pasada: convertir_a_float funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: convertir_a_float no funciona como se esperaba")

    # Prueba 3: convertir_a_boolean
    try:
        assert convertir_a_boolean(1) == True
        assert convertir_a_boolean(0) == False
        assert convertir_a_boolean("True") == True
        print("✅ Prueba 3 pasada: convertir_a_boolean funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: convertir_a_boolean no funciona como se esperaba")

    # Prueba 4: convertir_a_string
    try:
        assert convertir_a_string(123) == "123"
        assert convertir_a_string(3.14) == "3.14"
        assert convertir_a_string(True) == "True"
        print("✅ Prueba 4 pasada: convertir_a_string funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: convertir_a_string no funciona como se esperaba")

    # Prueba 5: convertir_a_lista
    try:
        assert convertir_a_lista("hello") == ['h', 'e', 'l', 'l', 'o']
        assert convertir_a_lista((1, 2, 3)) == [1, 2, 3]
        print("✅ Prueba 5 pasada: convertir_a_lista funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: convertir_a_lista no funciona como se esperaba")

    # Prueba 6: convertir_a_tupla
    try:
        assert convertir_a_tupla([1, 2, 3]) == (1, 2, 3)
        assert convertir_a_tupla("abc") == ('a', 'b', 'c')
        print("✅ Prueba 6 pasada: convertir_a_tupla funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: convertir_a_tupla no funciona como se esperaba")

    # Prueba 7: convertir_a_set
    try:
        assert convertir_a_set([1, 2, 2, 3]) == {1, 2, 3}
        assert convertir_a_set("hello") == {'h', 'e', 'l', 'o'}
        print("✅ Prueba 7 pasada: convertir_a_set funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: convertir_a_set no funciona como se esperaba")

    # Prueba 8: convertir_a_diccionario
    try:
        assert convertir_a_diccionario(['a', 'b', 'c'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}
        print("✅ Prueba 8 pasada: convertir_a_diccionario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: convertir_a_diccionario no funciona como se esperaba")

    # Prueba 9: conversion_implicita
    try:
        assert conversion_implicita(3, 4.5) == 7.5
        print("✅ Prueba 9 pasada: conversion_implicita funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 9 fallida: conversion_implicita no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de la conversión de tipos en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
