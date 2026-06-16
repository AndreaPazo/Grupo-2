# Valida si una contraseña es segura usando funciones INTERNAS (locales)
# Debe tener 8+ chars, mayúscula, minúscula y dígito
def contrasena(n):
    # Verificamos la longitud de la contraseña
    if len(n) < 8:
        return False

    # Verificamos que tenga al menos una mayúscula, una minúscula y un dígito
    tiene_mayuscula = any(char.isupper() for char in n)
    tiene_minuscula = any(char.islower() for char in n)
    tiene_digito = any(char.isdigit() for char in n)

    return tiene_mayuscula and tiene_minuscula and tiene_digito

# Le pedimos al usuario ingresar una contraseña segura y válida
usuario = input("Ingrese una contraseña para validar: ")
while not contrasena(usuario):
    print("La contraseña no es segura. Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un dígito.")
    usuario = input("Ingrese otra contraseña: ")

print("La contraseña es segura.")

