# Estructuras de datos para gestión de biblioteca

# Datos de libros predefinidos para utilizar en tus funciones
libros_iniciales = [
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
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "isbn": "978-8499890944",
        "anio": 1949,
        "genero": "Distopía",
        "disponible": True
    },
    {
        "titulo": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "isbn": "978-8497940246",
        "anio": 1813,
        "genero": "Novela romántica",
        "disponible": True
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "isbn": "978-8420412146",
        "anio": 1605,
        "genero": "Novela",
        "disponible": True
    },
    {
        "titulo": "Little Red Riding Hood(Caperucita roja)",
        "autor": "Charles Perrault",
        "isbn": "978-0156528504",
        "anio": 1697,
        "genero": "Fairy tale",
        "disponible": True
    },
    {
        "titulo": "Programación en Python IFCD32",
        "autor": "Sergio Vargas Mateo",
        "isbn": "978-84-1103-904-8",
        "anio": 2022,
        "genero": "Programación",
        "disponible": False
    }
]

# Aquí va el código que debes desarrollar
def agregar_libro(libros, nuevo_libro):
    libros.append(nuevo_libro)
    return libros

def buscar_por_autor(libros, autor):
    return [libro for libro in libros if libro["autor"].lower() == autor.lower()] 

def filtrar_por_anio(libros, anio):
    return [libro for libro in libros if libro["anio"] >= anio]

def libros_disponibles(libros):
    return [libro for libro in libros if libro["disponible"]]

# Datos adicionales para pruebas
datos_nuevos = [
    ("Rayuela", "Julio Cortázar", 1963),
    ("Ficciones", "Jorge Luis Borges", 1944)
]

# Aquí va el código que debes desarrollar
claves = ["titulo", "autor", "anio"]
convertir_tuplas_a_diccionarios = lambda tuplas: [dict(zip(claves, tupla)) for tupla in tuplas]
nuevos_libros = convertir_tuplas_a_diccionarios(datos_nuevos)

def ordenar_libros(libros, criterio):
    ordenada = sorted(libros, key=lambda libro: libro[criterio])
    return ordenada


# Pruebas (no modificar)
nuevo_libro = {
    "titulo": "La Odisea",
    "autor": "Homero",
    "isbn": "978-8491050742",
    "anio": -800,
    "genero": "Poema épico",
    "disponible": True
}

print("=== PRUEBAS DE FUNCIONALIDAD ===")
print("Agregando nuevo libro...")
libros = agregar_libro(libros_iniciales, nuevo_libro)
print(f"Total de libros: {len(libros)}")

print("\nBuscando libros de Cervantes:")
for libro in buscar_por_autor(libros, "Cervantes"):
    print(f"- {libro['titulo']} ({libro['isbn']})")

print("\nLibros desde 1950:")
for libro in filtrar_por_anio(libros, 1950):
    print(f"- {libro['titulo']} ({libro['anio']})")

print(f"\nLibros disponibles: {len(libros_disponibles(libros))}")

print("\nNuevos libros convertidos:")
nuevos_libros = convertir_tuplas_a_diccionarios(datos_nuevos)
for libro in nuevos_libros:
    print(f"- {libro['titulo']} por {libro['autor']} ({libro['anio']})")

print("\nLibros ordenados por año:")
for libro in ordenar_libros(libros, "anio")[:3]:  # Mostramos solo los 3 más antiguos
    print(f"- {libro['anio']} - {libro['titulo']}")