
#Crea un módulo conversor.py con funciones celsius_a_fahrenheit y fahrenheit_a_celsius y úsalas

 
class Conversor:
 def __init__(self, conversor):
        """El objeto guarda el valor numérico de la temperatura."""
        self.conversor = conversor

def a_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

def a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9


conversor= Conversor()


# CASO 1: Ingresas Celsius
temp_c = 50
resultado_f = Conversor.a_fahrenheit(temp_c)
print(f"{temp_c}°C equivalen a {resultado_f}°F")

# CASO 2: Ingresas Fahrenheit
temp_f = 50
resultado_c = Conversor.a_celsius(temp_f)
print(f"{temp_f}°F equivalen a {resultado_c:.2f}°C")


