"""Se pide ingresar grados celsius y transformarlos a Farenheit y Kelvin
Para Farenheit se multiplica por 9/5 + 32 y para Celsius se suma +273.15"""
celcius = float(input("Ingrese la temperatura en Celcius: "))
faren=celcius*9/5+32
kelvin=celcius+273.15
print(f"La temperatura en grados Farenheit es {faren} y en Kelvin es {kelvin}")