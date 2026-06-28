# Hacer una prueba de un cilindro en clase, tendrás como atributo el radio y la altura
# Calcular el area de la base, lateral, total y volumen
import math

class Cilindro:
    """Clase que modela un cilindro"""
    def __init__(self, radio, altura):  #self:instancia
        self.radio = radio          # atributo de radio
        self.altura = altura        # atributo de altura
    
    # Metodos
    def area_base(self):
        return math.pi * self.radio ** 2

    def area_lateral(self):
        return 2 * math.pi * self.radio * self.altura

    def area_total(self):
        return 2 * self.area_base() + self.area_lateral()

    def volumen(self):
        return self.area_base() * self.altura

# Crear un objeto cilindro
c = Cilindro(5, 10)

print("Radio:", c.radio)
print("Altura:", c.altura)
print(f"Área de la base: {c.area_base():.2f}")
print(f"Área lateral: {c.area_lateral():.2f}")
print(f"Área total: {c.area_total():.2f}")
print(f"Volumen: {c.volumen():.2f}")