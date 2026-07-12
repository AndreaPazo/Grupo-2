# Crea un programa que muestre un menú continuo con tres opciones:
# 1. Calcular área de un cuadrado,
# 2. Calcular área de un círculo y
# 3. Salir.
# Si se elige la opción 1, solicita el lado e imprime el área. Si se elige la opción 2,
# solicita el radio e imprime el área. Si se introduce una opción no válida,muestra un mensaje de error.
# El menú debe repetirse indefinidamente hasta que el usuario escriba la opción 3, que finaliza el programa
# con un mensaje de despedida.
# Haga uso de clases y métodos en su solución.

import math
class Calculador:
    def calcular_area_cuadrado(self, lado):
        self.lado=lado
        return self.lado**2

    def calcular_area_circulo(self, radio):
        return math.pi * (radio ** 2)
while True:
    print("="*20)
    print("MENÚ DE OPCIONES:")
    print("1. Calcular el área de un cuadrado")
    print("2. Calcular área de un círculo")
    print("3. Salir")
    opcion = input("Ingrese una opción (1, 2 o 3): ")
    if opcion == "1":
        lado = float(input("Ingrese el lado del cuadrado: "))
        calculador = Calculador()
        area_cuadrado = calculador.calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area_cuadrado:.2f}")
    elif opcion == "2":
        radio = float(input("Ingrese el radio del círculo: "))
        calculador = Calculador()
        area_circulo = calculador.calcular_area_circulo(radio)
        print(f"El área del círculo es: {area_circulo:.2f}")
    elif opcion == "3":
        print("Saliste del menú")
        break
    else:
        print("¡ERROR!Opción no válida. Ingrese una opción válida.")
