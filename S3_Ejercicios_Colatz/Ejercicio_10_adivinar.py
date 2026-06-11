# ejercicio10_adivinar.py

# Importamos random para poder generar un número aleatorio
import random

# Generamos un número secreto entre 1 y 20
numero_secreto = random.randint(1, 20)

# Definimos la cantidad máxima de intentos
intentos = 5

# Definimos el puntaje inicial
puntaje = 100

# Mostramos las instrucciones iniciales del juego
print("JUEGO DE ADIVINAR EL NÚMERO")
print("Debes adivinar un número entre 1 y 20")
print("Tienes", intentos, "intentos")
print("Tu puntaje inicial es:", puntaje)

# Usamos for para mostrar la lista de intentos disponibles
print("Intentos disponibles:")

for i in range(1, intentos + 1):
    print("Intento", i)

# El while controla el juego mientras todavía queden intentos
while intentos > 0:

    # Pedimos al usuario que ingrese un número
    numero = int(input("Ingrese un número: "))

    # Si el número ingresado es igual al número secreto, gana
    if numero == numero_secreto:
        print("¡Correcto! Adivinaste el número secreto")
        break

    # Si el número ingresado es menor que el número secreto,
    # damos una pista indicando que debe intentar con un número mayor
    elif numero < numero_secreto:
        print("El número secreto es mayor")

        # Condicional anidado para dar una pista de cercanía
        if numero_secreto - numero <= 3:
            print("Estás cerca")
        else:
            print("Estás lejos")

    # Si no es igual ni menor, entonces el número ingresado es mayor
    else:
        print("El número secreto es menor")

        # Condicional anidado para dar una pista de cercanía
        if numero - numero_secreto <= 3:
            print("Estás cerca")
        else:
            print("Estás lejos")

    # Restamos un intento porque el usuario no adivinó
    intentos -= 1

    # Restamos puntaje por cada intento fallido
    puntaje -= 20

    # Mostramos cuántos intentos quedan
    print("Te quedan", intentos, "intentos")

# El else del while se ejecuta solo si el bucle terminó sin usar break
else:
    print("Se acabaron los intentos")
    print("El número secreto era:", numero_secreto)

# Mostramos el puntaje final
print("Puntaje final:", puntaje)