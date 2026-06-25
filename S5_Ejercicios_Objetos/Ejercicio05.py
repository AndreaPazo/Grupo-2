#Implementa dos funciones: una que ordene la lista original (referencia) y otra que devuelva una copia ordenada
class Ordenador:
    def __init__(self, lista):
        # El objeto almacena la REFERENCIA a la lista original
        self.lista = lista

    def ordenar_original(self):
        """Ordena la lista original (modifica la referencia)."""
        # .sort() cambia el orden de la lista original permanentemente
        self.lista.sort()
        return self.lista

    def obtener_copia_ordenada(self):
        """Devuelve una copia ordenada sin alterar la original."""
        # sorted() crea una NUEVA lista en memoria, dejando la original intacta
        copia = sorted(self.lista)
        return copia

# --- PRUEBAS DEL CÓDIGO ---

numeros = [5, 2, 9, 1, 5, 6]  
gestor = Ordenador(numeros)

print(f"Lista original : {numeros}")

# 1. Copia ordenada: La lista 'numeros' NO cambia
copia = gestor.obtener_copia_ordenada()
print(f"Copia ordenada: {copia}")
print(f"La original sigue igual: {gestor.lista}")

# 2. Ordenar original: La lista 'numeros' SÍ cambia
gestor.ordenar_original()
print(f"La original ahora está ordenada: {gestor.lista}")