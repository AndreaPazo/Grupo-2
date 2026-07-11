# Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
# Realiza lo siguiente:
# (1) Agregar "Pedro Ruiz", 
# (2) Buscar "Carlos Díaz" y mostrar posición,
# (3) Modificar "Luis Torres" por "Luis Mendoza",
# (4) Eliminar "Ana García"
# (5) Actualizar agenda

agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
print("=" * 30)
print(f"{'AGENDA DE ALUMNOS':^29}")
print("=" * 30)
for i, alumno in enumerate(agenda, start=1):
    print(f"{i:>5}: {alumno}")

print(f"\n{'=' * 30}")
print(f"{'AGENDA ACTUALIZADA':^29}")
print("=" * 30)
# (1) Agregar "Pedro Ruiz"
agenda.append("Pedro Ruiz")

# (2) Buscar "Carlos Díaz" y mostrar posición
posicion = agenda.index("Carlos Díaz")
print(f"Carlos Díaz se encuentra en la posición {posicion}:")

# (3) Modificar "Luis Torres" por "Luis Mendoza"
agenda[agenda.index("Luis Torres")] = "Luis Mendoza"

# (4) Eliminar "Ana García"
agenda.remove("Ana García")

# (5) Actualizar agenda
for i, alumno in enumerate(agenda, start=1):
    print(f"{i:>5}: {alumno}")    #["Luis Mendoza", "Carlos Díaz", "María López", "Pedro Ruiz"]
