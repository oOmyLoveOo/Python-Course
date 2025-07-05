# Solucionario: Actividad de Operaciones con Diccionarios en Python

def crear_diccionario(clave, valor):
    """
    Crea y retorna un diccionario con una clave y un valor.
    """
    return {clave: valor}

def acceder_valor(diccionario, clave):
    """
    Retorna el valor asociado a la clave en el diccionario.
    Si la clave no existe, retorna None.
    """
    return diccionario.get(clave)

def agregar_elemento(diccionario, clave, valor):
    """
    Agrega un nuevo par clave-valor al diccionario y retorna el diccionario actualizado.
    """
    diccionario[clave] = valor
    return diccionario

def eliminar_elemento(diccionario, clave):
    """
    Elimina el par clave-valor del diccionario si la clave existe.
    Retorna el diccionario actualizado.
    """
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

def obtener_claves(diccionario):
    """
    Retorna una lista con todas las claves del diccionario.
    """
    return list(diccionario.keys())

def obtener_valores(diccionario):
    """
    Retorna una lista con todos los valores del diccionario.
    """
    return list(diccionario.values())

def actualizar_diccionario(diccionario1, diccionario2):
    """
    Actualiza diccionario1 con los pares clave-valor de diccionario2.
    Retorna el diccionario actualizado.
    """
    diccionario1.update(diccionario2)
    return diccionario1

def contar_frecuencias(lista):
    """
    Recibe una lista y retorna un diccionario con la frecuencia de cada elemento.
    """
    frecuencias = {}
    for elemento in lista:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    return frecuencias

def combinar_diccionarios(dict1, dict2):
    """
    Combina dos diccionarios en uno nuevo sin modificar los originales.
    Si hay claves duplicadas, mantiene el valor del segundo diccionario.
    """
    nuevo_dict = dict1.copy()
    nuevo_dict.update(dict2)
    return nuevo_dict

def es_subdiccionario(subdict, superdict):
    """
    Verifica si subdict es un subdiccionario de superdict.
    Retorna True si todos los pares clave-valor de subdict están en superdict, False en caso contrario.
    """
    for clave, valor in subdict.items():
        if clave not in superdict or superdict[clave] != valor:
            return False
    return True

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 10

    print("Evaluando la implementación...\n")

    # Prueba 1: crear_diccionario
    try:
        assert crear_diccionario("a", 1) == {"a": 1}
        print("✅ Prueba 1 pasada: crear_diccionario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: crear_diccionario no funciona como se esperaba")

    # Prueba 2: acceder_valor
    try:
        assert acceder_valor({"a": 1, "b": 2}, "a") == 1
        assert acceder_valor({"a": 1, "b": 2}, "c") == None
        print("✅ Prueba 2 pasada: acceder_valor funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: acceder_valor no funciona como se esperaba")

    # Prueba 3: agregar_elemento
    try:
        assert agregar_elemento({"a": 1}, "b", 2) == {"a": 1, "b": 2}
        print("✅ Prueba 3 pasada: agregar_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: agregar_elemento no funciona como se esperaba")

    # Prueba 4: eliminar_elemento
    try:
        assert eliminar_elemento({"a": 1, "b": 2}, "a") == {"b": 2}
        assert eliminar_elemento({"a": 1}, "b") == {"a": 1}
        print("✅ Prueba 4 pasada: eliminar_elemento funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: eliminar_elemento no funciona como se esperaba")

    # Prueba 5: obtener_claves
    try:
        assert set(obtener_claves({"a": 1, "b": 2})) == {"a", "b"}
        print("✅ Prueba 5 pasada: obtener_claves funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: obtener_claves no funciona como se esperaba")

    # Prueba 6: obtener_valores
    try:
        assert set(obtener_valores({"a": 1, "b": 2})) == {1, 2}
        print("✅ Prueba 6 pasada: obtener_valores funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: obtener_valores no funciona como se esperaba")

    # Prueba 7: actualizar_diccionario
    try:
        assert actualizar_diccionario({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
        print("✅ Prueba 7 pasada: actualizar_diccionario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: actualizar_diccionario no funciona como se esperaba")

    # Prueba 8: contar_frecuencias
    try:
        assert contar_frecuencias([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
        print("✅ Prueba 8 pasada: contar_frecuencias funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: contar_frecuencias no funciona como se esperaba")

    # Prueba 9: combinar_diccionarios
    try:
        assert combinar_diccionarios({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
        print("✅ Prueba 9 pasada: combinar_diccionarios funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 9 fallida: combinar_diccionarios no funciona como se esperaba")

    # Prueba 10: es_subdiccionario
    try:
        assert es_subdiccionario({"a": 1}, {"a": 1, "b": 2}) == True
        assert es_subdiccionario({"a": 1, "c": 3}, {"a": 1, "b": 2}) == False
        print("✅ Prueba 10 pasada: es_subdiccionario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 10 fallida: es_subdiccionario no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de las operaciones con diccionarios en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
