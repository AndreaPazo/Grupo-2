# Bucle que obliga al usuario a ingresar un número entero positivo > 1
while True:
    num = int(input("Ingrese un número entero positivo mayor a 1: "))
    if num > 1:
        break

print(num)

# Creamos el bucle hasta que el número sea = 1
while num != 1:

    #Evaluamos si es par, dividimos entre 2
    if num % 2 == 0:
        num = num // 2
        #Sino, es inpar y por lo tanto multiplicamos por 3 y le sumamos 1
    else:
        num = num * 3 + 1

    print(num)

