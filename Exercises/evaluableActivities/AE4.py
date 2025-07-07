# Funciones para la gestión de una biblioteca

# Aquí va el código que debes desarrollar
def agregar_libro(titulo, autor, isbn, anio, genero, editorial=None, paginas=None):
    libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "anio": anio,
        "genero": genero,
        "editorial": editorial,
        "paginas": paginas,
        "disponible": True
    }
    biblioteca.append(libro)

def buscar_libro(titulo=None, autor=None, isbn=None, anio=None, genero=None, editorial=None):
    resultado = []
    for libro in biblioteca:
        if (titulo is None or titulo.lower() in libro["titulo"].lower()) and \
           (autor is None or autor.lower() in libro["autor"].lower()) and \
           (isbn is None or isbn == libro["isbn"]) and \
           (anio is None or anio == libro["anio"]) and \
           (genero is None or genero.lower() in libro["genero"].lower()) and \
           (editorial is None or editorial.lower() in libro.get("editorial", "").lower()):
            resultado.append(libro)
    return resultado

def prestar_libro(isbn, usuario):
    for libro in biblioteca:
        if libro["isbn"] == isbn and libro["disponible"]:
            libro["disponible"] = False
            prestamos.append((libro, usuario))
            print(f"Libro '{libro['titulo']}' prestado a {usuario}.")
            return True
    print(f"El libro con ISBN {isbn} no está disponible para préstamo.")

def generar_informe_disponibilidad():
    total_libros = len(biblioteca)
    libros_disponibles = sum(1 for libro in biblioteca if libro["disponible"])
    libros_prestados = total_libros - libros_disponibles
    porcentaje_disponibilidad = (libros_disponibles / total_libros * 100) if libros_disponibles > 0 else 0
    return {
        "total_libros": total_libros,
        "libros_disponibles": libros_disponibles,
        "porcentaje_disponibilidad": porcentaje_disponibilidad,
        "libros_prestados": libros_prestados
    }

def libros_mas_antiguos(n):
    return sorted(biblioteca, key=lambda libro: libro["anio"])[:n]

# Biblioteca inicial vacía
biblioteca = []
prestamos = []

# Código de prueba (no modificar)
print("=== SISTEMA DE BIBLIOTECA ===")

# Agregar libros
print("\nAgregando libros...")
agregar_libro("Cien años de soledad", "Gabriel García Márquez", "978-8497592208", 1967, "Realismo mágico", editorial="Sudamericana", paginas=471)
agregar_libro("El señor de los anillos", "J.R.R. Tolkien", "978-8445000656", 1954, "Fantasía")
agregar_libro("1984", "George Orwell", "978-8499890944", 1949, "Distopía")

# Buscar libros
print("\nBúsqueda por autor:")
for libro in buscar_libro(autor="García"):
    print(f"- {libro['titulo']} ({libro['isbn']})")

# Prestar un libro
print("\nProbando el sistema de préstamos:")
prestar_libro("978-8497592208", "Juan Pérez")

# Generar informe
informe = generar_informe_disponibilidad()
print("\nInforme de disponibilidad:")
print(f"Total de libros: {informe['total_libros']}")
print(f"Libros disponibles: {informe['libros_disponibles']} ({informe['porcentaje_disponibilidad']:.1f}%)")
print(f"Libros prestados: {informe['libros_prestados']}")

# Mostrar libros más antiguos
print("\nLibros más antiguos:")
for libro in libros_mas_antiguos(2):
    print(f"- {libro['titulo']} ({libro['anio']})")