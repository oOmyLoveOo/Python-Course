# Funciones para la gestión de una biblioteca
# Autor: [Nombre del estudiante]
# Fecha: [Fecha actual]

# Biblioteca inicial con algunos libros
biblioteca = []
prestamos = []

def agregar_libro(titulo, autor, isbn, anio=None, genero=None, **datos_adicionales):
    """
    Agrega un nuevo libro a la biblioteca
    
    Parámetros:
    titulo (str): Título del libro
    autor (str): Autor del libro
    isbn (str): ISBN único del libro
    anio (int, opcional): Año de publicación
    genero (str, opcional): Género literario
    **datos_adicionales: Campos adicionales como editorial, páginas, etc.
    
    Retorna:
    dict: El libro agregado, o None si el ISBN ya existe
    """
    # Verificar si el ISBN ya existe
    for libro in biblioteca:
        if libro["isbn"] == isbn:
            print(f"Error: Ya existe un libro con ISBN {isbn}")
            return None
    
    # Crear el libro con los campos obligatorios
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "disponible": True
    }
    
    # Añadir campos opcionales si se proporcionaron
    if anio is not None:
        nuevo_libro["anio"] = anio
    
    if genero is not None:
        nuevo_libro["genero"] = genero
    
    # Añadir cualquier otro dato adicional
    for clave, valor in datos_adicionales.items():
        nuevo_libro[clave] = valor
    
    # Agregar el libro a la biblioteca
    biblioteca.append(nuevo_libro)
    return nuevo_libro

def buscar_libro(isbn=None, titulo=None, autor=None, genero=None):
    """
    Busca libros que coincidan con los criterios especificados
    
    Parámetros:
    isbn (str, opcional): ISBN exacto a buscar
    titulo (str, opcional): Parte del título a buscar
    autor (str, opcional): Parte del nombre del autor a buscar
    genero (str, opcional): Género literario a buscar
    
    Retorna:
    list: Lista de libros que coinciden con los criterios
    """
    resultados = []
    
    for libro in biblioteca:
        # Si se especificó ISBN y no coincide, saltar este libro
        if isbn and libro.get("isbn") != isbn:
            continue
            
        # Si se especificó título y no está contenido, saltar este libro
        if titulo and titulo.lower() not in libro.get("titulo", "").lower():
            continue
            
        # Si se especificó autor y no está contenido, saltar este libro
        if autor and autor.lower() not in libro.get("autor", "").lower():
            continue
            
        # Si se especificó género y no coincide, saltar este libro
        if genero and libro.get("genero") != genero:
            continue
            
        # Si llegamos aquí, el libro cumple todos los criterios especificados
        resultados.append(libro)
    
    return resultados

def prestar_libro(isbn, usuario):
    """
    Registra el préstamo de un libro a un usuario
    
    Parámetros:
    isbn (str): ISBN del libro a prestar
    usuario (str): Nombre o ID del usuario
    
    Retorna:
    bool: True si el préstamo fue exitoso, False en caso contrario
    """
    libros_encontrados = buscar_libro(isbn=isbn)
    
    if not libros_encontrados:
        print(f"Error: No se encontró un libro con ISBN {isbn}")
        return False
    
    libro = libros_encontrados[0]
    
    if not libro["disponible"]:
        print(f"Error: El libro '{libro['titulo']}' no está disponible")
        return False
    
    # Registrar el préstamo
    libro["disponible"] = False
    
    from datetime import datetime, timedelta
    fecha_prestamo = datetime.now()
    fecha_devolucion = fecha_prestamo + timedelta(days=14)  # Préstamo por 14 días
    
    prestamo = {
        "libro": libro,
        "usuario": usuario,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion_prevista": fecha_devolucion
    }
    
    prestamos.append(prestamo)
    print(f"Libro '{libro['titulo']}' prestado a {usuario} hasta {fecha_devolucion.strftime('%d/%m/%Y')}")
    return True

def generar_informe_disponibilidad():
    """
    Genera un informe de disponibilidad de libros
    
    Retorna:
    dict: Diccionario con el total de libros, disponibles y prestados
    """
    total = len(biblioteca)
    disponibles = sum(1 for libro in biblioteca if libro.get("disponible", True))
    prestados = total - disponibles
    
    informe = {
        "total_libros": total,
        "libros_disponibles": disponibles,
        "libros_prestados": prestados,
        "porcentaje_disponibilidad": (disponibles / total) * 100 if total > 0 else 0
    }
    
    return informe

def libros_mas_antiguos(n=5):
    """
    Retorna los N libros más antiguos de la biblioteca
    
    Parámetros:
    n (int): Número de libros a retornar, por defecto 5
    
    Retorna:
    list: Lista de los N libros más antiguos
    """
    # Filtrar libros que tienen año definido
    libros_con_anio = [libro for libro in biblioteca if "anio" in libro]
    
    # Ordenar por año (ascendente)
    libros_ordenados = sorted(libros_con_anio, key=lambda x: x["anio"])
    
    # Retornar los primeros N libros o todos si hay menos de N
    return libros_ordenados[:n]

# Ejemplo de uso
agregar_libro("Cien años de soledad", "Gabriel García Márquez", "978-8497592208", 1967, "Realismo mágico", 
              editorial="Sudamericana", paginas=471)
agregar_libro("El señor de los anillos", "J.R.R. Tolkien", "978-8445000656", 1954, "Fantasía")
agregar_libro("1984", "George Orwell", "978-8499890944", 1949, "Distopía")

# Buscar libros
print("Búsqueda por autor:")
for libro in buscar_libro(autor="García"):
    print(f"- {libro['titulo']} ({libro['isbn']})")

# Prestar un libro
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