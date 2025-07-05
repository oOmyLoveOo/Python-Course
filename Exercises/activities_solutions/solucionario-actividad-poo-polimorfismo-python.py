# Solucionario: Polimorfismo en Programación Orientada a Objetos en Python

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        raise NotImplementedError("Subclase debe implementar el método abstracto")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

class Pato(Animal):
    def hacer_sonido(self):
        return "Cuac!"

def sonido_animal(animal):
    return animal.hacer_sonido()

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14 * self.radio ** 2

def calcular_area(figura):
    return figura.area()

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 7

    print("Evaluando la implementación...\n")

    # Prueba 1: Polimorfismo de método con animales
    try:
        perro = Perro("Firulais")
        gato = Gato("Michi")
        pato = Pato("Donald")
        assert perro.hacer_sonido() == "Guau!"
        assert gato.hacer_sonido() == "Miau!"
        assert pato.hacer_sonido() == "Cuac!"
        print("✅ Prueba 1 pasada: Los métodos hacer_sonido están correctamente implementados")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: Los métodos hacer_sonido no están correctamente implementados")

    # Prueba 2: Función sonido_animal
    try:
        perro = Perro("Bobby")
        gato = Gato("Garfield")
        assert sonido_animal(perro) == "Guau!"
        assert sonido_animal(gato) == "Miau!"
        print("✅ Prueba 2 pasada: La función sonido_animal funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: La función sonido_animal no funciona como se esperaba")

    # Prueba 3: Representación de string de Punto
    try:
        punto = Punto(3, 4)
        assert str(punto) == "(3, 4)"
        print("✅ Prueba 3 pasada: La representación de string de Punto es correcta")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: La representación de string de Punto no es correcta")

    # Prueba 4: Suma de Puntos
    try:
        p1 = Punto(1, 2)
        p2 = Punto(3, 4)
        p3 = p1 + p2
        assert isinstance(p3, Punto)
        assert p3.x == 4 and p3.y == 6
        print("✅ Prueba 4 pasada: La suma de Puntos funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: La suma de Puntos no funciona como se esperaba")

    # Prueba 5: Área de Rectángulo
    try:
        rectangulo = Rectangulo(5, 4)
        assert rectangulo.area() == 20
        print("✅ Prueba 5 pasada: El cálculo del área del Rectángulo es correcto")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: El cálculo del área del Rectángulo no es correcto")

    # Prueba 6: Área de Círculo
    try:
        circulo = Circulo(3)
        assert abs(circulo.area() - 28.26) < 0.01
        print("✅ Prueba 6 pasada: El cálculo del área del Círculo es correcto")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: El cálculo del área del Círculo no es correcto")

    # Prueba 7: Función calcular_area
    try:
        rectangulo = Rectangulo(6, 3)
        circulo = Circulo(2)
        assert calcular_area(rectangulo) == 18
        assert abs(calcular_area(circulo) - 12.56) < 0.01
        print("✅ Prueba 7 pasada: La función calcular_area funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: La función calcular_area no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las clases y métodos están correctamente implementados.")
        print("Has demostrado un buen entendimiento de los conceptos de polimorfismo en POO en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
