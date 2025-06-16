# Estructuras de datos para gestión de biblioteca

# Definición de la colección de libros usando listas y diccionarios
libros = [
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "isbn": "978-8497592208",
        "anio": 1967,
        "genero": "Realismo mágico",
        "disponible": True
    },
    {
        "titulo": "El señor de los anillos",
        "autor": "J.R.R. Tolkien",
        "isbn": "978-8445000656",
        "anio": 1954,
        "genero": "Fantasía",
        "disponible": False
    },
    # Añadir más libros aquí...
]

# Crear un diccionario usando ISBN como clave
libros_por_isbn = {}
for libro in libros:
    libros_por_isbn[libro["isbn"]] = libro

# Crear un diccionario que clasifique libros por género
libros_por_genero = {}
for libro in libros:
    genero = libro["genero"]
    if genero not in libros_por_genero:
        libros_por_genero[genero] = []
    libros_por_genero[genero].append(libro)

def agregar_libro(coleccion, libro_nuevo):
    """
    Agrega un nuevo libro a la colección y actualiza todas las estructuras
    """
    coleccion.append(libro_nuevo)
    libros_por_isbn[libro_nuevo["isbn"]] = libro_nuevo
    
    genero = libro_nuevo["genero"]
    if genero not in libros_por_genero:
        libros_por_genero[genero] = []
    libros_por_genero[genero].append(libro_nuevo)
    
    return coleccion

def buscar_por_autor(coleccion, autor_buscado):
    """
    Encuentra todos los libros de un autor específico
    """
    return [libro for libro in coleccion if autor_buscado.lower() in libro["autor"].lower()]

def filtrar_por_anio(coleccion, anio_minimo):
    """
    Filtra libros más recientes que el año especificado
    """
    return [libro for libro in coleccion if libro["anio"] >= anio_minimo]

def libros_disponibles(coleccion):
    """
    Lista todos los libros disponibles para préstamo
    """
    return [libro for libro in coleccion if libro["disponible"]]

def convertir_tuplas_a_diccionarios(lista_tuplas):
    """
    Convierte una lista de tuplas (título, autor, año) a la estructura de diccionarios
    """
    resultado = []
    for titulo, autor, anio in lista_tuplas:
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "anio": anio,
            "isbn": "Sin asignar",
            "genero": "Sin clasificar",
            "disponible": True
        }
        resultado.append(nuevo_libro)
    return resultado

def ordenar_libros(coleccion, criterio="titulo"):
    """
    Ordena los libros según un criterio especificado
    """
    return sorted(coleccion, key=lambda libro: libro[criterio])

# Ejemplo de uso
nuevo_libro = {
    "titulo": "Don Quijote de la Mancha",
    "autor": "Miguel de Cervantes",
    "isbn": "978-8420412146",
    "anio": 1605,
    "genero": "Novela",
    "disponible": True
}

agregar_libro(libros, nuevo_libro)
print("Libros de Cervantes:", buscar_por_autor(libros, "Cervantes"))
print("Libros desde 1950:", filtrar_por_anio(libros, 1950))
print("Libros disponibles:", len(libros_disponibles(libros)))

# Ejemplo de conversión de tipos
datos_nuevos = [
    ("1984", "George Orwell", 1949),
    ("Rayuela", "Julio Cortázar", 1963)
]
nuevos_libros = convertir_tuplas_a_diccionarios(datos_nuevos)
print("Nuevos libros convertidos:", nuevos_libros)

# Ordenar libros por año
libros_ordenados = ordenar_libros(libros, "anio")
for libro in libros_ordenados:
    print(f"{libro['anio']} - {libro['titulo']}")