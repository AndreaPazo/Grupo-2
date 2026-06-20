# una clase para hacer la prueba de la clase, y tendrá como atributo el radio
# calcular el perímetro, área y volumen
import math
# global

class Formas:
    """Clase que modela un ."""
    def __init__(self, radio): #self=instancia
        self.radio = radio # atributo de radio
    # Metodos
    def area(self): # método — retorna el área
        return (self.radio * math.pi)

    def perimetro(self): # método — retorna el perímetro
        return (2) * math.pi * self.radio

    def volumen(self): # método — retorna el perímetro
        return ((4/3)* math.pi*self.radio**3)

    def describir(self): # método — imprime descripción
        print(f'Radio: {self.radio}')
        print(f'Área: {self.area():.2f}')
        print(f'Perímetro: {self.perimetro():.2f}')
        print(f'volumen: {self.volumen():.2f}')

c= Formas(5)
c.describir ()

print(f"el área es: {c.area():.2f}")


