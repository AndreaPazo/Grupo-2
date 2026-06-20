# Crea una función saludar(nombre) que reciba un nombre 
# Como cadena e imprima un saludo personalizado
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print (f"!Hola {self.nombre}, Bienvenido!")

    def despedirse(self):
        print (f"Adiós {self.nombre}, vuelve pronto.")

usuario = input("Ingrese un nombre: ")
p = Persona(usuario)
p.saludar()
p.despedirse()







