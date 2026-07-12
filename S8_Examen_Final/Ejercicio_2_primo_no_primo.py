# Crea un programa que solicite un número al usuario, luego de ello usted deberá indicar si el número ingresado
# es primo o no es primo.
# Para esta solución deberá hacer uso de funciones.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = int(input("Ingrese un número: "))
if es_primo(numero)== True:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
