# Actividad: Encapsulación en Programación Orientada a Objetos en Python

"""
Instrucciones para el estudiante:

1. Lee cuidadosamente los comentarios en cada función y clase.
2. Completa los espacios marcados con ___ usando los conceptos de encapsulación en POO.
3. No modifiques los nombres de las clases y métodos existentes.
4. Una vez que hayas completado todo, ejecuta este script para verificar tus soluciones.

¡Buena suerte!
"""

class CuentaBancaria:
    """
    Representa una cuenta bancaria.
    
    Atributos:
    - titular (str): El nombre del titular de la cuenta.
    - __saldo (float): El saldo actual de la cuenta (privado).
    - __numero_cuenta (str): El número de cuenta (privado).
    
    Completa la clase con el constructor (__init__) y los métodos indicados.
    """
    
    def __init__(self, titular, saldo, numero_cuenta):
        """
        Inicializa un nuevo objeto CuentaBancaria.
        
        El atributo '__saldo' debe inicializarse con el valor proporcionado.
        El atributo '__numero_cuenta' debe ser privado.
        """
        self.titular = titular
        self.__saldo = saldo
        self.__numero_cuenta = numero_cuenta
    
    def __str__(self):
        """
        Devuelve una representación en string de la cuenta.
        
        Debe devolver: "Cuenta de [titular] - Número: [numero_cuenta]"
        """
        return f"Cuenta de {self.titular} - Número: {self.__numero_cuenta}"

    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta.
        
        Parámetros:
        - cantidad (float): La cantidad a depositar.
        
        Debe aumentar el saldo si la cantidad es positiva.
        """
        if cantidad <= 0:
            return 
        self.__saldo += cantidad
            

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta si hay saldo suficiente.
        
        Parámetros:
        - cantidad (float): La cantidad a retirar.
        
        Retorna True si se pudo retirar, False en caso contrario.
        """
        if self.__saldo < cantidad or cantidad <= 0:
            return False
        self.__saldo -= cantidad
        return True

    @property
    def saldo(self):
        """
        Propiedad que devuelve el saldo actual de la cuenta.
        """
        return self.__saldo

    @property
    def numero_cuenta(self):
        """
        Propiedad que devuelve el número de cuenta.
        """
        return self.__numero_cuenta

class Banco:
    """
    Representa un banco que gestiona cuentas bancarias.
    
    Atributos:
    - nombre (str): El nombre del banco.
    - _cuentas (list): Una lista de objetos CuentaBancaria (protegido).
    
    Completa la clase con el constructor y los métodos indicados.
    """
    
    def __init__(self, nombre):
        """
        Inicializa un nuevo objeto Banco.
        
        El atributo '_cuentas' debe inicializarse como una lista vacía.
        """
        self.nombre = nombre
        self._cuentas = []
    
    def agregar_cuenta(self, cuenta):
        """
        Agrega una cuenta al banco.
        
        Parámetros:
        - cuenta (CuentaBancaria): La cuenta a agregar.
        """
        self._cuentas.append(cuenta)
    
    def buscar_cuenta(self, numero_cuenta):
        """
        Busca una cuenta por su número.
        
        Parámetros:
        - numero_cuenta (str): El número de la cuenta a buscar.
        
        Retorna la cuenta si se encuentra, None en caso contrario.
        """
        for cuenta in self._cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None
    
    @property
    def total_fondos(self):
        """
        Propiedad que devuelve el total de fondos en todas las cuentas del banco.
        """
        return sum(cuenta.saldo for cuenta in self._cuentas)

