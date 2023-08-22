#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene 
#y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.lower() #Convertimos a minúsculas para considerarlas iguales ya que Python diferencia m/M
        if palabra in frecuencia:
            frecuencia[palabra] +=1
        else:
            frecuencia[palabra] = 1
    return frecuencia

cadena_input = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena_input)

print("frecuencia de palabras: ")
for palabra, cantidad in resultado.items():
    print(f"'{palabra}': {cantidad}")