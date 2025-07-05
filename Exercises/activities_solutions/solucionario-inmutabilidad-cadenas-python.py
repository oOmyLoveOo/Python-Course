# Solucionario: Descubriendo la Inmutabilidad de las Cadenas en Python

def cambiar_letra(palabra, indice, nueva_letra):
    """
    Cambia la letra en la posición 'indice' de 'palabra' por 'nueva_letra'.
    Retorna la palabra modificada.
    """
    return palabra[:indice] + nueva_letra + palabra[indice+1:]

def agregar_exclamacion(frase):
    """
    Agrega un signo de exclamación al final de 'frase'.
    Retorna la frase modificada.
    """
    return frase + "!"

def quitar_espacios(texto):
    """
    Quita todos los espacios de 'texto'.
    Retorna el texto modificado.
    """
    return texto.replace(" ", "")

def invertir_cadena(cadena):
    """
    Invierte el orden de los caracteres en 'cadena'.
    Retorna la cadena invertida.
    """
    return cadena[::-1]

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 4

    print("Evaluando la implementación...\n")

    # Prueba 1: cambiar_letra
    try:
        assert cambiar_letra("Python", 2, 'j') == "Pyjhon"
        print("✅ Prueba 1 pasada: cambiar_letra funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: cambiar_letra no funciona como se esperaba")

    # Prueba 2: agregar_exclamacion
    try:
        assert agregar_exclamacion("Hola mundo") == "Hola mundo!"
        print("✅ Prueba 2 pasada: agregar_exclamacion funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: agregar_exclamacion no funciona como se esperaba")

    # Prueba 3: quitar_espacios
    try:
        assert quitar_espacios("Python es genial") == "Pythonesgenial"
        print("✅ Prueba 3 pasada: quitar_espacios funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: quitar_espacios no funciona como se esperaba")

    # Prueba 4: invertir_cadena
    try:
        assert invertir_cadena("inmutable") == "elbatumni"
        print("✅ Prueba 4 pasada: invertir_cadena funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: invertir_cadena no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento de la inmutabilidad de las cadenas en Python.")
    else:
        print("\nAlgunas funciones necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()

"""
Explicación de las soluciones:

1. cambiar_letra(): Usamos el slicing para crear una nueva cadena. Tomamos la parte de la cadena
   antes del índice, añadimos la nueva letra, y luego añadimos el resto de la cadena original.

2. agregar_exclamacion(): Simplemente concatenamos el signo de exclamación al final de la cadena.

3. quitar_espacios(): Usamos el método replace() para crear una nueva cadena reemplazando todos
   los espacios con una cadena vacía.

4. invertir_cadena(): Usamos el slicing con paso -1 para crear una nueva cadena con los caracteres
   en orden inverso.

Todas estas soluciones crean y retornan nuevas cadenas en lugar de intentar modificar las originales,
respetando así la inmutabilidad de las cadenas en Python.
"""