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
            print("La edad no puede ser negativa.")
        else:
            self.__edad = edad
    
    def set_dni(self, dni):
        if len(dni) != 8:
            print("El DNI debe tener 8 digitos")
        else:
            self.__dni = dni


    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print(f"nombre: {self.__nombre}")
        print(f"edad: {self.__edad}")
        print(f"dni: {self.__dni}")

    def es_mayor_de_edad(self):
        return self.__edad > 18
    
persona = Persona ("juan", 16, "12345678")

persona.mostrar()
if persona.es_mayor_de_edad():
    print('Es mayor de edad')
else:
    print("No es mayor de edad")

