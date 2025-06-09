# Actividad Combinada: Variables, Números, Cadenas y Booleanos en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando el valor o método apropiado.
3. Puedes usar números, strings, booleanos, o métodos de string según sea necesario.
4. No modifiques nada más en el código.
5. Una vez que hayas completado todas las funciones, ejecuta este script.

¡Buena suerte!
"""

def operacion_numerica():
    """
    Realiza una operación que involucre números enteros y float.
    El resultado debe ser 7.5
    """
    a = 5
    b = 2.5
    return a + b

def formateo_cadena():
    """
    Usa f-strings para formatear la cadena.
    Debe retornar "Hola, Juan. Tienes 25 años."
    """
    nombre = "Juan"
    edad = 25
    return f"Hola {nombre}. Tienes 25 años."

def manipulacion_cadena():
    """
    Manipula la cadena usando métodos de string.
    Debe retornar "python es genial"
    """
    texto = "  Python Es GENIAL  "
    return texto.strip().lower().___()

def operacion_booleana():
    """
    Realiza una operación booleana.
    Debe retornar True
    """
    a = True
    b = False
    return a and (not b)

def conteo_y_reemplazo():
    """
    Cuenta las ocurrencias de 'a' y reemplaza 'mundo' por 'python'.
    Debe retornar (3, "Hola python")
    """
    texto = "Hola mundo, abraza al mundo"
    conteo = texto.count('a')
    nuevo_texto = texto.replace('mundo', 'python')
    return (conteo, nuevo_texto)

def division_y_redondeo():
    """
    Divide 10 por 3 y redondea a 2 decimales.
    Debe retornar 3.33
    """
    resultado = 10 / 3
    return round(resultado, 2)

def encontrar_subcadena():
    """
    Encuentra la posición de 'python' en la cadena.
    Si 'python' no está en la cadena, debe retornar -1.
    """
    texto = "Aprendiendo programación con python"
    return texto.index('python') if 'python' in texto else -1

def es_numero_par_y_positivo(numero):
    """
    Verifica si el número es par y positivo.
    Debe retornar un booleano.
    """
    es_par = numero % 2 == ___
    es_positivo = numero > ___
    return es_par ___ es_positivo

def unir_y_dividir_cadenas():
    """
    Une las palabras con '-' y luego divídelas por '-'.
    Debe retornar ["python", "es", "divertido"]
    """
    palabras = ["python", "es", "divertido"]
    unidas = ___.___(palabras)
    return unidas.___(___) 

def eliminar_prefijo_y_sufijo():
    """
    Elimina el prefijo 'py' y el sufijo 'on' de la palabra 'python'.
    Debe retornar "th"
    """
    palabra = "python"
    return palabra.___("py").___("on")

# Función de verificación
def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 10

    print("Evaluando la implementación...\n")

    # Prueba 1: operacion_numerica
    try:
        assert operacion_numerica() == 7.5
        print("✅ Prueba 1 pasada: operacion_numerica funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: operacion_numerica no funciona como se esperaba")

    # Prueba 2: formateo_cadena
    try:
        assert formateo_cadena() == "Hola, Juan. Tienes 25 años."
        print("✅ Prueba 2 pasada: formateo_cadena funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: formateo_cadena no funciona como se esperaba")

    # Prueba 3: manipulacion_cadena
    try:
        assert manipulacion_cadena() == "python es genial"
        print("✅ Prueba 3 pasada: manipulacion_cadena funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: manipulacion_cadena no funciona como se esperaba")

    # Prueba 4: operacion_booleana
    try:
        assert operacion_booleana() == True
        print("✅ Prueba 4 pasada: operacion_booleana funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: operacion_booleana no funciona como se esperaba")

    # Prueba 5: conteo_y_reemplazo
    try:
        assert conteo_y_reemplazo() == (5, "Hola python, abraza al python")
        print("✅ Prueba 5 pasada: conteo_y_reemplazo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: conteo_y_reemplazo no funciona como se esperaba")

    # Prueba 6: division_y_redondeo
    try:
        assert division_y_redondeo() == 3.33
        print("✅ Prueba 6 pasada: division_y_redondeo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: division_y_redondeo no funciona como se esperaba")

    # Prueba 7: encontrar_subcadena
    try:
        assert encontrar_subcadena() == 29
        print("✅ Prueba 7 pasada: encontrar_subcadena funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: encontrar_subcadena no funciona como se esperaba")

    # Prueba 8: es_numero_par_y_positivo
    try:
        assert es_numero_par_y_positivo(6) == True
        assert es_numero_par_y_positivo(-2) == False
        assert es_numero_par_y_positivo(3) == False
        print("✅ Prueba 8 pasada: es_numero_par_y_positivo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: es_numero_par_y_positivo no funciona como se esperaba")

    # Prueba 9: unir_y_dividir_cadenas
    try:
        assert unir_y_dividir_cadenas() == ["python", "es", "divertido"]
        print("✅ Prueba 9 pasada: unir_y_dividir_cadenas funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 9 fallida: unir_y_dividir_cadenas no funciona como se esperaba")

    # Prueba 10: eliminar_prefijo_y_sufijo
    try:
        assert eliminar_prefijo_y_sufijo() == "th"
        print("✅ Prueba 10 pasada: eliminar_prefijo_y_sufijo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 10 fallida: eliminar_prefijo_y_sufijo no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un excelente manejo de variables, números, cadenas y booleanos en Python.")
    else:
        print("\nAlgunas funciones necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
