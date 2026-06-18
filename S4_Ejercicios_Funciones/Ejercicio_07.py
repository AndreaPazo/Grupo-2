# Crea una función que convierta una nota del 0-20 
# al sistema peruano: AD, A, B, C o Desaprobado.

def convertir(nota):
    if nota >= 18:
        return "AD"
    elif nota >= 14:
        return "A"
    elif nota >= 11:
        return "B"
    elif nota >= 10:
        return "C"
    else:
        return "Desaprobado"

nota = float(input("Ingrese la nota (0-20): "))

resultado = convertir(nota)
print("Calificación:", resultado)