# Escribe una función cuadrado(n) que reciba un entero 
# y retorne su cuadrado. Muestra el resultado.

class Potencia:
    def __init__(self, n):
        self.n = n

    def cuadrado(self):
        return self.n * self.n

num = int(input("Ingrese un número: "))
c = Potencia(num)

print("El cuadrado es:", c.cuadrado())