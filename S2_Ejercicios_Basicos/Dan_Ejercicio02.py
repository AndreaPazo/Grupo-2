#import math: para usar funciones que Python no tiene y en este caso para usar la constante pi 
import math
#Se pide calcular el área y el perímetro de un círculo ingresando la medidad del radio
rad = float(input("Ingrese el radio: "))
area = math.pi * rad ** 2
peri = 2*math.pi*rad
print(f"El área del círculo es {area:.2f} y el perímetro es {peri:.2f}")