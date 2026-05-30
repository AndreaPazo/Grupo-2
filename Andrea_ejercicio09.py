# Ecuación Cuadrática ax²+bx+c=0
# Resolver una ecuación cuadrática de la forma ax² + bx + c = 0. 
# Manejar los tres casos: dos raíces reales, una raíz doble y raíces complejas.

import math
import cmath

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    print("No es una ecuación cuadrática.")
else:
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("Dos raíces reales:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif discriminante == 0:
        x = -b / (2*a)
        print("Raíz doble:")
        print("x =", x)

    else:
        x1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2*a)
        print("Raíces complejas:")
        print("x1 =", x1)
        print("x2 =", x2)