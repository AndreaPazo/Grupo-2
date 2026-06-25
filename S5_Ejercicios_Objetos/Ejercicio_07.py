# Crea una función potencia(base, exp=2) que calcule base^exp. 
# Si no se indica exp, usa 2 por defecto

class Potencia:
    def __init__(self, base, exp=2):
        self.base = base
        self.exp = exp

    def calcular(self):
        return self.base ** self.exp

base = int(input("Ingrese la base: "))
exp = input("Presiona enter si tu exponente es 2; caso contrario ingrese el exponente: ")

if exp == "":
    p = Potencia(base)
else:
    p = Potencia(base, int(exp))

print("Resultado:", p.calcular())