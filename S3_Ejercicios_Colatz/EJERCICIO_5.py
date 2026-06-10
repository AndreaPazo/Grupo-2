
#Determina si un número es primo usando for con condicionales anidadas.

#solicitar al usuario que ingrese un número

numero=int(input("Ingrese un número: "))

#verificar si el número es menor que 2,  se define como un número natural que tiene exactamente dos divisores positivos: 1 y él mismo.

if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    #verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")