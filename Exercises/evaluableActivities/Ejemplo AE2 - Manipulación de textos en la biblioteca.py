# Funciones para manipulación de textos en sistema de biblioteca


def formatear_titulo(titulo):
    """
    Convierte la primera letra de cada palabra del título a mayúscula
    """
    return titulo.title()

def abreviar_titulo(titulo, max_longitud=20):
    """
    Abrevia títulos largos añadiendo "..." al final
    """
    if len(titulo) > max_longitud:
        return titulo[:max_longitud-3] + "..."
    return titulo

def buscar_por_palabra_clave(titulo, palabra_clave):
    """
    Busca una palabra clave en el título, sin distinguir mayúsculas/minúsculas
    """
    return palabra_clave.lower() in titulo.lower()

def validar_isbn(isbn):
    """
    Valida que un ISBN-13 tenga el formato correcto
    """
    # Eliminar guiones y espacios
    isbn_limpio = isbn.replace("-", "").replace(" ", "")
    
    # Verificar que tenga 13 dígitos y sean todos números
    if len(isbn_limpio) == 13 and isbn_limpio.isdigit():
        return True
    return False

def generar_codigo_referencia(titulo, autor, anio):
    """
    Genera un código de referencia utilizando las primeras letras del título y autor
    """
    palabras_titulo = titulo.split()
    palabras_autor = autor.split()
    
    codigo = ""
    # Agregar primera letra de cada palabra del título
    for palabra in palabras_titulo:
        if palabra:
            codigo += palabra[0].upper()
    
    # Agregar primera letra de cada palabra del autor
    for palabra in palabras_autor:
        if palabra:
            codigo += palabra[0].upper()
    
    # Añadir los últimos dos dígitos del año
    codigo += str(anio)[-2:]
    
    return codigo

# Ejemplo de uso
titulo = "el ingenioso hidalgo don quijote de la mancha"
autor = "miguel de cervantes saavedra"
anio = 1605
isbn = "978-84-376-0494-7"

print("Título formateado:", formatear_titulo(titulo))
print("Título abreviado:", abreviar_titulo(titulo))
print("Contiene 'quijote':", buscar_por_palabra_clave(titulo, "quijote"))
print("ISBN válido:", validar_isbn(isbn))
print("Código de referencia:", generar_codigo_referencia(titulo, autor, anio))