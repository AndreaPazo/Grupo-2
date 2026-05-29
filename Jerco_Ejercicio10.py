# Conversor de divisas
print("Elegir el tipo de cambio de moneda")
print("1) Soles(PEN)-Dólares(USD)")
print("2) Dólares(USD)-Soles(PEN)")
print("3) Soles(PEN)-Euros(EUR)")
print("4) Euros(EUR)-Soles(PEN)")

# Pedir al usuario una opción
Seleccion = int(input("Ingrese una opción: "))
monto = float(input("Ingrese el monto a convertir: "))

# Tasas de cambio de moneda actual
dolar = 3.39
euro = 3.96

# Mostrar resultado
if Seleccion == 1:
    resultado = monto / dolar
    print(f"S/{monto:.2f} equivalen a ${resultado:.2f}")

elif Seleccion == 2:
    resultado = monto * dolar
    print(f"${monto:.2f} equivalen a S/{resultado:.2f}")

elif Seleccion == 3:
    resultado = monto / euro
    print(f"S/{monto:.2f} equivalen a {resultado:.2f} €")

elif Seleccion == 4:
    resultado = monto * euro
    print(f"{monto:.2f} € equivalen a S/{resultado:.2f}")

else:
    print("Opción no válida. Intente nuevamente.")



