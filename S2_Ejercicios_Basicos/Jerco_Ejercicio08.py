# Pedir al usuario su talla y peso 
talla = float(input("Ingresar su talla en metros: "))
peso = float(input("Ingresar su peso en kilogramos: "))

# Calculamos el indice de masa corporal (IMC)
imc = peso / (talla ** 2)

# Mostramos el diagnostico segun los rangos de la OMS
if imc < 18.5:
    diagnostico = "peso bajo"
elif imc < 24.9:
    diagnostico = "peso normal"
elif imc < 29.9:
    diagnostico = "sobrepeso"
elif imc < 34.9:
    diagnostico = "Obesidad I"
elif imc < 39.9:
    diagnostico = "Obesidad II"
else:
    diagnostico = "Obesidad III"

# Mostrar resultado
print (f"Su IMC es: {imc:.2f}")
print (f"Su diagnostico es: {diagnostico}")



