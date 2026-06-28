# Ejemplo: paso por valor (tipo inmutable)
print("EJERCICIO01: ")
def duplicar(numero):
    num = numero * 2 # Solo modifica
    print('Dentro:', num)
x = 10
duplicar(x)
print('Fuera:', x) # Sigue siendo 10 ←
# NO cambió
# Salida:
# Dentro: 20
# Fuera: 10

print("\nEJERCICIO02: ")

# Ejemplo 1: lista (mutable) — SÍ cambia
def agregar_elemento(lista, valor):
    lista.append(valor) # modifica el objeto original

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista, 99)
print(mi_lista) # [1, 2, 3, 99] ← cambió

# Ejemplo 2: reasignación — NO cambia (nuevo objeto)
def reasignar(lista):
    lista = [10, 20] # crea un nuevo objeto local
agregar_elemento(mi_lista, 5)
reasignar(mi_lista)
print(mi_lista) # [1, 2, 3, 99, 5] ← no cambió

print("-------------")
# list — listas
nums = [3, 1, 4, 1, 5]
nums.append(9) #[3,1,4,1,5,9]
nums.sort() #[1,1,3,4,5,9]
nums.reverse() #[9,5,4,3,1,1]
nums.remove(1) # quita primer 1
print(nums.count(1)) # 1
print(f"Números cambiados de la lista: {nums}")

print("\nEJERCICIO03: ")
class Rectangulo:
# """Clase que modela un rectángulo."""
    def __init__(self, base, altura):
        self.base = base    # atributo de instancia
        self.altura = altura    # atributo de instancia
    
    def area(self):     # método — retorna el área
        return self.base * self.altura
    def perimetro(self):    # método — retorna el perímetro
        return 2 * (self.base + self.altura)
    def describir(self):    # método — imprime descripción
        print(f'Rectángulo: {self.base}x{self.altura}')
        print(f'Área : {self.area()}')
        print(f'Perímetro: {self.perimetro()}')

r = Rectangulo(5, 3)
r.describir()   # Rectángulo 5x3 / Área: 15 / Perímetro: 16

print("\nEJERCICIO04: ")

"""Módulo propio: operaciones
matemáticas."""
def sumar(a, b):
    return a + b

def potencia(base, exp):
    return base ** exp

def es_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
        return True
