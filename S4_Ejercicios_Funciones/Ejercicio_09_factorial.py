# EJERCICIO 09
# Crea una función que calcule el factorial de n (n!)
# usando un bucle while. Valida que n sea no negativo.

def calcular_factorial(n):
    # Validamos que el número no sea negativo
    if n < 0:
        return "Error: el número no debe ser negativo"

    # factorial empieza en 1 porque se irá multiplicando
    factorial = 1

    # contador servirá para multiplicar desde 1 hasta n
    contador = 1

    # Bucle while para calcular el factorial
    while contador <= n:
        factorial *= contador
        contador += 1

    # Retornamos el resultado final
    return factorial


# Programa principal
numero = int(input("Ingrese un número no negativo: "))

resultado = calcular_factorial(numero)

print("El factorial es:", resultado)