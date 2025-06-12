# Solucionario: Actividad de Operaciones con Sets en Python


def crear_set(elementos):
    """
    Crea y retorna un set con los elementos dados.
    """
    return set(elementos)

def agregar_elemento(conjunto, elemento):
    """
    Agrega un elemento al set y retorna el set actualizado.
    """
    conjunto.add(elemento)
    return conjunto

def eliminar_elemento(conjunto, elemento):
    """
    Elimina un elemento del set si existe.
    Si el elemento no existe, no debe lanzar un error.
    Retorna el set actualizado.
    """
    conjunto.discard(elemento)
    return conjunto

def es_subconjunto(subconjunto, superconjunto):
    """
    Retorna True si subconjunto es un subconjunto de superconjunto, False en caso contrario.
    """
    return subconjunto.issubset(superconjunto)

def union_sets(set1, set2):
    """
    Retorna la unión de set1 y set2.
    """
    return set1.union(set2)
    # Alternativa: return set1 | set2

def interseccion_sets(set1, set2):
    """
    Retorna la intersección de set1 y set2.
    """
    return set1.intersection(set2)
    # Alternativa: return set1 & set2

def diferencia_sets(set1, set2):
    """
    Retorna la diferencia entre set1 y set2 (elementos en set1 pero no en set2).
    """
    return set1.difference(set2)
    # Alternativa: return set1 - set2

def diferencia_simetrica_sets(set1, set2):
    """
    Retorna la diferencia simétrica entre set1 y set2.
    """
    return set1.symmetric_difference(set2)
    # Alternativa: return set1 ^ set2

def eliminar_duplicados(lista):
    """
    Elimina los duplicados de la lista dada y retorna una nueva lista sin duplicados.
    El orden de los elementos en la lista resultante no importa.
    """
    return list(set(lista))

def crear_frozenset(elementos):
    """
    Crea y retorna un frozenset con los elementos dados.
    """
    return frozenset(elementos)


print("Este es el solucionario para la Actividad de Operaciones con Sets en Python.")
print("Los estudiantes deben intentar resolver los ejercicios por sí mismos antes de consultar estas soluciones.")
print("Los profesores pueden usar este solucionario para verificar las respuestas de los estudiantes o proporcionar orientación adicional.")
