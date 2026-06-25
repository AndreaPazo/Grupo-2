
#Crea un módulo utils.py con funciones que usen *args y **kwargs para manejar cantidad variable de parámetros.

def sumar_todos(*args):
    """
    *args permite recibir cualquier cantidad de números.
    Se comportan como una tupla.
    """
    return sum(args)

def describir_objeto(**kwargs):
    """
    **kwargs permite recibir cualquier cantidad de argumentos con nombre.
    Se comportan como un diccionario.
    """
    descripcion = ""
    for clave, valor in kwargs.items():
        descripcion += f"{clave}: {valor}, "
    return descripcion.strip(", ")



# Ejemplo de *args: Sumar N números
resultado_suma = sumar_todos(10, 20, 30, 40, 50)
print(f"La suma total es: {resultado_suma}")

# Ejemplo de **kwargs: Definir un objeto con atributos variables
info = describir_objeto(nombre="Laptop", precio=1200, marca="HP", color="Negro")
print(f"Detalles: {info}")