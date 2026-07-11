# Elaborar un algoritmo que permita elegir entre 3 figuras: circulo, cuadrilátero o triangulo (rectángulo).
# Dependiendo de la figura elegida, solicitará el radio, los lados del cuadrilátero, los lados del cuadrilátero o la base y altura respectivamente
# Una vez ingresado los datos, debera mostrar el perimetro y area de la figura elegida.
# finalmente consultara si desea algun otro calculo, y de responder si, debera elegir nuevamente la figura y los siguiente pasos.
# trabajar el algoritmo aplicando clases y metodos.
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrilatero:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return self.lado1 * self.lado2

    def perimetro(self):
        return 2 * (self.lado1 + self.lado2)

class Triangulo_rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa 

while True:
    print("======= DATOS DE FIGURA =======")
    print("Seleccione una figura: ")
    print("1. Circulo")
    print("2. Cuadrilátero")
    print("3. Triángulo Rectángulo")
    print("=" * 30)
    figura = input("Ingrese el número de la figura elegida: ")

    if figura == "1":
        radio = float(input("Ingrese el radio del círculo: "))
        circulo = Circulo(radio)
        print(f"Área del círculo     : {circulo.area():>4.2f}")
        print(f"Perímetro del círculo: {circulo.perimetro():>4.2f}")

    elif figura == "2":
        lado1 = float(input("Ingrese el primer lado del cuadrilátero: "))
        lado2 = float(input("Ingrese el segundo lado del cuadrilátero: "))
        cuadrilatero = Cuadrilatero(lado1, lado2)
        print(f"Área del cuadrilátero     : {cuadrilatero.area():>4.2f}")
        print(f"Perímetro del cuadrilátero: {cuadrilatero.perimetro():>4.2f}")

    elif figura == "3":
        base = float(input("Ingrese la base del triángulo rectángulo: "))
        altura = float(input("Ingrese la altura del triángulo rectángulo: "))
        triangulo = Triangulo_rectangulo(base, altura)
        print(f"Área del triángulo rectángulo     : {triangulo.area():>4.2f}")
        print(f"Perímetro del triángulo rectángulo: {triangulo.perimetro():>4.2f}")

    else:
        print("Opción no válida. Elija nuevamente.")

    continuar = input("¿Desea realizar otro cálculo? (si/no): ")
    if continuar.lower() != "si":
        break
