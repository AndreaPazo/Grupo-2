#PAR O IMPAR
# Solicitar un número entero al usuario y determinar si es par o impar
# Mostrar también si el número es positivo, negativo o cero

num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print (f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")

#Evaluamos si el numero es negativo, positivo o cero
if num < 0:
    print(f"El número {num} es negativo.")
elif num > 0:
    print(f"El número {num} es positivo.")
else:
    print(f"El número {num} es cero.")

