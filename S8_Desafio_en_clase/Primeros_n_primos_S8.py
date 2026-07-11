# El usuario ingresa un número y debe mostrar los n primeros número primos

print("=" * 31)
print("  SUMATORIA DE NÚMEROS PRIMOS  ")
print("=" * 31)

def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return
    return

def imprimir_primos(n):
    contador = 0
    num = 2

    while contador < n:
        if es_primo(num):
            print(num)
            contador += 1
        num += 1

usuario = int(input("Ingrese una cantidad de números primos: "))
imprimir_primos(usuario)
