# Implementa una función recursiva hanoi(n, origen, destino, auxiliar)
#  que resuelva las Torres de Hanói.
class TorresHanoi:
    def __init__(self, n, origen, destino, auxiliar):
        # Atributos del objeto
        self.n = n
        self.origen = origen
        self.destino = destino
        self.auxiliar = auxiliar

    def hanoi(self, n, origen, destino, auxiliar):
        # Caso base: si solo hay 1 disco, se mueve directamente
        if n == 1:
            print(f"Mover disco 1 de {origen} a {destino}")
            return

        # Mover n-1 discos desde origen hasta auxiliar
        self.hanoi(n - 1, origen, auxiliar, destino)

        # Mover el disco mayor desde origen hasta destino
        print(f"Mover disco {n} de {origen} a {destino}")

        # Mover los n-1 discos desde auxiliar hasta destino
        self.hanoi(n - 1, auxiliar, destino, origen)

        # Ejecutar el método
    def resolver(self):
        self.hanoi(self.n, self.origen, self.destino, self.auxiliar)

# Crear el objeto
juego = TorresHanoi(3, "A", "C", "B")
print("Resolvemos el juego de Hanoi:")
juego.resolver()

