
#Ingresar 3 notas de un estudiante (escala 0-20). Calcular el
#promedio y mostrar si el alumno está Aprobado (≥11) o
#Desaprobado (<11)

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
print(f"La suma de las notas son: {nota1+nota2+nota3}")

if(nota1 <0 or nota1>20):
    print("La nota 1 no es incorrecta")
if(nota2 <0 or nota2>20):
    print("La nota 2 no es incorrecta")
if(nota3 <0 or nota3>20):
    print("La nota 3 no es incorrecta")
else:
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio es: {promedio:.2f}")
    if(promedio >= 11):
        print("El alumno está Aprobado")
    else:
        print("El alumno está Desaprobado")