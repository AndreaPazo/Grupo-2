# El usuario ingresa un número y debe mostrar el factorial de ese número
print("=" * 30)
print("==== CALCULO DE FACTORIAL ====")
print("=" * 30)

while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Número inválido. Ingrese un número entero positivo.")
            continue
        else:
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            print(f"El factorial de {numero} es: {factorial}")
            break

    except ValueError:
        print("Texto inválido. Ingrese un número entero positivo.")
