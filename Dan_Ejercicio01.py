#Se pide ingresar dos números y hacer las 4 operaciones básicas
num1 = float(input("Ingrese el número 1: "))
num2 = float(input("Ingrese el número 2: "))
print(f"La suma es {num1+num2}")
print("La resta es ", num1-num2)
print("La multiplicación es ", num2*num1)
#Además, si el segundo número es 0 debe salir un mensaje de "La división no es válida."
if num2 == 0:
    print("La división no es válida.")
else:
    print(f"La división es {num2/num1}")