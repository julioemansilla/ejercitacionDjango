#Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto 
#en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, 
#iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

#Implementacion Iterativa
def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Error: No es un valor Entero. Intente nuevamente.")

entero = get_int()
print("Ha ingresado el valor entero: ", entero)