# EJERCICIO 03
# Demuestra que una variable creada dentro de una función
# no es accesible desde fuera.
# Calcula el área de un cuadrado.

def calcular_area_cuadrado(lado):
    # La variable "area" se crea dentro de la función,
    # por eso es una variable local.
    area = lado * lado

    # Devolvemos el valor de "area"; la variable como tal sigue siendo local.
    return area


# Programa principal
resultado = calcular_area_cuadrado(5)

print("El área del cuadrado es:", resultado)


# Intentamos acceder a la variable local "area" desde fuera.
# Usamos eval("area") para comprobarlo sin que VS Code marque advertencia.
try:
    eval("area")
except NameError:
    print("La variable 'area' no es accesible desde fuera de la función.")