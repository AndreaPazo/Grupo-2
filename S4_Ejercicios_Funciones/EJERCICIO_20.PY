# Implementa un sistema completo de registro de notas

# Diccionario global
notas_estudiantes = {}

# 1. Registrar estudiante
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre not in notas_estudiantes:
        notas_estudiantes[nombre] = []
        print(f"Estudiante '{nombre}' registrado correctamente.")
    else:
        print("El estudiante ya existe.")

# 2. Agregar nota
def agregar_nota():
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre not in notas_estudiantes:
        print("El estudiante no existe.")
        return

    while True:
        try:
            nota = float(input("Ingrese la nota (0-20): "))

            if 0 <= nota <= 20:
                notas_estudiantes[nombre].append(nota)
                print("Nota agregada correctamente.")
                break
            else:
                print("La nota debe estar entre 0 y 20.")

        except ValueError:
            print("Ingrese un número válido.")

# 3. Mostrar notas
def mostrar_notas():
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in notas_estudiantes:
        if notas_estudiantes[nombre]:
            print(f"Notas de {nombre}: {notas_estudiantes[nombre]}")
        else:
            print(f"{nombre} aún no tiene notas.")
    else:
        print("Estudiante no encontrado.")

# Función para calcular promedio
def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# 4. Mostrar promedio
def mostrar_promedio():
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in notas_estudiantes:

        if len(notas_estudiantes[nombre]) == 0:
            print("El estudiante no tiene notas.")
        else:
            promedio = calcular_promedio(notas_estudiantes[nombre])
            print(f"Promedio de {nombre}: {promedio:.2f}")

    else:
        print("Estudiante no encontrado.")

# 5. Mostrar estudiantes
def mostrar_estudiantes():

    if len(notas_estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("\nLista de estudiantes:")

        for estudiante in notas_estudiantes:
            print("-", estudiante)


# ==========================
#      MENÚ PRINCIPAL
# ==========================

while True:

    print("\n--- Sistema de Registro ---")
    print("1. Agregar estudiante")
    print("2. Agregar nota")
    print("3. Mostrar notas de estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Calcular promedio de un estudiante")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante()

    elif opcion == "2":
        agregar_nota()

    elif opcion == "3":
        mostrar_notas()

    elif opcion == "4":
        mostrar_estudiantes()

    elif opcion == "5":
        mostrar_promedio()

    elif opcion == "6":
        print(f"\nEstudiantes registrados: {'Nota':>8}")

        if len(notas_estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            for estudiante in notas_estudiantes:
                print(f"- {estudiante:<26} {notas_estudiantes[estudiante][0]:.0f}")

        print("\nSaliendo...")
        break

    else:
        print("Opción no válida.")