# EJERCICIO 03: Crea una función agregar(lista, elemento)
# que añada el elemento al final de la lista. ¿Cambia fuera?

# Creamos una función llamada agregar
# Recibe dos parámetros:
# lista: la lista donde queremos añadir un dato
# elemento: el dato que queremos agregar al final de la lista

def agregar(lista, elemento):
    # append() es un método de listas
    # Sirve para añadir un elemento al final de la lista
    lista.append(elemento)

    # No es necesario usar return porque la lista se modifica directamente
    # Esto ocurre porque las listas son mutables


# Creamos una lista inicial
mi_lista = [10, 20, 30]

# Mostramos la lista antes de llamar a la función
print("Antes de agregar:", mi_lista)

# Llamamos a la función y le pasamos la lista y el nuevo elemento
agregar(mi_lista, 40)

# Mostramos la lista después de llamar a la función
print("Después de agregar:", mi_lista)

# Respondemos la pregunta ¿cambia fuera?
print("¿Cambia fuera?: Sí, cambia fuera de la función porque la lista es mutable.")
print("La función modifica la lista original al usar append().")