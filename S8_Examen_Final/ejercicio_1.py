# Realizar un algoritmo que solicite al usuario la longitud de los lados de un triángulo, luego deberá indicar
# si se puede formar un triángulo con los lados ingresados, para dicha validación debe cumplirse lo siguiente:
# a+b>c
# a+c>b
# b+c>a
# Donde a, b y c son los lados del triángulo.
# El programa debe arrojar como resultado si se puede formar un triángulo con los lados ingresados.


lado1 = float(input("Ingrese la longitud del lado 1 del triángulo: "))
lado2 = float(input("Ingrese la longitud del lado 2 del triángulo: "))                      
lado3 = float(input("Ingrese la longitud del lado 3 del triángulo: "))     

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Sí se puede formar un triángulo con los lados que ha ingresado.")
else:
    print("No se puede formar un triángulo.")
