# Actividad: Práctica de Funciones de Cadenas en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Implementa cada función según las instrucciones proporcionadas.
3. Utiliza los conceptos aprendidos sobre manipulación de cadenas en Python para completar las funciones.
4. Una vez que hayas implementado todas las funciones, ejecuta este script.
5. El script evaluará tu implementación y te dará una puntuación.
6. Si obtienes una puntuación perfecta, ¡felicidades! Has dominado estos conceptos.
7. Si no obtienes una puntuación perfecta, revisa tus implementaciones y vuelve a intentarlo.

Conceptos clave a utilizar:
- Formateo de cadenas (f-strings)
- Métodos de cadenas como strip(), capitalize(), split(), join(), find(), replace()
- Operadores in, startswith(), endswith()
- Indexación de cadenas
- Conversión a mayúsculas y minúsculas

¡Buena suerte!
"""

def formatear_nombre(nombre, apellido, edad):
    """
    Usa f-strings para formatear un saludo.
    
    Pista: Utiliza f-strings para incluir las variables en la cadena.
    Formato esperado: "Hola, me llamo {nombre} {apellido} y tengo {edad} años."
    """
    # Tu código aquí
    pass

def limpiar_y_capitalizar(texto):
    """
    Elimina espacios al inicio y al final, y capitaliza la primera letra.
    
    Pista: Combina los métodos strip() y capitalize().
    """
    # Tu código aquí
    pass

def dividir_y_unir(frase, separador):
    """
    Divide la frase en palabras y luego las une usando el separador.
    
    Pista: Usa split() para dividir y join() para unir.
    """
    # Tu código aquí
    pass

def encontrar_subcadena(texto, subcadena):
    """
    Encuentra la posición de la subcadena en el texto.
    Devuelve la posición como un número (usa el método find()).
    
    Pista: El método find() devuelve -1 si la subcadena no se encuentra.
    """
    # Tu código aquí
    pass

def verificar_prefijo_sufijo(texto, prefijo, sufijo):
    """
    Verifica si el texto comienza con el prefijo y termina con el sufijo.
    Devuelve una cadena con el resultado de ambas comprobaciones.
    
    Pista: Usa los métodos startswith() y endswith(). Ten en cuenta las mayúsculas/minúsculas.
    Formato esperado: "Comienza con {prefijo}: {True/False}, Termina con {sufijo}: {True/False}"
    """
    # Tu código aquí
    pass

def contar_y_reemplazar(texto, palabra, reemplazo):
    """
    Cuenta cuántas veces aparece 'palabra' en el texto y luego la reemplaza con 'reemplazo'.
    
    Pista: Utiliza los métodos count() y replace().
    Formato esperado: "La palabra '{palabra}' aparece {n} veces. Texto modificado: '{nuevo_texto}'"
    """
    # Tu código aquí
    pass

def procesar_url(url):
    """
    Elimina 'https://' del inicio y '.com' del final de la URL si están presentes.
    
    Pista: Investiga los métodos removeprefix() y removesuffix().
    """
    # Tu código aquí
    pass

def estilo_titulo(frase):
    """
    Convierte una frase a 'estilo título' usando el método title().
    
    Pista: El método title() capitaliza la primera letra de cada palabra.
    """
    # Tu código aquí
    pass

# Función de verificación
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