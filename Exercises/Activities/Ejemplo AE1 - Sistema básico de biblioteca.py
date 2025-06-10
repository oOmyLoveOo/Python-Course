# Sistema básico de biblioteca


# Definición de variables para un libro
titulo_libro1 = "Cien años de soledad"
autor_libro1 = "Gabriel García Márquez"
anio_publicacion_libro1 = 1967
genero_libro1 = "Realismo mágico"
paginas_libro1 = 471
disponible_libro1 = True

# Cálculo de la antigüedad del libro
anio_actual = 2025
antiguedad_libro1 = anio_actual - anio_publicacion_libro1

# Determinar si el libro está disponible
if disponible_libro1:
    estado_libro1 = "disponible para préstamo"
else:
    estado_libro1 = "no disponible (prestado)"

# Crear una descripción completa del libro
descripcion_libro1 = titulo_libro1 + " escrito por " + autor_libro1 + " (" + str(anio_publicacion_libro1) + ")"

# Determinar si el libro es un clásico
if antiguedad_libro1 > 50:
    categoria_libro1 = "clásico"
else:
    categoria_libro1 = "contemporáneo"

# Mostrar la información del libro
print("INFORMACIÓN DEL LIBRO:")
print("Título:", titulo_libro1)
print("Autor:", autor_libro1)
print("Año de publicación:", anio_publicacion_libro1)
print("Género:", genero_libro1)
print("Páginas:", paginas_libro1)
print("Estado:", estado_libro1)
print("Descripción:", descripcion_libro1)
print("El libro es un", categoria_libro1, "con", antiguedad_libro1, "años de antigüedad.")