import math

class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4/3) * math.pi * self.radio ** 3
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
Usuario = float(input("Ingrese la medida del radio: "))
e = Esfera(Usuario)

print("Lectura de cada objeto de la esfera: ")
print(f"Perímetro: {e.perimetro():.2f}")
print(f"Área: {e.area():.2f}")
print(f"Volumen: {e.volumen():.2f}")


    




