#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
#Construya los siguientes métodos para la clase:

    # Un constructor, donde los datos pueden estar vacíos.
    # Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    # mostrar(): Muestra los datos de la persona.
    # Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre="", edad = 0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if edad < 0:
            print("La edad no puede ser negativa")
        else:
            self.__edad = edad

    def get_edad(self):
        return self.__edad

    def set_dni (self, dni):
        if len(dni) != 8:
            print("El dni debe tener 8 digitos.")
        else:
            self.__dni = dni

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

    def es_mayor_de_edad(self):
        return self.__edad >= 18

persona = Persona()

persona.set_nombre("juan")
persona.set_edad(25)
persona.set_dni("12345678")

persona.mostrar()

if persona.es_mayor_de_edad():
    print("Es mayor de Edad")
else:
    print("No es mayor de edad")






