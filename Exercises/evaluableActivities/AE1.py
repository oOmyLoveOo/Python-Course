# Sistema básico de biblioteca

# Datos del libro:
# Título: Cien años de soledad
# Autor: Gabriel García Márquez
# Año de publicación: 1967
# Género: Realismo mágico
# Páginas: 471
# Disponible: True

# Aquí va el código que debes desarrollar

# Definición de variables
currentYear = 2025

class Book:
    def __init__(self, title, author, release, genre, pages, availability):
        self.title = title
        self.author = author
        self.release = release
        self.genre = genre
        self.pages = pages
        self.availability = availability

# Operaciones básica
    def isAvailable(self):
        return True if self.availability else False

    def  calculateAge(self):
        return currentYear - self.release

    def description(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Release Year: {self.release} ({self.calculateAge()} years ago)\n"
            f"Genre: {self.genre}\n"
            f"Pages: {self.pages}\n"
            f"Availability: {'Available' if self.isAvailable() else 'Checked out'}\n"
            f"Category: {self.isClassic()}\n"
        )

    def isClassic(self):
        return "Classic" if self.calculateAge() >= 50 else "Comptemporary"
    

Book1 = Book("cenicientaaa", "Juancitoooo", 2001, "+19", 20, True )
Book2 = Book("cenicientaeee", "Juancito", 2002, "+17", 1000, False )
Book3 = Book("cenicientaooo", "Juancitoo", 2003, "+18", 70, False )


Library = [Book1, Book2, Book3]

# Mostrar la información del libro
for Book in Library:
    print(Book.description())
    print("-" * 40)

#Otra forma de hacerlo
# Sistema básico de biblioteca usando una "matriz o lista con sublistas"
currentYear = 2025

# Cada libro es una lista: [Título, Autor, Año, Género, Páginas, Disponible]
"""
biblioteca = [
    ["Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico", 471, True],
    ["El amor en los tiempos del cólera", "Gabriel García Márquez", 1985, "Romance", 368, False],
    ["Crónica de una muerte anunciada", "Gabriel García Márquez", 1981, "Misterio", 120, True],
]

# Funciones auxiliares
def calcularEdad(anio_publicacion):
    return currentYear - anio_publicacion

def esClasico(anio_publicacion):
    return "Clásico" if calcularEdad(anio_publicacion) >= 50 else "Contemporáneo"

def disponibilidad_texto(disponible):
    return "Disponible" if disponible else "Prestado"

# Mostrar la información de cada libro
for libro in biblioteca:
    print(f"Título: {libro[0]}")
    print(f"Autor: {libro[1]}")
    print(f"Año de publicación: {libro[2]} ({calcularEdad(libro[2])} años atrás)")
    print(f"Género: {libro[3]}")
    print(f"Páginas: {libro[4]}")
    print(f"Estado: {disponibilidad_texto(libro[5])}")
    print(f"Categoría: {esClasico(libro[2])}")
    print("-" * 40) 
    
"""


