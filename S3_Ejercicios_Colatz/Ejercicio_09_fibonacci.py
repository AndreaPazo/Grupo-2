# ejercicio9_fibonacci.py

# Pedimos al usuario que ingrese el número límite
# El programa mostrará los números Fibonacci menores que ese valor
n = int(input("Ingrese N: "))

# Inicializamos los dos primeros valores de la sucesión Fibonacci
a = 0
b = 1

# Creamos contadores para guardar estadísticas del proceso
contador = 0
pares = 0
impares = 0

# Validamos que el número ingresado sea mayor que cero
if n <= 0:
    print("Debe ingresar un número mayor que 0")

else:
    # Mientras el número actual de Fibonacci sea menor que N,
    # el programa seguirá generando la secuencia
    while a < n:

        # Mostramos el número Fibonacci actual
        print(a)

        # Verificamos si el número actual es par o impar
        if a % 2 == 0:
            # Si el residuo de dividir entre 2 es cero, es par
            pares = pares + 1
        else:
            # Si no es par, entonces es impar
            impares = impares + 1

        # Calculamos el siguiente número Fibonacci
        # Cada nuevo número se obtiene sumando los dos anteriores
        siguiente = a + b

        # Actualizamos los valores para avanzar en la secuencia
        # El segundo valor pasa a ser el primero
        a = b

        # El número calculado pasa a ser el segundo valor
        b = siguiente

        # Aumentamos el contador porque se generó un número Fibonacci
        contador += 1

    # Cuando termina el ciclo, mostramos las estadísticas finales
    print("Cantidad de números Fibonacci:", contador)
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)