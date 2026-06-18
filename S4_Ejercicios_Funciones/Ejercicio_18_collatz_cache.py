# EJERCICIO 18
# Analiza la secuencia de Collatz del 1 al N.
# Usa memorización (caché) para evitar recalcular.
# Encuentra el número con más pasos.

def pasos_collatz(numero, cache):
    # Primero revisamos si el número ya fue calculado antes.
    # Si ya está guardado en el caché, no lo volvemos a calcular.
    if numero in cache:
        return cache[numero]

    # Guardamos el número inicial.
    # Esto es importante porque "numero" va a cambiar durante el cálculo.
    original = numero

    # Aplicamos la regla de Collatz:
    # Si el número es par, se divide entre 2.
    if numero % 2 == 0:
        siguiente = numero // 2

    # Si el número es impar, se multiplica por 3 y se suma 1.
    else:
        siguiente = 3 * numero + 1

    # Calculamos los pasos.
    # Se suma 1 porque acabamos de avanzar de "numero" a "siguiente".
    # Luego usamos la función nuevamente para saber cuántos pasos faltan.
    pasos = 1 + pasos_collatz(siguiente, cache)

    # Guardamos el resultado en el caché.
    # Así, si más adelante aparece el mismo número,
    # Python usará este valor guardado y no recalculará todo.
    cache[original] = pasos

    # Retornamos la cantidad total de pasos.
    return pasos


def analizar_collatz(n):
    # Creamos el caché con el caso base.
    # El número 1 necesita 0 pasos porque ya llegó al final.
    cache = {1: 0}

    # Empezamos desde el número 1.
    numero = 1

    # Estas variables guardarán el número que tenga más pasos.
    numero_mayor_pasos = 1
    mayor_pasos = 0

    print("Análisis de Collatz del 1 al", n)
    print("--------------------------------")

    # Recorremos todos los números desde 1 hasta n.
    while numero <= n:
        # Calculamos los pasos del número actual.
        pasos = pasos_collatz(numero, cache)

        # Mostramos el resultado de cada número.
        print("Número:", numero, "- Pasos:", pasos)

        # Si el número actual tiene más pasos que el mayor registrado,
        # actualizamos los valores.
        if pasos > mayor_pasos:
            mayor_pasos = pasos
            numero_mayor_pasos = numero

        # Pasamos al siguiente número.
        numero += 1

    print("--------------------------------")
    print("El número con más pasos es:", numero_mayor_pasos)
    print("Cantidad de pasos:", mayor_pasos)


# Programa principal
# Pedimos al usuario hasta qué número desea analizar.
n = int(input("Ingrese un número límite: "))

# Llamamos a la función principal.
analizar_collatz(n)