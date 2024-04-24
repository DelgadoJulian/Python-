valor = ["50", "60", "20",]
productos = ["Opc(1)Muñeco, Precio" , valor[0] ,"        ""Opcion(2)Baston,Precio ",valor[1],"           ""Opcion(3)Pelota,Precio ", valor[2]]
import os


boleanito = True
while boleanito:
    print(" ")
    print("========== WELCOME TO MY TOY STORE ============")
    print("(1) Ver productos")
    print("(2) Mostrar cheque")
    print("(0) Salir del programa")
    print("===============================================")
    print("Seleccione un accion a ejecutar")
    opc = input()
    os.system("cls")
    if opc == "1":
        print("Esta es la lista de productos con sus precios correspondientes")
        print("=========================================================================================================================")
        print(productos) 
        print("=========================================================================================================================")
        print("Que productos quiere comprar")
        prod=int(input())
        print("Cuantos desea comprar")
        com=int(input())

    if opc == "2":
        print("Este es el producto elejido")
        print(productos[prod])
        print("Esta es la cantidad del producto")
        print(valor[com])
        print("Por tus compras pagas")
        print(valor[com])*com

    if opc == "0":
        print("Gracias por comprar en nuestra tienda")
        boleanito = False