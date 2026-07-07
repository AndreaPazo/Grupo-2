# Ingresar la cantidad de alumnos, y por cada alumno guardar: en un arreglo los nombres, segundo arreglo apellidos paternos,
# tercer arreglo apellidos maternos en cuarto arreglo notas y 
# quinto arreglo si es >= a 11.5 (aprobado), si es < 11.5 (desaprobado)

def lista_alumnos(Alumnos):
    nombres = []
    apellidos_paternos = []
    apellidos_maternos = []
    notas = []
    estado = []

    for i in range(Alumnos):
        print(f"\nAlumno {i + 1}:")
        nombre = input("Ingrese el nombre: ")
        apellido_paterno = input("Ingrese el apellido paterno: ")
        apellido_materno = input("Ingrese el apellido materno: ")
        nota = float(input("Ingrese la nota entre 0 a 20: "))
        
        while True:
            if 0 <= nota <= 20:
                break
            else:
                print("Ingrese nuevamente la nota: ")
                nota = float(input("Ingrese la nota entre 0 a 20: "))

        nombres.append(nombre)
        apellidos_paternos.append(apellido_paterno)
        apellidos_maternos.append(apellido_materno)
        notas.append(nota)

        if nota >= 11.5:
            estado.append("Aprobado")
        else:
            estado.append("Desaprobado")

    return nombres, apellidos_paternos, apellidos_maternos, notas, estado

try:
    alumnos = int(input("Ingrese la cantidad de alumnos escribiendo el nombre del número: "))
    if alumnos <= 0:
        print("La cantidad de alumnos debe ser mayor a cero.")
    else:
        nombres, apellidos_paternos, apellidos_maternos, notas, estado = lista_alumnos(alumnos)

        print("\nLista de Alumnos:")
        #alineacion de las filas y columnas
        print("{:<20} {:<20} {:<20} {:<10} {:<15}".format("Nombre", "Apellido Paterno", "Apellido Materno", "Nota", "Estado"))
        for i in range(alumnos):
            print("{:<20} {:<20} {:<20} {:<10.1f} {:<15}".format(
                nombres[i],
                apellidos_paternos[i],
                apellidos_maternos[i],
                notas[i],
                estado[i]
            ))
except ValueError:
    print("Ingrese un número válido para la cantidad de alumnos.")
