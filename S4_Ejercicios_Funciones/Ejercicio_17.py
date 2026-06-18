# Usa un CLOSURE para crear contadores independientes sin variables globales. 
# La función interna 'recuerda' el estado del scope externo.

def crear_contador():
    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    
    return incrementar

contador1 = crear_contador()
contador2 = crear_contador()

print(contador1())  
print(contador1()) 
print(contador1())  

print(contador2())  
print(contador2())
print(contador1()) 
print(contador2()) 