# Pedir un número real al usuario 
num = float(input("Ingresar un número real: "))

# Revisamos si el número es positivo, negativo o cero
if num > 0:
    clasificacion = "positivo"
elif num < 0:
    clasificacion = "negativo"
else:
    clasificacion = "cero."

# Indicamos si es entero o decimal

if num.is_integer():
    tipo = "entero."
else:
    tipo = "decimal."

#Mostrar resultado
print (f"El número {num} es {clasificacion} y {tipo}")



