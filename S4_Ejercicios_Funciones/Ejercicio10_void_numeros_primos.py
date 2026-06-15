# Crea una función void que muestre todos los números primos desde 2 hasta N usando bucles anidados.
def mostrar_primos_hasta(n):

    # Recorremos todos los números desde 2 hasta n
    for num in range(2, n + 1):
        # Suponemos que el número sí es primo
        es_primo = True

        # Probamos si ese número se puede dividir entre otros
        for divisor in range(2, num):
            # Si el residuo es 0, entonces no es primo
            if num % divisor == 0:
                es_primo = False
                break

        # Si sigue siendo primo, lo mostramos en pantalla
        if es_primo:
            print(num)

# Pedir al usuario hasta donde quiere ver números primos
Usuario = int(input("Ingrese una cantidad para verificar números primos: "))
print(f"Los números primos hasta {Usuario} son:")
mostrar_primos_hasta(Usuario)

