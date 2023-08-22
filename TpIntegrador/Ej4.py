#Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene 
#y la cantidad de veces que aparece (frecuencia). 
#Escribir otra función que reciba el diccionario generado con la función anterior y 
#devuelva una tupla con la palabra más repetida y su frecuencia.

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in frecuencia:
            frecuencia[palabra] +=1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def palabra_mas_repetida(diccionario):
    palabra_max = None
    frecuencia_max = 0

    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia

    if palabra_max is not None:
        return palabra_max, frecuencia_max
    else:
        return None, 0
    
cadena_input = input("Ingrese una cadena de caracteres: ")
resultado_diccionario = contar_palabras(cadena_input)
palabra_repetida, frecuencia_repetida = palabra_mas_repetida(resultado_diccionario)

print("Frecuencia de palabras: ")
for palabra, cantidad in resultado_diccionario.items():
    print(f"'{palabra}': {cantidad}")

if palabra_repetida is not None:
    print(f"'La palabra más repetida es ' {palabra_repetida}' con una frecuencia de {frecuencia_repetida} veces.")
else:
    print("no se encontraron palabras repetidas en la cadena")

