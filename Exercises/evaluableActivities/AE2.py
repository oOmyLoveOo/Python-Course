# Funciones para manipulación de textos en sistema de biblioteca

# Aquí va el código que debes desarrollar

# Formateo de títulos:
# Crear una función que normalice los títulos de los libros (primera letra de cada palabra en mayúscula).
def formatear_titulo(titulo):
    return titulo.title()
# Implementar otra función que abrevie títulos largos (más de 20 caracteres) añadiendo "..." al final.
def abreviar_titulo(titulo):
    return titulo[:20].rstrip() + "..." if len(titulo) > 20 else titulo

# Búsqueda de libros:
# Desarrollar una función que permita buscar libros por palabra clave en el título.
# Implementar la búsqueda sin distinguir entre mayúsculas y minúsculas.
def buscar_por_palabra_clave(titulo, palabra_clave):
    return palabra_clave.lower() in titulo.lower()

# Validación de ISBN:
# Crear una función para validar el formato de ISBN-13 (debe tener 13 dígitos, puede contener guiones).
def validar_isbn(isbn):
    counter = 0
    for char in isbn:
        if char.isdigit():
            counter += 1
        elif char != "-":
            return False
    return counter == 13

# Implementar una función que limpie y estandarice los ISBN (eliminar espacios, convertir a un formato consistente).
def limpiar_isbn(isbn):
    isbn_limpio = ''.join(i for i in isbn if i.isdigit())
    return isbn_limpio if len(isbn_limpio) == 13 else None

# Generación de códigos:
# Desarrollar una función que genere un código de referencia para cada libro combinando las primeras letras del título, autor y año.
def generar_codigo_referencia(titulo, autor, anio):
    titulo_sin = titulo.replace(" ", "")[:3] 
    autor_sin = autor.replace(" ", "")[:3]
    anio_sin = str(anio).replace(" ", "")[:3]
    code = titulo_sin + autor_sin + anio_sin
    return code

# Datos para probar las funciones
titulo = "el ingenioso hidalgo don quijote de la mancha"
autor = "miguel de cervantes saavedra"
anio = 1605
isbn = "978-84-376-0494-7"

# Pruebas de las funciones (no modificar)
print("Título formateado:", formatear_titulo(titulo))
print("Título abreviado:", abreviar_titulo(titulo))
print("Contiene 'quijote':", buscar_por_palabra_clave(titulo, "quijote"))
print("ISBN válido:", validar_isbn(isbn))
print(limpiar_isbn(isbn))
print("Código de referencia:", generar_codigo_referencia(titulo, autor, anio))