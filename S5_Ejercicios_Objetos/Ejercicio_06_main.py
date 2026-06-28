#EJERCICIO 06: Crea un módulo estadisticas.py con funciones promedio, maximo y minimo.
# Úsalas desde main.py.

# Ejercicio_06_main.py
# Este es el archivo principal.
# Desde aquí vamos a usar las funciones creadas en el módulo estadisticas.

# Importamos el archivo Ejercicio_06_estadisticas.py
# Se escribe el nombre del archivo, pero sin la extensión .py
import Ejercicio_06_estadisticas

# Creamos una lista de notas para probar las funciones
notas = [15, 18, 12, 20, 16]

# Llamamos a la función promedio del módulo Ejercicio_06_estadisticas
resultado_promedio = Ejercicio_06_estadisticas.promedio(notas)

# Llamamos a la función maximo para obtener la nota más alta
resultado_maximo = Ejercicio_06_estadisticas.maximo(notas)

# Llamamos a la función minimo para obtener la nota más baja
resultado_minimo = Ejercicio_06_estadisticas.minimo(notas)

# Mostramos la lista original
print("Lista de notas:", notas)

# Mostramos el promedio calculado
print("Promedio:", resultado_promedio)

# Mostramos la nota máxima
print("Nota máxima:", resultado_maximo)

# Mostramos la nota mínima
print("Nota mínima:", resultado_minimo)