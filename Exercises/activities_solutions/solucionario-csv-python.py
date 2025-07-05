# Actividad: Procesamiento de Archivos CSV en Python

import csv
import json

def crear_csv_ejemplo(nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Fecha', 'Vendedor', 'Producto', 'Cantidad'])
        escritor.writerows([
            ['2023-01-15', 'Juan', 'Laptop', 2],
            ['2023-01-16', 'María', 'Teléfono', 3],
            ['2023-01-17', 'Pedro', 'Tablet', 1],
            ['2023-01-18', 'Juan', 'Teléfono', 2],
            ['2023-01-19', 'María', 'Laptop', 1]
        ])

def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def calcular_ventas_totales(datos):
    return sum(float(fila['Cantidad']) for fila in datos)

def encontrar_mejor_vendedor(datos):
    ventas_por_vendedor = {}
    for fila in datos:
        vendedor = fila['Vendedor']
        cantidad = int(fila['Cantidad'])
        ventas_por_vendedor[vendedor] = ventas_por_vendedor.get(vendedor, 0) + cantidad
    return max(ventas_por_vendedor, key=ventas_por_vendedor.get)

def ventas_por_producto(datos):
    ventas = {}
    for fila in datos:
        producto = fila['Producto']
        cantidad = int(fila['Cantidad'])
        ventas[producto] = ventas.get(producto, 0) + cantidad
    return ventas

def guardar_resumen_json(nombre_archivo, resumen):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(resumen, archivo, indent=2)

def procesar_ventas(archivo_entrada, archivo_salida):
    datos = leer_csv(archivo_entrada)
    ventas_totales = calcular_ventas_totales(datos)
    mejor_vendedor = encontrar_mejor_vendedor(datos)
    ventas_producto = ventas_por_producto(datos)
    
    resumen = {
        "ventas_totales": ventas_totales,
        "mejor_vendedor": mejor_vendedor,
        "ventas_por_producto": ventas_producto
    }
    
    guardar_resumen_json(archivo_salida, resumen)

def verificar_implementacion():
    print("Evaluando la implementación...\n")
    puntuacion = 0
    total_pruebas = 6

    # Prueba 1: Crear y leer CSV
    try:
        crear_csv_ejemplo("ventas.csv")
        datos = leer_csv("ventas.csv")
        assert len(datos) == 5
        assert len(datos[0]) == 4
        print("✅ Prueba 1 pasada: Crear y leer CSV funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: Problema con crear o leer CSV")

    # Prueba 2: Calcular ventas totales
    try:
        datos = leer_csv("ventas.csv")
        total = calcular_ventas_totales(datos)
        assert isinstance(total, float)
        assert total > 0
        print("✅ Prueba 2 pasada: Cálculo de ventas totales funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: Problema con el cálculo de ventas totales")

    # Prueba 3: Encontrar mejor vendedor
    try:
        datos = leer_csv("ventas.csv")
        mejor = encontrar_mejor_vendedor(datos)
        assert isinstance(mejor, str)
        assert len(mejor) > 0
        print("✅ Prueba 3 pasada: Encontrar mejor vendedor funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: Problema al encontrar el mejor vendedor")

    # Prueba 4: Ventas por producto
    try:
        datos = leer_csv("ventas.csv")
        ventas_prod = ventas_por_producto(datos)
        assert isinstance(ventas_prod, dict)
        assert len(ventas_prod) > 0
        print("✅ Prueba 4 pasada: Ventas por producto funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: Problema con ventas por producto")

    # Prueba 5: Guardar resumen JSON
    try:
        resumen = {"test": "datos"}
        guardar_resumen_json("resumen_test.json", resumen)
        with open("resumen_test.json", "r") as f:
            datos_guardados = json.load(f)
        assert datos_guardados == resumen
        print("✅ Prueba 5 pasada: Guardar resumen JSON funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: Problema al guardar resumen JSON")

    # Prueba 6: Proceso completo
    try:
        procesar_ventas("ventas.csv", "resumen_ventas.json")
        with open("resumen_ventas.json", "r") as f:
            resumen = json.load(f)
        assert "ventas_totales" in resumen
        assert "mejor_vendedor" in resumen
        assert "ventas_por_producto" in resumen
        print("✅ Prueba 6 pasada: Proceso completo funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Problema con el proceso completo")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las funciones están correctamente implementadas.")
        print("Has demostrado un buen entendimiento del procesamiento de archivos CSV y JSON en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
