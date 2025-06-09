# Actividad: Práctica de Operadores Aritméticos en Python

"""
Instrucciones para el estudiante:

1. Lee el ejemplo proporcionado sobre cómo crear una función con return:

   def duplicar(numero):
       return numero * 2

   En este ejemplo, la función 'duplicar' toma un número como entrada,
   lo multiplica por 2 y devuelve el resultado usando 'return'.

2. Completa las funciones siguientes según las instrucciones.
3. Utiliza los operadores aritméticos correspondientes en cada función.
4. Asegúrate de usar 'return' para devolver el resultado de cada operación.
5. No uses variables adicionales, realiza las operaciones directamente en el return.
6. Ejecuta el archivo para verificar si tus implementaciones son correctas. 
   Si todo es correcto, sube el documento a la plataforma.

¡Buena suerte!
"""

def suma(a, b):
    """
    Realiza una suma y devuelve el resultado.
    """
    # Tu código aquí
    pass

def resta(a, b):
    """
    Realiza una resta y devuelve el resultado.
    """
    # Tu código aquí
    pass

def multiplicacion(a, b):
    """
    Realiza una multiplicación y devuelve el resultado.
    """
    # Tu código aquí
    pass

def division(a, b):
    """
    Realiza una división y devuelve el resultado.
    """
    # Tu código aquí
    pass

def division_entera(a, b):
    """
    Realiza una división entera y devuelve el resultado.
    """
    # Tu código aquí
    pass

def modulo(a, b):
    """
    Calcula el módulo y devuelve el resultado.
    """
    # Tu código aquí
    pass

def potencia(base, exponente):
    """
    Calcula la potencia y devuelve el resultado.
    """
    # Tu código aquí
    pass

def operacion_combinada(a, b, c, d):
    """
    Realiza la operación (a + b) * c - d y devuelve el resultado.
    """
    # Tu código aquí
    pass

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 8

    print("Evaluando tu implementación...\n")

    # Prueba 1: suma
    try:
        assert suma(5, 3) == 8
        print("✅ Prueba 1 pasada: suma funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: suma no funciona como se esperaba")

    # Prueba 2: resta
    try:
        assert resta(10, 4) == 6
        print("✅ Prueba 2 pasada: resta funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: resta no funciona como se esperaba")

    # Prueba 3: multiplicación
    try:
        assert multiplicacion(6, 7) == 42
        print("✅ Prueba 3 pasada: multiplicación funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: multiplicación no funciona como se esperaba")

    # Prueba 4: división
    try:
        assert division(20, 4) == 5.0
        print("✅ Prueba 4 pasada: división funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: división no funciona como se esperaba")

    # Prueba 5: división entera
    try:
        assert division_entera(22, 5) == 4
        print("✅ Prueba 5 pasada: división entera funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: división entera no funciona como se esperaba")

    # Prueba 6: módulo
    try:
        assert modulo(17, 3) == 2
        print("✅ Prueba 6 pasada: módulo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: módulo no funciona como se esperaba")

    # Prueba 7: potencia
    try:
        assert potencia(2, 4) == 16
        print("✅ Prueba 7 pasada: potencia funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: potencia no funciona como se esperaba")

    # Prueba 8: operación combinada
    try:
        assert operacion_combinada(2, 3, 4, 5) == 15
        print("✅ Prueba 8 pasada: operación combinada funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: operación combinada no funciona como se esperada")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Has completado todas las funciones correctamente.")
        print("Toma una captura de pantalla de este resultado y súbela a la plataforma en la tarea correspondiente.")
    else:
        print("\nSigue practicando y vuelve a intentarlo para obtener una puntuación perfecta.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()