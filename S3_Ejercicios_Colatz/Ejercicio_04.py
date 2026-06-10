# Exercicio 4: Menú de opciones
# Crea un menú que se repita hasta 
# que el usuario elija 'Salir' (do-while).

while True:
# menú
    print("MENÚ")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

# if anidado dentro del while
    if opcion == "1":
        print("Seleccionó la Opción 1")
    elif opcion == "2":
        print("Seleccionó la Opción 2")
    elif opcion == "3":
        print("Saliendo...")
        break  # rompe el bucle
    else:
        print("Opción no válida")