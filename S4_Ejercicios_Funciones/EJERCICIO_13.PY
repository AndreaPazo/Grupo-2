
#13.Python no tiene variables estáticas nativas. 
# Simúlalas usando un atributo de la propia función para generar IDs únicos.

# Función para generar IDs únicos utilizando un atributo de la función
def generar_id():
    if not hasattr(generar_id, "contador"):
        generar_id.contador = 49 # Inicializar el contador como un atributo de la función
    generar_id.contador += 1
    return generar_id.contador

# Generar algunos IDs únicos
print(generar_id())  # Salida: 50
print(generar_id())  # Salida: 51
print(generar_id())  # Salida: 52
print(generar_id())  # Salida: 53
print(generar_id())  # Salida: 54
print(generar_id())  # Salida: 55
print(generar_id())  # Salida: 56
print(generar_id())  # Salida: 57
print(generar_id())  # Salida: 58