# Crea una función que reciba un entero y retorne True si es par 
# o False si es impar. Pruébala con condicional.

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Ingresa un número entero: "))

if par(num):
    print("El número es par")
else:
    print("El número es impar")