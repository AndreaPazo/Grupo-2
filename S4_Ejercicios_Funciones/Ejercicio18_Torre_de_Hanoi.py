# Resuelve la Torre de Hanói con una función recursiva 
# Usa una variable de estado para contar movimientos. Verifica que son exactamente 2^n-1

def Torre_de_Hanoi(n, origen, auxiliar, destino, estado):

    # Si solo queda 1 disco, lo movemos directamente al destino
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        
        # Sumamos 1 porque acabamos de hacer un movimiento
        estado["movimientos"] += 1
    else:
        # Primero quitamos los discos pequeños que están encima
        # y los llevamos al poste auxiliar
        Torre_de_Hanoi(n - 1, origen, destino, auxiliar, estado)

        # Ahora podemos mover el disco más grande al destino
        print(f"Mover disco {n} de {origen} a {destino}")

        # Contamos este movimiento
        estado["movimientos"] += 1

        # Por último, movemos los discos pequeños que habíamos dejado
        # en el auxiliar hacia el destino
        Torre_de_Hanoi(n - 1, auxiliar, origen, destino, estado)


def resolver_hanoi(n):
    # Aqui guardamos la cantidad de movimientos realizados
    estado = {"movimientos": 0}

    # Llamamos a la función recursiva usando los postes A, B y C
    # Comenzamos el ejercicio usando:
    # A = Origen
    # B = Auxiliar
    # C = Destino
    Torre_de_Hanoi(n, "A", "B", "C", estado)

    # Calculamos cuántos movimientos debería tener la solución correcta
    esperados = 2 ** n - 1

    # Mostramos cuántos movimientos se hicieron realmente
    print("\nMovimientos realizados:", estado["movimientos"])

    # Mostramos cuántos movimientos se esperaban
    print("Movimientos esperados:", esperados)

    # Verificamos si el resultado es correcto
    if estado["movimientos"] == esperados:
        print("Verificación correcta")
    else:
        print("Verificación incorrecta")



print("Hola torre de hanoi, usaremos 3 discos:")
resolver_hanoi(3)