def verificar_implementacion():
    puntuacion = 0
    total_pruebas = 7

    print("Evaluando la implementación...\n")

    # Prueba 1: Creación de una cuenta bancaria
    try:
        cuenta = CuentaBancaria("Juan Pérez", 1000, "1234567890")
        assert cuenta.titular == "Juan Pérez"
        assert cuenta.saldo == 1000
        assert cuenta.numero_cuenta == "1234567890"
        print("✅ Prueba 1 pasada: La clase CuentaBancaria se inicializa correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 1 fallida: La clase CuentaBancaria no se inicializa como se esperaba")

    # Prueba 2: Representación en string de una cuenta
    try:
        cuenta = CuentaBancaria("María López", 500, "0987654321")
        assert str(cuenta) == "Cuenta de María López - Número: 0987654321"
        print("✅ Prueba 2 pasada: El método __str__ de CuentaBancaria funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 2 fallida: El método __str__ de CuentaBancaria no funciona como se esperaba")

    # Prueba 3: Depósito y retiro en cuenta
    try:
        cuenta = CuentaBancaria("Carlos Ruiz", 200, "1357924680")
        cuenta.depositar(300)
        assert cuenta.saldo == 500
        assert cuenta.retirar(200) == True
        assert cuenta.saldo == 300
        assert cuenta.retirar(500) == False
        assert cuenta.saldo == 300
        print("✅ Prueba 3 pasada: Los métodos depositar y retirar funcionan correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 3 fallida: Los métodos depositar y retirar no funcionan como se esperaba")

    # Prueba 4: Encapsulación de atributos en CuentaBancaria
    try:
        cuenta = CuentaBancaria("Ana Martínez", 1500, "2468013579")
        assert not hasattr(cuenta, "__saldo")
        assert not hasattr(cuenta, "__numero_cuenta")
        print("✅ Prueba 4 pasada: Los atributos de CuentaBancaria están correctamente encapsulados")
        puntuacion += 1
    except:
        print("❌ Prueba 4 fallida: Los atributos de CuentaBancaria no están correctamente encapsulados")

    # Prueba 5: Creación de un banco
    try:
        banco = Banco("Banco Python")
        assert banco.nombre == "Banco Python"
        assert len(banco._cuentas) == 0
        print("✅ Prueba 5 pasada: La clase Banco se inicializa correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 5 fallida: La clase Banco no se inicializa como se esperaba")

    # Prueba 6: Agregar y buscar cuentas en el banco
    try:
        banco = Banco("Banco Serpiente")
        cuenta1 = CuentaBancaria("Lucas Gómez", 3000, "1111222233")
        cuenta2 = CuentaBancaria("Elena Torres", 4000, "4444555566")
        banco.agregar_cuenta(cuenta1)
        banco.agregar_cuenta(cuenta2)
        assert banco.buscar_cuenta("1111222233") == cuenta1
        assert banco.buscar_cuenta("4444555566") == cuenta2
        assert banco.buscar_cuenta("9999999999") == None
        print("✅ Prueba 6 pasada: Los métodos agregar_cuenta y buscar_cuenta funcionan correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 6 fallida: Los métodos agregar_cuenta y buscar_cuenta no funcionan como se esperaba")

    # Prueba 7: Propiedad total_fondos
    try:
        banco = Banco("Banco del Curso")
        banco.agregar_cuenta(CuentaBancaria("Pedro Sánchez", 1000, "7777888899"))
        banco.agregar_cuenta(CuentaBancaria("Laura Flores", 2000, "1212343456"))
        assert banco.total_fondos == 3000
        print("✅ Prueba 7 pasada: La propiedad total_fondos funciona correctamente")
        puntuacion += 1
    except:
        print("❌ Prueba 7 fallida: La propiedad total_fondos no funciona como se esperaba")

    print(f"\nPuntuación final: {puntuacion}/{total_pruebas}")
    
    if puntuacion == total_pruebas:
        print("\n¡Felicidades! Todas las clases y métodos están correctamente implementados.")
        print("Has demostrado un buen entendimiento de los conceptos de encapsulación en POO en Python.")
    else:
        print("\nAlgunas partes necesitan revisión. Revisa tu implementación y vuelve a intentarlo.")

# Ejecutar la verificación
if __name__ == "__main__":
    verificar_implementacion()
