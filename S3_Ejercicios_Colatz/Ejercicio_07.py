# Ejercicio 7: Validar 
# Pide contraseña con while; 
# máximo 3 intentos, bloquea si falla.

# Contraseña
clave_correcta = "1234"
# Contador de intentos
intentos = 0
# condición: máximo 3 intentos
while intentos < 3:
    clave = input("Ingrese la contraseña de 4 digitos: ")
    # éxito: imprime y rompe bucle
    if clave == clave_correcta:
        print("Acceso concedido")
        break
    # incrementa contador de fallos
    intentos += 1
    # condicional anidado: avisa
    if intentos < 3:
        print("Contraseña incorrecta. Intente nuevamente.")
# verifica bloqueo post-bucle
if intentos == 3:
    print("Cuenta bloqueada.")