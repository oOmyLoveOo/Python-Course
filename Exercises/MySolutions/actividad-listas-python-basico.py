# Actividad: Operaciones Básicas con Listas en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando las operaciones de lista apropiadas.
3. No modifiques los nombres de las funciones existentes.
4. Una vez que hayas completado todo, ejecuta este script.

¡Buena suerte!
"""

def crear_lista_numeros(n):
    """
    Crea una lista de números del 1 al n (inclusive).
    """
    return ___

def obtener_elemento(lista, indice):
    """
    Devuelve el elemento en la posición 'indice' de la lista.
    Si el índice no existe, devuelve None.
    """
    if ___:
        return ___
    return None

def contar_elementos(lista, elemento):
    """
    Cuenta cuántas veces aparece 'elemento' en la lista.
    """
    return ___

def agregar_elemento(lista, elemento):
    """
    Agrega 'elemento' al final de la lista.
    """
    ___
    return lista

def eliminar_elemento(lista, elemento):
    """
    Elimina la primera aparición de 'elemento' en la lista.
    Si el elemento no está en la lista, no la modifica.
    """
    if ___:
        ___
    return lista

def invertir_lista(lista):
    """
    Invierte el orden de los elementos en la lista.
    """
    ___
    return lista

def concatenar_listas(lista1, lista2):
    """
    Concatena lista2 al final de lista1.
    """
    ___
    return lista1

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 7

    print("Evaluando la implementación...\n")

    # Prueba 1: crear_lista_numeros
    try:
        assert crear_lista_numeros(5) == [1, 2, 3, 4, 5]
        print("✅ Prueba 1 pasada: crear_lista_numeros funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: crear_lista_numeros no funciona como se esperaba")

    # Prueba 2: obtener_elemento
    try:
        assert obtener_elemento([1, 2, 3], 1) == 2
        assert obtener_elemento([1, 2, 3], 3) == None
        print("✅ Prueba 2 pasada: obtener_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: obtener_elemento no funciona como se esperaba")

    # Prueba 3: contar_elementos
    try:
        assert contar_elementos([1, 2, 2, 3, 2], 2) == 3
        print("✅ Prueba 3 pasada: contar_elementos funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: contar_elementos no funciona como se esperaba")

    # Prueba 4: agregar_elemento
    try:
        assert agregar_elemento([1, 2, 3], 4) == [1, 2, 3, 4]
        print("✅ Prueba 4 pasada: agregar_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: agregar_elemento no funciona como se esperaba")

    # Prueba 5: eliminar_elemento
    try:
        assert eliminar_elemento([1, 2, 2, 3], 2) == [1, 2, 3]
        assert eliminar_elemento([1, 2, 3], 4) == [1, 2, 3]
        print("✅ Prueba 5 pasada: eliminar_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: eliminar_elemento no funciona como se esperaba")

    # Prueba 6: invertir_lista
    try:
        assert invertir_lista([1, 2, 3]) == [3, 2, 1]
        print("✅ Prueba 6 pasada: invertir_lista funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: invertir_lista no funciona como se esperaba")

    # Prueba 7: concatenar_listas
    try:
        assert concatenar_listas([1, 2], [3, 4]) == [1, 2, 3, 4]
        print("✅ Prueba 7 pasada: concatenar_listas funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: concatenar_listas no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de las operaciones básicas con listas en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
