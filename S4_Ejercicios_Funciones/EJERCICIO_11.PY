
#11.La conjetura de Collatz: si n es par → n/2; si es impar → 3n+1. 
# Repite hasta llegar a 1. Muestra la secuencia y cuenta los pasos.

def collatz(n):
    pasos = 0
    secuencia = [n]
    
    while n != 1:
        if n % 2 == 0:  # n es par
            n = n // 2
        else:           # n es impar
            n = 3 * n + 1
        
        secuencia.append(n)
        pasos += 1
    
    return secuencia, pasos 
# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número : "))

# Obtener la secuencia de Collatz y el número de pasos
secuencia, pasos = collatz(numero)

# Mostrar la secuencia y el número de pasos
print("Secuencia de Collatz:", secuencia)
print("Número de pasos para llegar a 1:", pasos)