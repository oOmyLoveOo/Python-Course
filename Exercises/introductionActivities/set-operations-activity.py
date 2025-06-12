# Actividad: Operaciones con Sets en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando las operaciones de set apropiadas.
3. No modifiques los nombres de las funciones existentes.
4. Una vez que hayas completado todo, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

def crear_set(elementos):
    """
    Crea y retorna un set con los elementos dados.
    
    Ejemplo de uso:
    >>> crear_set([1, 2, 3, 3, 4])
    {1, 2, 3, 4}
    """
    return set(elementos)

def agregar_elemento(conjunto, elemento):
    """
    Agrega un elemento al set y retorna el set actualizado.
    
    Ejemplo de uso:
    >>> s = {1, 2, 3}
    >>> agregar_elemento(s, 4)
    {1, 2, 3, 4}
    """
    conjunto.add(elemento)
    return conjunto

def eliminar_elemento(conjunto, elemento):
    """
    Elimina un elemento del set si existe.
    Si el elemento no existe, no debe lanzar un error.
    Retorna el set actualizado.
    
    Ejemplo de uso:
    >>> s = {1, 2, 3}
    >>> eliminar_elemento(s, 2)
    {1, 3}
    >>> eliminar_elemento(s, 4)  # No lanza error
    {1, 3}
    """
    conjunto.discard(elemento)
    return conjunto

def es_subconjunto(subconjunto, superconjunto):
    """
    Retorna True si subconjunto es un subconjunto de superconjunto, False en caso contrario.
    
    Ejemplo de uso:
    >>> es_subconjunto({1, 2}, {1, 2, 3, 4})
    True
    >>> es_subconjunto({1, 5}, {1, 2, 3, 4})
    False
    """
    return True if subconjunto.issubset(superconjunto) else False

def union_sets(set1, set2):
    """
    Retorna la unión de set1 y set2.
    
    Ejemplo de uso:
    >>> union_sets({1, 2, 3}, {3, 4, 5})
    {1, 2, 3, 4, 5}
    """
    set1.union(set2)
    return set1.union(set2)

def interseccion_sets(set1, set2):
    """
    Retorna la intersección de set1 y set2.
    
    Ejemplo de uso:
    >>> interseccion_sets({1, 2, 3, 4}, {3, 4, 5, 6})
    {3, 4}
    """
    interseccion = set1.intersection(set2)
    return interseccion

def diferencia_sets(set1, set2):
    """
    Retorna la diferencia entre set1 y set2 (elementos en set1 pero no en set2).
    
    Ejemplo de uso:
    >>> diferencia_sets({1, 2, 3, 4}, {3, 4, 5, 6})
    {1, 2}
    """
    difference = set1.difference(set2)
    return difference

def diferencia_simetrica_sets(set1, set2):
    """
    Retorna la diferencia simétrica entre set1 y set2.
    
    Ejemplo de uso:
    >>> diferencia_simetrica_sets({1, 2, 3, 4}, {3, 4, 5, 6})
    {1, 2, 5, 6}
    """
    diff = set1.symmetric_difference(set2)
    return diff

def eliminar_duplicados(lista):
    """
    Elimina los duplicados de la lista dada y retorna una nueva lista sin duplicados.
    El orden de los elementos en la lista resultante no importa.
    
    Ejemplo de uso:
    >>> eliminar_duplicados([1, 2, 2, 3, 4, 3, 5])
    [1, 2, 3, 4, 5]
    """
    return list(set(lista))

def crear_frozenset(elementos):
    """
    Crea y retorna un frozenset con los elementos dados.
    
    Ejemplo de uso:
    >>> crear_frozenset([1, 2, 3, 3, 4])
    frozenset({1, 2, 3, 4})
    """
    frozen = frozenset(elementos)
    return frozen

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 10

    print("Evaluando la implementación...\n")

    # Prueba 1: crear_set
    try:
        assert crear_set([1, 2, 3, 3, 4]) == {1, 2, 3, 4}
        print("✅ Prueba 1 pasada: crear_set funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: crear_set no funciona como se esperaba")

    # Prueba 2: agregar_elemento
    try:
        s = {1, 2, 3}
        assert agregar_elemento(s, 4) == {1, 2, 3, 4}
        print("✅ Prueba 2 pasada: agregar_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: agregar_elemento no funciona como se esperaba")

    # Prueba 3: eliminar_elemento
    try:
        s = {1, 2, 3}
        assert eliminar_elemento(s, 2) == {1, 3}
        assert eliminar_elemento(s, 4) == {1, 3}
        print("✅ Prueba 3 pasada: eliminar_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: eliminar_elemento no funciona como se esperaba")

    # Prueba 4: es_subconjunto
    try:
        assert es_subconjunto({1, 2}, {1, 2, 3, 4}) == True
        assert es_subconjunto({1, 5}, {1, 2, 3, 4}) == False
        print("✅ Prueba 4 pasada: es_subconjunto funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: es_subconjunto no funciona como se esperaba")

    # Prueba 5: union_sets
    try:
        assert union_sets({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}
        print("✅ Prueba 5 pasada: union_sets funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: union_sets no funciona como se esperaba")

    # Prueba 6: interseccion_sets
    try:
        assert interseccion_sets({1, 2, 3, 4}, {3, 4, 5, 6}) == {3, 4}
        print("✅ Prueba 6 pasada: interseccion_sets funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: interseccion_sets no funciona como se esperaba")

    # Prueba 7: diferencia_sets
    try:
        assert diferencia_sets({1, 2, 3, 4}, {3, 4, 5, 6}) == {1, 2}
        print("✅ Prueba 7 pasada: diferencia_sets funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: diferencia_sets no funciona como se esperaba")

    # Prueba 8: diferencia_simetrica_sets
    try:
        assert diferencia_simetrica_sets({1, 2, 3, 4}, {3, 4, 5, 6}) == {1, 2, 5, 6}
        print("✅ Prueba 8 pasada: diferencia_simetrica_sets funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: diferencia_simetrica_sets no funciona como se esperaba")

    # Prueba 9: eliminar_duplicados
    try:
        assert set(eliminar_duplicados([1, 2, 2, 3, 4, 3, 5])) == {1, 2, 3, 4, 5}
        print("✅ Prueba 9 pasada: eliminar_duplicados funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 9 fallida: eliminar_duplicados no funciona como se esperaba")

    # Prueba 10: crear_frozenset
    try:
        assert crear_frozenset([1, 2, 3, 3, 4]) == frozenset({1, 2, 3, 4})
        print("✅ Prueba 10 pasada: crear_frozenset funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 10 fallida: crear_frozenset no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de las operaciones con sets en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
