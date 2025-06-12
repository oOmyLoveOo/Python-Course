# Actividad: Operaciones con Tuplas en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando las operaciones de tupla apropiadas.
3. No modifiques los nombres de las funciones existentes.
4. Una vez que hayas completado todo, ejecuta este script.

¡Buena suerte!
"""

def crear_tupla_coordenadas(x, y, z):
    """
    Crea y retorna una tupla con las coordenadas x, y, z.
    
    Ejemplo:
    >>> crear_tupla_coordenadas(1, 2, 3)
    (1, 2, 3)
    """
    return 1, 2, 3

def acceder_elemento(tupla, indice):
    """
    Retorna el elemento de la tupla en la posición 'indice'.
    Si el índice no existe, retorna None.
    
    Ejemplos:
    >>> acceder_elemento((1, 2, 3), 1)
    2
    >>> acceder_elemento((1, 2, 3), 3)
    None
    """
    if -len(tupla) <= indice < len(tupla):
        return tupla[indice]
    return None

def longitud_tupla(tupla):
    """
    Retorna la longitud de la tupla.
    
    Ejemplo:
    >>> longitud_tupla((1, 2, 3, 4))
    4
    """
    return len(tupla)

def concatenar_tuplas(tupla1, tupla2):
    """
    Concatena tupla1 y tupla2, y retorna el resultado.
    
    Ejemplo:
    >>> concatenar_tuplas((1, 2), (3, 4))
    (1, 2, 3, 4)
    """
    return tupla1 + tupla2

def repetir_tupla(tupla, n):
    """
    Repite la tupla 'n' veces y retorna el resultado.
    
    Ejemplo:
    >>> repetir_tupla((1, 2), 3)
    (1, 2, 1, 2, 1, 2)
    """
    return tupla * n

def contar_elemento(tupla, elemento):
    """
    Cuenta cuántas veces aparece 'elemento' en la tupla.
    
    Ejemplo:
    >>> contar_elemento((1, 2, 2, 3, 2), 2)
    3
    """
    return tupla.count(elemento)

def indice_elemento(tupla, elemento):
    """
    Retorna el índice de la primera aparición de 'elemento' en la tupla.
    Si el elemento no está en la tupla, retorna -1.
    
    Ejemplos:
    >>> indice_elemento((1, 2, 3, 2), 2)
    1
    >>> indice_elemento((1, 2, 3), 4)
    -1
    """
    try:
        return tupla.index(elemento)
    except ValueError:
        return -1

def desempaquetar_tupla(tupla):
    """
    Desempaqueta la tupla en tres variables y las retorna.
    Asume que la tupla siempre tendrá 3 elementos.
    
    Ejemplo:
    >>> desempaquetar_tupla((1, 2, 3))
    (1, 2, 3)
    """
    x, y, z = tupla
    return x, y, z

def es_inmutable(tupla):
    """
    Intenta modificar el primer elemento de la tupla.
    Retorna True si genera un error (demostrando inmutabilidad),
    False si se pudo modificar.
    
    Ejemplo:
    >>> es_inmutable((1, 2, 3))
    True
    """
    try:
        tupla[0] = 100
        return False
    except TypeError:
        return True

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 9

    print("Evaluando la implementación...\n")

    # Prueba 1: crear_tupla_coordenadas
    try:
        assert crear_tupla_coordenadas(1, 2, 3) == (1, 2, 3)
        print("✅ Prueba 1 pasada: crear_tupla_coordenadas funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: crear_tupla_coordenadas no funciona como se esperaba")

    # Prueba 2: acceder_elemento
    try:
        assert acceder_elemento((1, 2, 3), 1) == 2
        assert acceder_elemento((1, 2, 3), 3) == None
        print("✅ Prueba 2 pasada: acceder_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: acceder_elemento no funciona como se esperaba")

    # Prueba 3: longitud_tupla
    try:
        assert longitud_tupla((1, 2, 3, 4)) == 4
        print("✅ Prueba 3 pasada: longitud_tupla funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: longitud_tupla no funciona como se esperaba")

    # Prueba 4: concatenar_tuplas
    try:
        assert concatenar_tuplas((1, 2), (3, 4)) == (1, 2, 3, 4)
        print("✅ Prueba 4 pasada: concatenar_tuplas funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: concatenar_tuplas no funciona como se esperaba")

    # Prueba 5: repetir_tupla
    try:
        assert repetir_tupla((1, 2), 3) == (1, 2, 1, 2, 1, 2)
        print("✅ Prueba 5 pasada: repetir_tupla funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: repetir_tupla no funciona como se esperaba")

    # Prueba 6: contar_elemento
    try:
        assert contar_elemento((1, 2, 2, 3, 2), 2) == 3
        print("✅ Prueba 6 pasada: contar_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: contar_elemento no funciona como se esperaba")

    # Prueba 7: indice_elemento
    try:
        assert indice_elemento((1, 2, 3, 2), 2) == 1
        assert indice_elemento((1, 2, 3), 4) == -1
        print("✅ Prueba 7 pasada: indice_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: indice_elemento no funciona como se esperaba")

    # Prueba 8: desempaquetar_tupla
    try:
        assert desempaquetar_tupla((1, 2, 3)) == (1, 2, 3)
        print("✅ Prueba 8 pasada: desempaquetar_tupla funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: desempaquetar_tupla no funciona como se esperaba")

    # Prueba 9: es_inmutable
    try:
        assert es_inmutable((1, 2, 3)) == True
        print("✅ Prueba 9 pasada: es_inmutable funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 9 fallida: es_inmutable no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de las operaciones con tuplas en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()