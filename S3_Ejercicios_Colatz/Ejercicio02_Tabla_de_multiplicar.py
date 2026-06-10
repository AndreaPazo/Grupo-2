# # Pedir al usuario un numero e indica si es positivo, negativo o cero

# num = float(input("Ingrese un número: "))

# if num > 0:
#     clasificacion = "positivo"
# elif num < 0:
#     clasificacion = "negativo"
# else:
#     clasificacion = "cero."

#Mostrar resultado
# print (f"El número {num} es {clasificacion}")

# print("-----------")

# Muestra la tabla de multiplicar de un numero ingresado por el usuario (del 1 al 10)

while True:
    num = int(input("Ingrese un número del 1 al 10: "))

    if num > 10:
        print("Número inválido. Intente nuevamente.")
        continue

    for i in range(1, 11):
        print(f"{i} x {num} = {i * num}")
    break

