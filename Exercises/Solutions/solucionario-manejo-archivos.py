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
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

def agregar_a_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(contenido)

def leer_lineas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.readlines()

def copiar_archivo(origen, destino):
    with open(origen, 'r') as archivo_origen:
        with open(destino, 'w') as archivo_destino:
            archivo_destino.write(archivo_origen.read())

def contar_palabras(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        return len(contenido.split())

def leer_binario(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        return archivo.read(10)

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
