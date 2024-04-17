catalogo = { # Aqui se guarda los datos y valores de los productos en diccionario
    "Vikingo de Coco": 500,
    "Vikingo de Mora con leche": 500,
    "Vikingo de Yogurth": 500,
    "Vikingo de Mantecado": 500
}

# En esta seccion se almacena los productos agrgados al carrito
carrito = {}

# Se muestra al usuario el catalogo
def mostrarCatalogo():
    print("Catálogo de productos:")
    for producto, precio in catalogo.items():
        print(f"{producto}: ${precio}") #usamos "f" para concatenar 

# Se agrega datos al carrito
def agregarCarrito(producto, cantidad):
    if producto in catalogo:
        if cantidad > 0:
            if producto in carrito:
                carrito[producto] += cantidad 
            else:
                carrito[producto] = cantidad
            print(f"{cantidad} {producto}(s) agregado(s) al carrito.") 
        else:
            print("La cantidad debe ser mayor a 0.")
    else:
        print("Producto no encontrado.")

# Se muestra al usuario el carrito
def mostrarCarrito():
    if carrito:
        print("Contenido del carrito:")
        for producto, cantidad in carrito.items():
            print(f"{cantidad} {producto}(s)")
    else:
        print("El carrito está vacío.")

# Aqui se emplea una formula para calcular el total de la compra
def calcularTotal():
    total = 0
    for producto, cantidad in carrito.items():
        total += catalogo[producto] * cantidad
    print(f"Total de la compra: ${total}")

# Aqui en esta parte se finaliza la compra
def finalizarCompra():
    calcular_total()
    print("¡Gracias por tu compra!")
    carrito.clear()

# Este es nuestro menu principal
while True:
    print("\n--- Menú ---")
    print("1. Mostrar catálogo")
    print("2. Agregar producto al carrito")
    print("3. Mostrar contenido del carrito")
    print("4. Calcular total de la compra")
    print("5. Finalizar compra")
    print("6. Salir del simulador")

    opc = input("Selecciona una opción: ")
# Dependiendo de la opcion que desee elegir el usuario, se ejecuta 
    if opc == "1":
        mostrarCatalogo()
    elif opc == "2":
        producto = input("Ingresa el nombre del producto: ") #
        cantidad = int(input("Ingresa la cantidad: ")) # Se le pregunta al usuario la cantidad de vikingos que desea comprar.
        agregarCarrito(producto, cantidad) #Aqui se guarda el producto elegido y la cantidad.
    elif opc == "3":
        mostrar_carrito()
    elif opc == "4":
        calcular_total()
    elif opc == "5":
        finalizar_compra()
    elif opc == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")