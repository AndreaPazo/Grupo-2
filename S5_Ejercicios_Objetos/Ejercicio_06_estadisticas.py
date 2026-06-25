# Ejercicio_06_estadisticas.py
# Este archivo será nuestro módulo.
# Un módulo es un archivo .py que contiene funciones reutilizables.

def promedio(lista):
    """
    Calcula el promedio de una lista de números.
    """
    # sum(lista) suma todos los valores de la lista
    # len(lista) cuenta cuántos elementos tiene la lista
    # Luego se divide la suma entre la cantidad de elementos
    return sum(lista) / len(lista)


def maximo(lista):
    """
    Retorna el valor máximo de una lista.
    """
    # max(lista) busca el número más grande dentro de la lista
    return max(lista)


def minimo(lista):
    """
    Retorna el valor mínimo de una lista.
    """
    # min(lista) busca el número más pequeño dentro de la lista
    return min(lista)