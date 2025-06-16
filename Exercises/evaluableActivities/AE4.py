# Funciones para la gestión de una biblioteca

# Aquí va el código que debes desarrollar

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