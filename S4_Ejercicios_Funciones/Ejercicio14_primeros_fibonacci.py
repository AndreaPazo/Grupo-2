# Genera los primeros N términos de Fibonacci (0,1,1,2,3,5...)
# y crea otra función que verifique si un número pertenece
def terminos_de_fibonacci(n):
    # Colocamos los dos primeros números de Fibonacci
    secuencia = [0, 1]

    # Si piden solo 1 número, devolvemos solo 0
    if n == 1:
        return [0]
    
    # Si piden 2 números, devolvemos [0, 1]
    if n == 2:
        return secuencia
    
    # Mientras la lista tenga menos de n números, seguimos agregando
    while len(secuencia) < n:
        # Sumamos los dos últimos números de la lista
        num_nuevo = secuencia[-1] + secuencia[-2]

        # Agregamos ese número nuevo al final de la lista
        secuencia.append(num_nuevo)

    # Por último devolvemos toda la secuencia
    return secuencia

def num_pertenece_fibonacci(dato):
    # Empezamos con los dos primeros números
    secuencia = [0, 1]

    # Generamos números de Fibonacci hasta llegar o pasar el número
    while secuencia [-1] < dato:
        num_nuevo = secuencia[-1] + secuencia[-2]
        secuencia.append(num_nuevo)

    # Revisamos si el número esta dentro de la secuencia
    return dato in secuencia

# Jugamos con lo que pida el usuario
cantidad = int(input("¿Cuántos términos de Fibonacci deseas ver?: "))
print("Secuencia de Fibonacci:", terminos_de_fibonacci(cantidad))

valor = int(input("¿Qué número deseas verificar si pertenece a Fibonacci?: "))
if num_pertenece_fibonacci(valor):
    print(f"El número {valor} sí pertenece a Fibonacci.")
else:
    print(f"El número {valor} no pertenece a Fibonacci.")
    
