def formatear_nombre(nombre, apellido, edad):
    return f"Hola, me llamo {nombre} {apellido} y tengo {edad} años."

def limpiar_y_capitalizar(texto):
    return texto.strip().capitalize()

def dividir_y_unir(frase, separador):
    return separador.join(frase.split())

def encontrar_subcadena(texto, subcadena):
    posicion = texto.find(subcadena)
    return posicion

def verificar_prefijo_sufijo(texto, prefijo, sufijo):
    return f"Comienza con {prefijo}: {texto.lower().startswith(prefijo.lower())}, Termina con {sufijo}: {texto.lower().endswith(sufijo.lower())}"

def contar_y_reemplazar(texto, palabra, reemplazo):
    conteo = texto.count(palabra)
    nuevo_texto = texto.replace(palabra, reemplazo)
    return f"La palabra '{palabra}' aparece {conteo} veces. Texto modificado: '{nuevo_texto}'"

def procesar_url(url):
    return url.removeprefix("https://").removesuffix(".com")

def estilo_titulo(frase):
    return frase.title()

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando la implementación...\n")

    # Prueba 1: formatear_nombre
    try:
        assert formatear_nombre("Juan", "Pérez", 30) == "Hola, me llamo Juan Pérez y tengo 30 años."
        print("✅ Prueba 1 pasada: formatear_nombre funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: formatear_nombre no funciona como se esperaba")

    # Prueba 2: limpiar_y_capitalizar
    try:
        assert limpiar_y_capitalizar("  python es genial  ") == "Python es genial"
        print("✅ Prueba 2 pasada: limpiar_y_capitalizar funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: limpiar_y_capitalizar no funciona como se esperaba")

    # Prueba 3: dividir_y_unir
    try:
        assert dividir_y_unir("Python es un lenguaje de programación", "-") == "Python-es-un-lenguaje-de-programación"
        print("✅ Prueba 3 pasada: dividir_y_unir funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: dividir_y_unir no funciona como se esperaba")

    # Prueba 4: encontrar_subcadena
    try:
        assert encontrar_subcadena("Python es versátil", "versátil") == 10
        assert encontrar_subcadena("Python es versátil", "Java") == -1
        print("✅ Prueba 4 pasada: encontrar_subcadena funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: encontrar_subcadena no funciona como se esperaba")

    # Prueba 5: verificar_prefijo_sufijo
    try:
        assert verificar_prefijo_sufijo("PyThOnPy", "Py", "py") == "Comienza con Py: True, Termina con py: True"
        print("✅ Prueba 5 pasada: verificar_prefijo_sufijo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: verificar_prefijo_sufijo no funciona como se esperaba")

    # Prueba 6: contar_y_reemplazar
    try:
        resultado = contar_y_reemplazar("Python es genial y Python es divertido", "Python", "Java")
        assert resultado == "La palabra 'Python' aparece 2 veces. Texto modificado: 'Java es genial y Java es divertido'"
        print("✅ Prueba 6 pasada: contar_y_reemplazar funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: contar_y_reemplazar no funciona como se esperaba")

    # Prueba 7: procesar_url
    try:
        assert procesar_url("https://www.ejemplo.com") == "www.ejemplo"
        assert procesar_url("www.python.org") == "www.python.org"
        print("✅ Prueba 7 pasada: procesar_url funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: procesar_url no funciona como se esperaba")

    # Prueba 8: estilo_titulo
    try:
        assert estilo_titulo("el lenguaje de programación python es genial") == "El Lenguaje De Programación Python Es Genial"
        print("✅ Prueba 8 pasada: estilo_titulo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: estilo_titulo no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un excelente manejo de las funciones de cadenas en Python.")
    else:
        print("\nAlgunas funciones necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
