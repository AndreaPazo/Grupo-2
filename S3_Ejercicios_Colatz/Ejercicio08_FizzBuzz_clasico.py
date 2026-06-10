# Del 1 al 50: Fizz (÷3), Buzz (÷5), FizzBuzz (÷ambos), o el número.

# Recorremos los números del 1 al 50
for num in range(1, 51):

    #Primero verificamos si cumple ambas condiciones, si es multiplo de 3 y 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")

    # Si no cumple ambas, revisamos si es multiplo de 3
    elif num % 3 == 0:
        print("Fizz", end=" ")

    # De lo contrario, revisamos si es multiplo de 5
    elif num % 5 == 0:
        print("Buzz", end=" ")

    # Si no cumple ninguna de las anteriores, imprimimos el número 
    else:
        #Usamos condicional anidada para dar formato
        if num < 10:
            print(num, end="  ")

        else:
            print(num, end=" ")

