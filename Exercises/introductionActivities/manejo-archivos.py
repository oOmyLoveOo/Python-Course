# Actividad: Manejo de Archivos en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando los conceptos de manejo de archivos apropiados.
3. No modifiques los nombres de las funciones existentes.
4. Una vez que hayas completado todo, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

def leer_archivo(nombre_archivo):
    """
    Lee el contenido de un archivo y lo retorna como una cadena.
    
    Parámetros:
    - nombre_archivo (str): El nombre del archivo a leer.
    
    Retorna:
    - str: El contenido del archivo.
    """
    with open(nombre_archivo, "r") as f:
        str = f.read()
        return str

def escribir_archivo(nombre_archivo, contenido):
    """
    Escribe el contenido en un archivo, sobrescribiendo si ya existe.
    
    Parámetros:
    - nombre_archivo (str): El nombre del archivo a escribir.
    - contenido (str): El contenido a escribir en el archivo.
    """
    with open(nombre_archivo, "w") as f:
        f.write(contenido)

def agregar_a_archivo(nombre_archivo, contenido):
    """
    Agrega el contenido al final de un archivo existente.
    
    Parámetros:
    - nombre_archivo (str): El nombre del archivo a modificar.
    - contenido (str): El contenido a agregar al archivo.
    """
    with open(nombre_archivo, "a") as f:
        f.write(contenido)

def leer_lineas(nombre_archivo):
    """
    Lee el archivo línea por línea y retorna una lista de líneas.
    
    Parámetros:
    - nombre_archivo (str): El nombre del archivo a leer.
    
    Retorna:
    - list: Una lista donde cada elemento es una línea del archivo.
    """
    with open(nombre_archivo, "r") as f:
        return f.readlines()

def copiar_archivo(origen, destino):
    """
    Copia el contenido de un archivo a otro.
    
    Parámetros:
    - origen (str): El nombre del archivo de origen.
    - destino (str): El nombre del archivo de destino.
    """
    with open(origen, "r") as o:
        with open(destino, "w") as d:
            d.write(o.read())

def contar_palabras(nombre_archivo):
    """
    Cuenta el número de palabras en un archivo.
    
    Parámetros:
    - nombre_archivo (str): El nombre del archivo a analizar.
    
    Retorna:
    - int: El número de palabras en el archivo.
    """
    with open(nombre_archivo, "r") as f:
        contenido = f.read()
        return len(contenido.split())
    
def leer_binario(nombre_archivo):
    """
    Lee un archivo en modo binario y retorna los primeros 10 bytes.
    
    Parámetros:
    - nombre_archivo (str): El nombre del archivo a leer.
    
    Retorna:
    - bytes: Los primeros 10 bytes del archivo.
    """
    with open(nombre_archivo, "rb") as f:
        bytes = f.read(10)
        return bytes

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 7

    print("Evaluando la implementación...\n")

    # Prueba 1: Leer y escribir archivo
    try:
        contenido_original = "Hola, mundo!"
        escribir_archivo("test.txt", contenido_original)
        contenido_leido = leer_archivo("test.txt")
        assert contenido_leido == contenido_original
        print("✅ Prueba 1 pasada: Leer y escribir archivo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: Problema con leer o escribir archivo")

    # Prueba 2: Agregar a archivo
    try:
        agregar_a_archivo("test.txt", "\nEsta es una nueva línea.")
        contenido = leer_archivo("test.txt")
        assert contenido == "Hola, mundo!\nEsta es una nueva línea."
        print("✅ Prueba 2 pasada: Agregar a archivo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: Problema con agregar a archivo")

    # Prueba 3: Leer líneas
    try:
        lineas = leer_lineas("test.txt")
        assert len(lineas) == 2
        assert lineas[0] == "Hola, mundo!\n"
        assert lineas[1] == "Esta es una nueva línea."
        print("✅ Prueba 3 pasada: Leer líneas funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: Problema con leer líneas")

    # Prueba 4: Copiar archivo
    try:
        copiar_archivo("test.txt", "copia_test.txt")
        contenido_original = leer_archivo("test.txt")
        contenido_copia = leer_archivo("copia_test.txt")
        assert contenido_original == contenido_copia
        print("✅ Prueba 4 pasada: Copiar archivo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: Problema con copiar archivo")

    # Prueba 5: Contar palabras
    try:
        num_palabras = contar_palabras("test.txt")
        assert num_palabras == 7
        print("✅ Prueba 5 pasada: Contar palabras funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: Problema con contar palabras")

    # Prueba 6: Leer binario
    try:
        escribir_archivo("binario.bin", "Contenido binario de prueba")
        datos_binarios = leer_binario("binario.bin")
        assert isinstance(datos_binarios, bytes)
        assert len(datos_binarios) == 10
        print("✅ Prueba 6 pasada: Leer binario funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Problema con leer binario")

    # Prueba 7: Manejo de excepciones
    try:
        resultado = leer_archivo("archivo_inexistente.txt")
        print("❌ Prueba 7 fallida: No se manejó correctamente la excepción de archivo inexistente")
    except FileNotFoundError:
        print("✅ Prueba 7 pasada: Se manejó correctamente la excepción de archivo inexistente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: Se lanzó una excepción inesperada")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de los conceptos de manejo de archivos en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
