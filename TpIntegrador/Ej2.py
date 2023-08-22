#Escribir una función que calcule el mínimo común múltiplo entre dos números

def MCD(a, b):
    while b != 0:
        a, b = b, a % b     # Intercambio de valores entre a y b, actualizando b con el residuo de a % b
    return a

def mcm(a,b):
    return (a * b) // MCD(a, b)

numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingresar el segundo número: "))

resultado = mcm(numero1, numero2)

print(f"El mínimo comun multiplo entre {numero1} y {numero2} es: {resultado}")