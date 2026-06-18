
#4. Usa la constante global PI dentro de 
# una función para calcular la circunferencia 
# de un círculo.

#constante global
PI = 3.1416

#formula de funcion circunferencia = 2 * PI * radio
def calcular_circunferencia(radio):
    circunferencia = 2 * PI * radio
    return circunferencia

#solicitar al usuario el radio del círculo
radio = float(input("Ingrese el radio : "))

#calcular la circunferencia utilizando la función y mostrar el resultado
resultado = calcular_circunferencia(radio)
print(f"La circunferencia es:{resultado:.2f}")