'''Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven 
que deriva de la clase creada en el punto 7. 
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación 
que estará expresada en tanto por ciento. 

Crear los siguientes métodos para la clase: 
 Un constructor.
 Los setters y getters para el nuevo atributo. 
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad 
pero menor de 25 años y falso en caso contrario. 
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.'''

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
