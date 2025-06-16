# Actividad: POO y Herencia en Python - Sistema de Biblioteca Avanzado

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada clase y método.
2. Completa los espacios marcados con ___ usando los conceptos de POO y herencia apropiados.
3. No modifiques los nombres de las clases y métodos existentes.
4. Una vez que hayas completado todo, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

class ElementoBiblioteca:
    """
    Clase base para todos los elementos de la biblioteca.
    
    Atributos:
    - titulo (str): El título del elemento.
    - codigo (str): Un código único para el elemento.
    - prestado (bool): Indica si el elemento está prestado o no.
    """
    
    def __init__(self, titulo, codigo):
        """
        Inicializa un nuevo ElementoBiblioteca.
        """
        self.titulo = titulo
        self.codigo = codigo
        self.prestado = False
    
    def prestar(self):
        """
        Marca el elemento como prestado si no lo está ya.
        Retorna True si se pudo prestar, False si ya estaba prestado.
        """
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        """
        Marca el elemento como devuelto si estaba prestado.
        Retorna True si se pudo devolver, False si no estaba prestado.
        """
        if self.prestado:
            self.prestado = False
            return True
        return False
    
    def __str__(self):
        """
        Retorna una representación en string del elemento.
        Debe incluir el título, código y estado de préstamo.
        """
        return f"{self.__class__.__name__}: {self.titulo}, Código: {self.codigo}, Prestado: {"Si" if self.prestado else "No"}"

class Libro(ElementoBiblioteca):
    """
    Representa un libro en la biblioteca.
    
    Atributos adicionales:
    - autor (str): El autor del libro.
    - num_paginas (int): El número de páginas del libro.
    """
    
    def __init__(self, titulo, codigo, autor, num_paginas):
        """
        Inicializa un nuevo Libro.
        """
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas
    
    def __str__(self):
        """
        Retorna una representación en string del libro.
        Debe incluir la información de ElementoBiblioteca más el autor y número de páginas.
        """
        return f"{super().__str__()}, Autor: {self.autor}, Páginas: {self.num_paginas}"

class Revista(ElementoBiblioteca):
    """
    Representa una revista en la biblioteca.
    
    Atributos adicionales:
    - numero (int): El número de la revista.
    - mes (str): El mes de publicación.
    - ano (int): El año de publicación.
    """
    
    def __init__(self, titulo, codigo, numero, mes, ano):
        """
        Inicializa una nueva Revista.
        """
        super().__init__(titulo, codigo)
        self.numero = numero
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        """
        Retorna una representación en string de la revista.
        Debe incluir la información de ElementoBiblioteca más el número, mes y año.
        """
        return f"{super().__str__()}, Número: {self.numero}, Mes: {self.mes}, Año: {self.ano}"

class DVD(ElementoBiblioteca):
    """
    Representa un DVD en la biblioteca.
    
    Atributos adicionales:
    - director (str): El director de la película.
    - duracion (int): La duración en minutos.
    """
    
    def __init__(self, titulo, codigo, director, duracion):
        """
        Inicializa un nuevo DVD.
        """
        super().__init__(titulo, codigo)
        self.director = director
        self.duracion = duracion
    
    def __str__(self):
        """
        Retorna una representación en string del DVD.
        Debe incluir la información de ElementoBiblioteca más el director y duración.
        """
        return f"{super().__str__()}, Director: {self.director}, Duración: {self.duracion} minutos"

