
#20.Implementa un sistema completo de registro de notas. Usa un diccionario global compartido entre múltiples 
# funciones especializadas


# Diccionario global para almacenar las notas de los estudiantes
notas_estudiantes = {}

#REGISTRA UN NUEVO ESTUDIANTE:
def registrar_estudiante():
    nombre = input("Ingrese el nombre del  estudiante: ")
    if nombre not in notas_estudiantes:
        notas_estudiantes[nombre] = []
        print(f"Estudiante {nombre} registrado correctamente.")
    else:
        print("El estudiante ya existe.")

#AGREGA UNA NOTA A UN ESTUDIANTE EXISTENTE:
def agregar_nota():
    # 1. Pedir el nombre (asegúrate de escribir un texto, no un número)
    nombre = input("Ingrese el nombre del estudiante: ")
    
    # 2. Verificar si el nombre existe en el diccionario
    if nombre in notas_estudiantes:
        while True:
            try:
                # 3. Pedir la nota solo cuando el nombre ya fue validado
                nota = float(input(f"Ingrese la nota para {nombre} (0-20): "))
                
                # 4. Validar el rango
                if 0 <= nota <= 20:
                    notas_estudiantes[nombre].append(nota)
                    print("Nota agregada con éxito.")
                    break # Salimos del bucle
                else:
                    print("Error: La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
    else:
        print("Error: Estudiante no encontrado. Regístrelo primero.")

#MUESTRA LAS NOTAS DE UN ESTUDIANTE ESPECÍFICO:
def mostrar_notas():
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = notas_estudiantes.get(nombre)
    if notas is not None:
        print(f"Notas de {nombre}: {notas}")
    else:
        print("Estudiante no encontrado.")

def calcular_promedio(notas):
    if notas:
        return sum(notas) / len(notas)
    return 0

#MUESTRA LA LISTA DE TODOS LOS ESTUDIANTES:
def mostrar_estudiantes():
    if not notas_estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\nLista de estudiantes:")
        for nombre in notas_estudiantes:
            print(f"- {nombre}")



#MENU PRINCIAL PARA INTERACTUAR CON EL SISTEMA DE REGISTRO DE NOTAS:
while True:
    print("\n--- Sistema de Registro ---")
    print("1. Agregar estudiante")
    print("2. Agregar nota")
    print("3. Mostrar notas de estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Calcular promedio de un estudiante")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

#EVALUA LA OPCIÓN SELECCIONADA POR EL USUARIO Y LLAMA A LA FUNCIÓN CORRESPONDIENTE:
    if opcion == '1':
        registrar_estudiante()
    elif opcion == '2':
        agregar_nota()
    elif opcion == '3':
        mostrar_notas()
    elif opcion == '4':
        mostrar_estudiantes()
    elif opcion == '5':
        mostrar_estudiantes()
    elif opcion == '6':
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")