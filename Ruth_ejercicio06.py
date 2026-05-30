
#Crear un programa que pida un número del 1 al 7 y
#muestre el nombre del día correspondiente usando
#estructura match-case

numero = int(input("Ingrese un número del 1 al 7: "))
match numero:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número es incorrecto, por favor ingrese un número del 1 al 7")