# EJERCICIO 12
# Un número es perfecto si la suma de sus divisores propios
# es igual al mismo número.
# Ejemplo: 6 es perfecto porque 1 + 2 + 3 = 6.

def es_perfecto(numero):
    # Esta variable guardará la suma de los divisores del número
    suma_divisores = 0

    # Empezamos desde 1 porque es el primer divisor propio
    divisor = 1

    # Buscamos divisores menores que el número
    while divisor < numero:
        # Si el residuo es 0, significa que divide exactamente al número
        if numero % divisor == 0:
            suma_divisores += divisor

        # Pasamos al siguiente posible divisor
        divisor += 1

    # Retorna True si el número es perfecto
    return suma_divisores == numero


def buscar_perfectos(n):
    numero = 1
    encontrados = 0

    # Recorremos los números desde 1 hasta n
    while numero <= n:
        if es_perfecto(numero):
            # Si es el primer número perfecto encontrado,
            # recién mostramos el encabezado.
            if encontrados == 0:
                print("Números perfectos hasta", n, ":")

            print(numero)
            encontrados += 1

        numero += 1

    # Si no se encontró ningún número perfecto, mostramos solo este mensaje
    if encontrados == 0:
        print("No se encontraron números perfectos hasta", n)


# Programa principal
n = int(input("Ingrese un número límite: "))

buscar_perfectos(n)