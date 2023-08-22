#Escribir una función que calcule el máximo común divisor entre dos números.

def MCD(a, b):
    while b != 0:
        a, b = b, a % b     # Intercambio de valores entre a y b, actualizando b con el residuo de a % b
    return a

numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingresar el segundo número: "))

resultado = MCD(numero1, numero2)

print(f"El máximo comun divisor entre {numero1} y {numero2} es: {resultado}")
 