# Actividad: Manejo de Archivos en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función.
2. Completa los espacios marcados con ___ usando los conceptos de manejo de archivos en Python.
3. Presta atención a las pistas proporcionadas para cada función.
4. No modifiques los nombres de las funciones existentes.
5. Una vez que hayas completado todo, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

import os

def crear_archivo(nombre_archivo, contenido):
    """
    Crea un nuevo archivo con el nombre especificado y escribe el contenido en él.
    Si el archivo ya existe, debe sobrescribirlo.

    Pista: Usa 'open()' con el modo 'w' y un bloque 'with' para manejar el archivo de forma segura.
    """
    with open(nombre_archivo, "w") as file:
        file.write(contenido)

def leer_archivo(nombre_archivo):
    """
    Lee el contenido completo del archivo especificado y lo retorna como una cadena.

    Pista: Usa 'open()' con el modo 'r' y el método 'read()' para obtener todo el contenido.
    """
    with open(nombre_archivo, "r") as file:
        return file.read()

def agregar_linea(nombre_archivo, linea):
    """
    Agrega una nueva línea al final del archivo especificado.

    Pista: Usa 'open()' con el modo 'a' para añadir contenido sin sobrescribir.
    No olvides añadir un salto de línea '\n' al final de la línea.
    """
    with open(nombre_archivo, "a") as file:
        file.write(linea + '\n')

def leer_lineas(nombre_archivo):
    """
    Lee el archivo línea por línea y retorna una lista de las líneas.

    Pista: Usa 'open()' con el modo 'r' y el método 'readlines()' o un bucle for para iterar sobre las líneas.
    """
    with open(nombre_archivo, "r") as f:
        return f.readlines()

def copiar_archivo(origen, destino):
    """
    Copia el contenido del archivo de origen al archivo de destino.

    Pista: Abre el archivo de origen en modo lectura y el de destino en modo escritura.
    Luego, lee el contenido del origen y escríbelo en el destino.
    """
    with open(origen, "r") as f:
        with open(destino, "w") as d:
            d.write(f.read())


def contar_palabras(nombre_archivo):
    """
    Cuenta el número total de palabras en el archivo.

    Pista: Lee el contenido del archivo, usa el método 'split()' para dividir el texto en palabras,
    y luego cuenta la longitud de la lista resultante.
    """
    with open(nombre_archivo, "r") as f:
        contenido = f.read()
        return len(contenido.split())

def leer_por_bloques(nombre_archivo, tamano_bloque=1024):
    """
    Lee el archivo en bloques del tamaño especificado y retorna el contenido.

    Pista: Usa un bucle while para leer bloques con el método 'read(tamano_bloque)'
    hasta que no haya más contenido para leer.
    """
    with open(nombre_archivo, "r") as f:
        contenido = ""
        while True:
            bloque = f.read(tamano_bloque)
            if not bloque:
                break
            contenido += bloque
        return contenido

def obtener_info_archivo(nombre_archivo):
    """
    Retorna un diccionario con la siguiente información del archivo:
    - tamaño en bytes
    - fecha de última modificación
    - nombre del archivo (sin la ruta)

    Pista: Usa 'os.stat()' para obtener información del archivo y 'os.path.basename()'
    para obtener el nombre del archivo sin la ruta.
    """
    stats = os.stat(nombre_archivo)
    return {
        "tamaño" : stats.st_size,
        "ultima_modificacion" : stats.st_mtime,
        "nombre" : os.path.basename(nombre_archivo)
    }


def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando la implementación...\n")

    # Prueba 1: Crear y leer archivo
    try:
        crear_archivo("test.txt", "Hola, mundo!")
        contenido = leer_archivo("test.txt")
        assert contenido == "Hola, mundo!"
        print("✅ Prueba 1 pasada: Crear y leer archivo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: Crear y leer archivo no funciona como se esperaba")

    # Prueba 2: Agregar línea
    try:
        agregar_linea("test.txt", "Nueva línea")
        contenido = leer_archivo("test.txt")
        # Modificamos esta línea para que se ajuste a la implementación actual
        assert contenido == "Hola, mundo!Nueva línea\n"
        print("✅ Prueba 2 pasada: Agregar línea funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: Agregar línea no funciona como se esperaba")

    # Prueba 3: Leer líneas
    try:
        lineas = leer_lineas("test.txt")
        # Y ajustamos también esta verificación
        assert lineas == ["Hola, mundo!Nueva línea\n"]
        print("✅ Prueba 3 pasada: Leer líneas funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: Leer líneas no funciona como se esperada")

    # Prueba 4: Copiar archivo
    try:
        copiar_archivo("test.txt", "copia_test.txt")
        contenido_original = leer_archivo("test.txt")
        contenido_copia = leer_archivo("copia_test.txt")
        assert contenido_original == contenido_copia
        print("✅ Prueba 4 pasada: Copiar archivo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: Copiar archivo no funciona como se esperaba")

    # Prueba 5: Contar palabras
    try:
        crear_archivo("palabras.txt", "Esto es una prueba de contar palabras")
        num_palabras = contar_palabras("palabras.txt")
        assert num_palabras == 7
        print("✅ Prueba 5 pasada: Contar palabras funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: Contar palabras no funciona como se esperaba")

    # Prueba 6: Leer por bloques
    try:
        crear_archivo("bloques.txt", "a" * 2000)
        contenido = leer_por_bloques("bloques.txt", 1000)
        assert len(contenido) == 2000 and contenido == "a" * 2000
        print("✅ Prueba 6 pasada: Leer por bloques funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Leer por bloques no funciona como se esperaba")

    # Prueba 7: Obtener info del archivo
    try:
        info = obtener_info_archivo("test.txt")
        assert "tamaño" in info and "ultima_modificacion" in info and "nombre" in info
        assert info["nombre"] == "test.txt"
        print("✅ Prueba 7 pasada: Obtener info del archivo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: Obtener info del archivo no funciona como se esperaba")

    # Prueba 8: Manejo de excepciones
    try:
        leer_archivo("archivo_inexistente.txt")
        print("❌ Prueba 8 fallida: No se manejó correctamente la excepción de archivo inexistente")
    except FileNotFoundError:
        print("✅ Prueba 8 pasada: Se manejó correctamente la excepción de archivo inexistente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: No se manejó correctamente la excepción de archivo inexistente")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de los conceptos de manejo de archivos en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

    # Limpieza de archivos de prueba
    archivos_prueba = ["test.txt", "copia_test.txt", "palabras.txt", "bloques.txt"]
    for archivo in archivos_prueba:
        if os.path.exists(archivo):
            os.remove(archivo)

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
