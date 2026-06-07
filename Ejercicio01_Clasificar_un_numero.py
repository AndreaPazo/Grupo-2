# Pide un número al usuario e indica si es positivo, negativo o cero
num = float(input("Ingresar un número: "))

# Revisamos si el número es positivo, negativo o cero
if num > 0:
    clasificacion = "positivo"
elif num < 0:
    clasificacion = "negativo"
else:
    clasificacion = "cero."

#Mostrar resultado
print (f"El número {num} es {clasificacion}")

