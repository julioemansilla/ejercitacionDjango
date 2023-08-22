'''Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
titular (que es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. 

Crear los siguientes métodos para la clase: 
 Un constructor, donde los datos pueden estar vacíos. 
 Los setters y getters para cada uno de los atributos. E
l atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
 mostrar(): Muestra los datos de la cuenta. 
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
no se hará nada. 
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.'''


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular.nombre

    def set_titular(self, nombre):
        self.titular.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

    def mostrar(self):
        print(f"Titular: {self.get_titular()}")
        print(f"Cantidad: {self.cantidad:.2f}")  # Muestra la cantidad con dos decimales

# Crear una instancia de Persona y una instancia de Cuenta
titular_persona = Persona("Juan Pérez")
cuenta_juan = Cuenta(titular_persona, 1000.0)

# Mostrar los datos iniciales de la cuenta
cuenta_juan.mostrar()

# Realizar operaciones en la cuenta
cuenta_juan.ingresar(500)
cuenta_juan.retirar(200)

# Mostrar los datos actualizados de la cuenta
cuenta_juan.mostrar()

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        edad = 2023 - int(self.titular.nombre.split()[-1])  # Suponiendo que el último elemento del nombre sea el año de nacimiento
        return 18 <= edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para realizar retiros.")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.bonificacion}%")

# Crear una instancia de Persona y una instancia de CuentaJoven
titular_joven = Persona("Ana González 2000")
cuenta_ana = CuentaJoven(titular_joven, 1500.0, 5.0)

# Mostrar los datos iniciales de la cuenta joven
cuenta_ana.mostrar()

# Realizar operaciones en la cuenta joven (retirar solo si es titular válido)
cuenta_ana.retirar(200)

# Mostrar los datos actualizados de la cuenta joven
cuenta_ana.mostrar()
