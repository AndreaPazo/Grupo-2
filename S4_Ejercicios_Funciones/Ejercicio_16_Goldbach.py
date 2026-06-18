# EJERCICIO
# Todo número par mayor que 2 se puede expresar
# como la suma de dos números primos.
# Conjetura de Goldbach.

def es_primo(numero):
    # Un número menor que 2 no es primo
    if numero < 2:
        return False

    divisor = 2

    # Verificamos si tiene divisores entre 2 y numero - 1
    while divisor < numero:
        if numero % divisor == 0:
            return False

        # Aumentamos el divisor en 1
        divisor += 1

    return True


def hallar_par_primos(numero):
    # Empezamos probando desde 2
    primo1 = 2

    while primo1 < numero:
        primo2 = numero - primo1

        # Si ambos son primos, encontramos el par
        if es_primo(primo1) and es_primo(primo2):
            print(numero, "=", primo1, "+", primo2)
            return True

        # Probamos con el siguiente posible primo
        primo1 += 1

    return False


def comprobar_goldbach(limite):
    # La conjetura empieza desde el primer par mayor que 2, que es 4
    numero = 4

    print("Comprobando la conjetura de Goldbach hasta", limite)

    while numero <= limite:
        # Solo evaluamos números pares mayores que 2
        if numero % 2 == 0:
            hallar_par_primos(numero)

        # Pasamos al siguiente número
        numero += 1


# Programa principal
n = int(input("Ingrese un número límite: "))

comprobar_goldbach(n)