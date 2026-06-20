
#8.Crea un contador global que una función incremente 
# cada vez que sea llamada. Usa la palabra clave 'global'.

#contador global
contador = 0
#función para incrementar el contador
def incrementar_contador():
    global contador  # Indicar que se va a usar la variable global
    contador += 1    # Incrementar el contador
    return contador

# Llamar a la función varias veces y mostrar el contador
print(incrementar_contador())  # Salida: 1
print(incrementar_contador())  # Salida: 2
print(incrementar_contador())  # Salida: 3
print(incrementar_contador())  # Salida: 4
print(incrementar_contador())  # Salida: 5

