# ==========================================
# PROGRAMA: CARRITO DE COMPRAS
# Lenguaje: Python POO(Programación Orientada a Objetos)
# ==========================================

class Cliente:
    def __init__(self, nombres, apellidos, dni, telefono):
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.telefono = telefono

    def mostrar_datos(self):
        print("\n========== DATOS DEL CLIENTE ==========")
        print(f"Nombres   : {self.nombres}")
        print(f"Apellidos : {self.apellidos}")
        print(f"DNI       : {self.dni}")
        print(f"Teléfono  : {self.telefono}")


class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio


class DetalleCompra:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad


class Compra:
    def __init__(self, cliente):
        self.cliente = cliente
        self.detalles = []

    def agregar_producto(self, producto, cantidad):
        detalle = DetalleCompra(producto, cantidad)
        self.detalles.append(detalle)

    def calcular_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.subtotal()
        return total

    def mostrar_resumen(self):
        self.cliente.mostrar_datos()

        print("\n============= RESUMEN DE LA COMPRA =============")
        print("{:<19} {:>10} {:>10} {:>13}".format(
            "Producto", "Precio", "Cantidad", "Subtotal"))
        print("-" * 55)

        for detalle in self.detalles:
            print("{:<21} S/{:>6.2f} {:>10}     S/{:>7.2f}".format(
                detalle.producto.nombre,
                detalle.producto.precio,
                detalle.cantidad,
                detalle.subtotal()
            ))

        print("-" * 55)
        print(f"TOTAL DE LA COMPRA: S/ {self.calcular_total():.2f}")     


# ==========================
#    PROGRAMA PRINCIPAL
# ==========================

print("===================================")
print("        CARRITO DE COMPRAS")
print("===================================")

# Datos del cliente
nombres = input("Ingrese nombres: ")
apellidos = input("Ingrese apellidos: ")
dni = input("Ingrese DNI: ")
telefono = input("Ingrese teléfono: ")

cliente = Cliente(nombres, apellidos, dni, telefono)

# Lista de productos
productos = [
    Producto(1, "Arroz (1kg)", 4.80),
    Producto(2, "Azúcar (1kg)", 4.50),
    Producto(3, "Gaseosa (3L)", 12.00),
    Producto(4, "Aceite vegetal(1L)", 10.50),
    Producto(5, "Leche evaporada", 4.50),
    Producto(6, "Huevos (docena)", 7.80),
    Producto(7, "Fideos (500g)", 3.20),
    Producto(8, "Pollo (1kg)", 11.50),
    Producto(9, "Papa blanca (1kg)", 3.50),
    Producto(10, "Agua mineral", 2.00)
    
]

compra = Compra(cliente)

# Proceso de compra
while True:

    print("\n========== CATÁLOGO ==========")
    print("{:<5} {:<20} {:>10}".format("ID", "Producto", "Precio"))

    for producto in productos:
        print("{:<5} {:<20} S/{:>8.2f}".format(
            producto.id_producto,
            producto.nombre,
            producto.precio
        ))

    opcion = input("\nIngrese el ID del producto (o escriba 'salir'): ")

    if opcion.lower() == "salir":
        break

    if not opcion.isdigit():
        print("ID inválido.")
        continue

    id_producto = int(opcion)

    producto_encontrado = None

    for producto in productos:
        if producto.id_producto == id_producto:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("El producto no existe.")
        continue

    try:
        cantidad = int(input(f"Ingrese la cantidad de {producto.nombre}: "))  #CAMBIÉ

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            continue

        compra.agregar_producto(producto_encontrado, cantidad)
        print("Producto agregado correctamente.")

    except ValueError:
        print("Debe ingresar una cantidad válida.")

# Mostrar resumen
print("\n\nCOMPRA FINALIZADA")
compra.mostrar_resumen()

# Selección del método de pago
print("\n========== MÉTODO DE PAGO ==========")
print("1. Efectivo")
print("2. Yape")
print("3. Plin")
print("4. Tarjeta")

while True:
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        metodo_pago = "Efectivo"
        break
    elif opcion == "2":
        metodo_pago = "Yape"
        break
    elif opcion == "3":
        metodo_pago = "Plin"
        break
    elif opcion == "4":
        metodo_pago = "Tarjeta"
        break
    else:
        print("Opción inválida. Intente nuevamente.")

print(f"\nMétodo de pago seleccionado: {metodo_pago}")
print("¡Gracias por su compra! 😊")

