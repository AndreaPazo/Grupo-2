# Crea funciones que usen métodos de dict para
# Gestionar un inventario: agregar, actualizar y listar.
class Inventario:
    def __init__(self):
        self.productos = {}     # Diccionario vacío para guardar los productos

    def agregar(self, nombre, cantidad, precio):
        if self.productos.get(nombre) is None:      # get(): busca si el producto ya existe
            self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
            print(f"Producto '{nombre}' agregado correctamente.")
        else:
            print(f"El producto '{nombre}' ya existe.")

    def actualizar(self, nombre, cantidad=None, precio=None):
        producto = self.productos.get(nombre)       # get(): busca el producto en el diccionario

        if producto is not None:
            if cantidad is not None:
                producto.update({"cantidad": cantidad})     # update(): cambia solo los datos que se envíen

            if precio is not None:
                producto.update({"precio": precio})

            print(f"Producto '{nombre}' actualizado correctamente.")
        else:
            print(f"El producto '{nombre}' no existe.")

    def listar(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nLISTA DE INVENTARIO")
            for nombre, datos in self.productos.items():    # items(): permite recorrer clave y valor del dict
                print(f"Producto: {nombre}")
                print(f"Cantidad: {datos['cantidad']}")
                print(f"Precio: S/{datos['precio']:.2f}")
                print("-" * 20)

# Programa principal
inventario = Inventario()

while True:     #Interacción con el usuario
    print("\n----- MENÚ -----")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Listar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))

        inventario.agregar(nombre, cantidad, precio)

    elif opcion == "2":

        nombre = input("Producto a actualizar: ")
        if inventario.productos.get(nombre):
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))

            inventario.actualizar(nombre, cantidad, precio)
        else:
            print(f"El producto '{nombre}' no existe.")

    elif opcion == "3":
        inventario.listar()

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente")

