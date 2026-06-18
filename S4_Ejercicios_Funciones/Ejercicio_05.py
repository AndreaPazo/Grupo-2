# Crea una función void que reciba un número y 
# muestre su tabla de multiplicar completa del 1 al 10.

def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Ingrese un número: "))

tabla_multiplicar(num)