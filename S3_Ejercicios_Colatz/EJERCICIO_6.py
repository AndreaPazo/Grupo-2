
#6Dibuja una pirámide de N filas usando bucles for anidados.
 
n = int(input("Ingrese el número de filas: "))

for i in range(1, n + 1):

    # Espacios
    for E in range(n - i):
        print(" ", end="")

    # Asteriscos
    for A in range(2 * i - 1):
        print("*", end="")

    print()


# for i in range(1, n + 1):  # Línea 4 → for externo: controla las filas
#     espacios = " " * (n - i)  # Línea 6 → spaces = n-i (disminuye por fila)
#     asteriscos = "*" * (2 * i - 1)  # Línea 8 → asteriscos = 2*i-1 (1,3,5,7...)
#     print(espacios + asteriscos) 