class Biblioteca:
    """
    Representa una biblioteca que contiene varios tipos de elementos.
    
    Atributos:
    - nombre (str): El nombre de la biblioteca.
    - elementos (list): Una lista de objetos ElementoBiblioteca.
    """
    
    def __init__(self, nombre):
        """
        Inicializa una nueva Biblioteca.
        """
        self.nombre = nombre
        self.elementos = []
    
    def agregar_elemento(self, elemento):
        """
        Agrega un elemento a la biblioteca.
        
        Parámetros:
        - elemento (ElementoBiblioteca): El elemento a agregar.
        """
        return self.elementos.append(elemento)
    
    def buscar_elemento(self, codigo):
        """
        Busca un elemento por su código.
        
        Parámetros:
        - codigo (str): El código del elemento a buscar.
        
        Retorna el elemento si se encuentra, None en caso contrario.
        """
        for elemento in self.elementos:
            if elemento.codigo == codigo:
                return elemento
        return None
    
    
    def prestar_elemento(self, codigo):
        """
        Presta un elemento de la biblioteca si está disponible.
        
        Parámetros:
        - codigo (str): El código del elemento a prestar.
        
        Retorna True si se pudo prestar, False en caso contrario.
        """
        elemento = self.buscar_elemento(codigo)
        if elemento:
            return elemento.prestar()
        return False
    
    def devolver_elemento(self, codigo):
        """
        Devuelve un elemento prestado a la biblioteca.
        
        Parámetros:
        - codigo (str): El código del elemento a devolver.
        
        Retorna True si se pudo devolver, False en caso contrario.
        """
        elemento = self.buscar_elemento(codigo)
        if elemento:
            return elemento.devolver()
        return False

    
    @property
    def cantidad_elementos(self):
        """
        Propiedad que devuelve la cantidad total de elementos en la biblioteca.
        """
        return len(self.elementos)
    
    @property
    def cantidad_prestados(self):
        """
        Propiedad que devuelve la cantidad de elementos prestados.
        """
        return sum(1 for elemento in self.elementos if elemento.prestado)

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 10

    print("Evaluando la implementación...\n")

    # Prueba 1: Creación de elementos
    try:
        libro = Libro("El Quijote", "L001", "Miguel de Cervantes", 863)
        revista = Revista("National Geographic", "R001", 255, "Marzo", 2023)
        dvd = DVD("El Padrino", "D001", "Francis Ford Coppola", 175)
        assert isinstance(libro, ElementoBiblioteca)
        assert isinstance(revista, ElementoBiblioteca)
        assert isinstance(dvd, ElementoBiblioteca)
        print("✅ Prueba 1 pasada: Las clases heredan correctamente de ElementoBiblioteca")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: Problema con la herencia de ElementoBiblioteca")

    # Prueba 2: Métodos de ElementoBiblioteca
    try:
        elemento = ElementoBiblioteca("Prueba", "T001")
        assert elemento.prestar() == True
        assert elemento.prestar() == False
        assert elemento.devolver() == True
        assert elemento.devolver() == False
        print("✅ Prueba 2 pasada: Los métodos de ElementoBiblioteca funcionan correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: Problemas con los métodos de ElementoBiblioteca")

    # Prueba 3: Representación en string
    try:
        libro = Libro("Cien años de soledad", "L002", "Gabriel García Márquez", 417)
        assert str(libro) == "Libro: Cien años de soledad, Código: L002, Prestado: No, Autor: Gabriel García Márquez, Páginas: 417"
        print("✅ Prueba 3 pasada: La representación en string de Libro es correcta")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: Problema con la representación en string de Libro")

    # Prueba 4: Creación de Biblioteca
    try:
        biblioteca = Biblioteca("Biblioteca Central")
        assert biblioteca.nombre == "Biblioteca Central"
        assert biblioteca.cantidad_elementos == 0
        print("✅ Prueba 4 pasada: La clase Biblioteca se inicializa correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: Problema con la inicialización de Biblioteca")

    # Prueba 5: Agregar elementos a la Biblioteca
    try:
        biblioteca = Biblioteca("Biblioteca Central")
        libro = Libro("1984", "L003", "George Orwell", 328)
        revista = Revista("Time", "R002", 100, "Enero", 2024)
        biblioteca.agregar_elemento(libro)
        biblioteca.agregar_elemento(revista)
        assert biblioteca.cantidad_elementos == 2
        print("✅ Prueba 5 pasada: Se pueden agregar elementos a la Biblioteca")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: Problema al agregar elementos a la Biblioteca")

    # Prueba 6: Buscar elementos en la Biblioteca
    try:
        biblioteca = Biblioteca("Biblioteca Central")
        libro = Libro("El Hobbit", "L004", "J.R.R. Tolkien", 310)
        biblioteca.agregar_elemento(libro)
        assert biblioteca.buscar_elemento("L004") == libro
        assert biblioteca.buscar_elemento("L005") == None
        print("✅ Prueba 6 pasada: La búsqueda de elementos funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Problema con la búsqueda de elementos")

    # Prueba 7: Prestar y devolver elementos
    try:
        biblioteca = Biblioteca("Biblioteca Central")
        dvd = DVD("Matrix", "D002", "Hermanas Wachowski", 136)
        biblioteca.agregar_elemento(dvd)
        assert biblioteca.prestar_elemento("D002") == True
        assert biblioteca.prestar_elemento("D002") == False
        assert biblioteca.devolver_elemento("D002") == True
        assert biblioteca.devolver_elemento("D002") == False
        print("✅ Prueba 7 pasada: El préstamo y devolución de elementos funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: Problema con el préstamo y devolución de elementos")

    # Prueba 8: Cantidad de elementos prestados
    try:
        biblioteca = Biblioteca("Biblioteca Central")
        libro1 = Libro("Libro1", "L101", "Autor1", 200)
        libro2 = Libro("Libro2", "L102", "Autor2", 300)
        biblioteca.agregar_elemento(libro1)
        biblioteca.agregar_elemento(libro2)
        biblioteca.prestar_elemento("L101")
        assert biblioteca.cantidad_prestados == 1
        biblioteca.prestar_elemento("L102")
        assert biblioteca.cantidad_prestados == 2
        biblioteca.devolver_elemento("L101")
        assert biblioteca.cantidad_prestados == 1
        print("✅ Prueba 8 pasada: El conteo de elementos prestados funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 8 fallida: Problema con el conteo de elementos prestados")

    # Prueba 9: Revista
    try:
        revista = Revista("Science", "R003", 378, "Abril", 2024)
        assert str(revista) == "Revista: Science, Código: R003, Prestado: No, Número: 378, Mes: Abril, Año: 2024"
        print("✅ Prueba 9 pasada: La clase Revista funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 9 fallida: Problema con la clase Revista")

    # Prueba 10: DVD
    try:
        dvd = DVD("Inception", "D003", "Christopher Nolan", 148)
        assert str(dvd) == "DVD: Inception, Código: D003, Prestado: No, Director: Christopher Nolan, Duración: 148 minutos"
        print("✅ Prueba 10 pasada: La clase DVD funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 10 fallida: Problema con la clase DVD")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las clases y métodos están correctamente implementados.")
        print("Has demostrado un buen entendimiento de los conceptos de POO y herencia en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
