# Solucionario: Introducción a la Programación Orientada a Objetos en Python


class Libro:
    """
    Representa un libro en una biblioteca.
    
    Atributos:
    - titulo (str): El título del libro.
    - autor (str): El autor del libro.
    - paginas (int): El número de páginas del libro.
    - prestado (bool): Indica si el libro está prestado o no.
    
    Completa la clase con el constructor (__init__) y el método __str__.
    """
    
    def __init__(self, titulo, autor, paginas):
        """
        Inicializa un nuevo objeto Libro.
        
        El atributo 'prestado' debe inicializarse como False por defecto.
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.prestado = False
    
    def __str__(self):
        """
        Devuelve una representación en string del libro.
        
        Debe devolver: "Título: [titulo], Autor: [autor], Páginas: [paginas]"
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"

    def prestar(self):
        """
        Marca el libro como prestado si no lo está ya.
        
        Retorna True si se pudo prestar el libro, False si ya estaba prestado.
        """
        if not self.prestado:
            self.prestado = True
            return True
        return False

    @classmethod
    def crear_libro_corto(cls, titulo, autor):
        """
        Método de clase para crear un libro considerado corto (menos de 100 páginas).
        
        Crea y retorna un nuevo objeto Libro con 99 páginas.
        """
        return cls(titulo, autor, 99)

class Biblioteca:
    """
    Representa una biblioteca que contiene libros.
    
    Atributos:
    - nombre (str): El nombre de la biblioteca.
    - libros (list): Una lista de objetos Libro.
    
    Completa la clase con el constructor y los métodos indicados.
    """
    
    def __init__(self, nombre):
        """
        Inicializa un nuevo objeto Biblioteca.
        
        El atributo 'libros' debe inicializarse como una lista vacía.
        """
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca.
        
        Parámetros:
        - libro (Libro): El libro a agregar.
        """
        self.libros.append(libro)
    
    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.
        
        Parámetros:
        - titulo (str): El título del libro a buscar.
        
        Retorna el libro si se encuentra, None en caso contrario.
        """
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
    
    @property
    def cantidad_libros(self):
        """
        Propiedad que devuelve la cantidad de libros en la biblioteca.
        """
        return len(self.libros)

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 7

    print("Evaluando la implementación...\n")

    # Prueba 1: Creación de un libro
    try:
        libro = Libro("Don Quijote", "Miguel de Cervantes", 863)
        assert libro.titulo == "Don Quijote"
        assert libro.autor == "Miguel de Cervantes"
        assert libro.paginas == 863
        assert libro.prestado == False
        print("✅ Prueba 1 pasada: La clase Libro se inicializa correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: La clase Libro no se inicializa como se esperaba")

    # Prueba 2: Representación en string de un libro
    try:
        libro = Libro("El principito", "Antoine de Saint-Exupéry", 96)
        assert str(libro) == "Título: El principito, Autor: Antoine de Saint-Exupéry, Páginas: 96"
        print("✅ Prueba 2 pasada: El método __str__ de Libro funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: El método __str__ de Libro no funciona como se esperaba")

    # Prueba 3: Préstamo de un libro
    try:
        libro = Libro("1984", "George Orwell", 328)
        assert libro.prestar() == True
        assert libro.prestar() == False
        print("✅ Prueba 3 pasada: El método prestar funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: El método prestar no funciona como se esperaba")

    # Prueba 4: Creación de un libro corto
    try:
        libro_corto = Libro.crear_libro_corto("La metamorfosis", "Franz Kafka")
        assert isinstance(libro_corto, Libro)
        assert libro_corto.titulo == "La metamorfosis"
        assert libro_corto.autor == "Franz Kafka"
        assert libro_corto.paginas == 99
        print("✅ Prueba 4 pasada: El método de clase crear_libro_corto funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: El método de clase crear_libro_corto no funciona como se esperaba")

    # Prueba 5: Creación de una biblioteca
    try:
        biblioteca = Biblioteca("Biblioteca Municipal")
        assert biblioteca.nombre == "Biblioteca Municipal"
        assert len(biblioteca.libros) == 0
        print("✅ Prueba 5 pasada: La clase Biblioteca se inicializa correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: La clase Biblioteca no se inicializa como se esperaba")

    # Prueba 6: Agregar y buscar libros en la biblioteca
    try:
        biblioteca = Biblioteca("Biblioteca Central")
        libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
        libro2 = Libro("El código Da Vinci", "Dan Brown", 589)
        biblioteca.agregar_libro(libro1)
        biblioteca.agregar_libro(libro2)
        assert biblioteca.buscar_libro("Cien años de soledad") == libro1
        assert biblioteca.buscar_libro("El código Da Vinci") == libro2
        assert biblioteca.buscar_libro("Libro inexistente") == None
        print("✅ Prueba 6 pasada: Los métodos agregar_libro y buscar_libro funcionan correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Los métodos agregar_libro y buscar_libro no funcionan como se esperaba")

    # Prueba 7: Propiedad cantidad_libros
    try:
        biblioteca = Biblioteca("Pequeña Biblioteca")
        assert biblioteca.cantidad_libros == 0
        biblioteca.agregar_libro(Libro("Libro 1", "Autor 1", 100))
        biblioteca.agregar_libro(Libro("Libro 2", "Autor 2", 200))
        assert biblioteca.cantidad_libros == 2
        print("✅ Prueba 7 pasada: La propiedad cantidad_libros funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: La propiedad cantidad_libros no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las clases y métodos están correctamente implementados.")
        print("Has demostrado un buen entendimiento de los conceptos básicos de POO en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
