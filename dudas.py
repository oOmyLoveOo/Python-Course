✅ Forma en una línea (más común y clara):
python
Copiar
Editar
def buscar_libro(self, titulo):
    return next((libro for libro in self.libros if libro.titulo == titulo), None)
next() obtiene el primer elemento del generador que cumpla la condición.

El segundo argumento (None) es el valor por defecto si no se encuentra ningún libro.

✅ Alternativas (no necesariamente recomendadas en 1 línea, pero posibles)
Usando filter() y next():
python
Copiar
Editar
def buscar_libro(self, titulo):
    return next(filter(lambda libro: libro.titulo == titulo, self.libros), None)
Similar a la anterior, pero con filter() y lambda