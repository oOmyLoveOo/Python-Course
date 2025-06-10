# Actividad: Descubriendo la Inmutabilidad de las Cadenas en Python
"""
Instrucciones para el estudiante:

1. Lee cada ejercicio cuidadosamente.
2. Intenta completar cada función según las instrucciones.
3. Si encuentras errores o comportamientos inesperados, anótalos y reflexiona sobre por qué ocurren.
4. Ejecuta el código y observa los resultados.
5. Al final, lee la siguiente explicación sobre la inmutabilidad de las cadenas.

Explicación sobre la inmutabilidad de las cadenas:

Si has intentado modificar las cadenas directamente en las funciones anteriores,
probablemente te hayas encontrado con algunos problemas o comportamientos inesperados.
Esto se debe a que las cadenas en Python son inmutables.

Inmutabilidad significa que una vez que se crea una cadena, no se puede modificar.
Cualquier operación que parezca modificar una cadena en realidad está creando una nueva cadena.

Por ejemplo:
- No puedes cambiar un carácter específico de una cadena usando indexación.
- Métodos como replace() o upper() devuelven nuevas cadenas, no modifican la original.
- Para "modificar" una cadena, necesitas crear y retornar una nueva con los cambios deseados.

Reflexiona sobre cómo podrías reescribir las funciones teniendo en cuenta la inmutabilidad de las cadenas.

¡Buena suerte!
"""




def cambiar_letra(palabra, indice, nueva_letra):
    """
    Intenta cambiar la letra en la posición 'indice' de 'palabra' por 'nueva_letra'.
    Retorna la palabra modificada.
    """
    # Tu código aquí
    return palabra[:indice] + nueva_letra + palabra[indice + 1:]

def agregar_exclamacion(frase):
    """
    Intenta agregar un signo de exclamación al final de 'frase'.
    Retorna la frase modificada.
    """
    # Tu código aquí
    return frase + "!"

def quitar_espacios(texto):
    """
    Intenta quitar todos los espacios de 'texto'.
    Retorna el texto modificado.
    """
    # Tu código aquí
    return texto.strip().replace(" ", "")

def invertir_cadena(cadena):
    """
    Intenta invertir el orden de los caracteres en 'cadena'.
    Retorna la cadena invertida.
    """
    # Tu código aquí
    invertida = ""
    for i in range(len(cadena) -1, -1, -1):
        invertida += cadena[i]
    return invertida

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 4

    print("Evaluando tu implementación...\n")

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
        print("\n¡Felicidades! Has completado todas las funciones correctamente.")
        print("Has entendido cómo trabajar con cadenas inmutables.")
        print("Toma una captura de pantalla de este resultado y súbela a la plataforma en la tarea correspondiente.")
    else:
        print("\nRevisa la explicación sobre inmutabilidad y vuelve a intentarlo para obtener una puntuación perfecta.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()

