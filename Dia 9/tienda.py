import os  #Importo "Os" para usar sus funciones
import time  #Importo "time" para usar sus funciones
carrito = []  #Creo la lista carrito vacia 

Nombre = [] #Creo la lista de Nombres
Precio = [] #creo la lista de precio
Cantidad = [] #creo la lista de cantidad


print(" ")
print("/=============================================/")
print("/         WELCOME TO MY FRUIT STORE           /") #Aqui en esta parte, desarrollo el menu de bienvenida al usuario
print("/  Ingrese porfavor los productos a la lista  /")
print("/=============================================/")
time.sleep(2.0) #Aqui usando la funcion "Time" importada, El sistema reconoce, que debe esperar (2.0) para seguir su ruta
os.system("cls") #Una vez acabado ese tiempo, se borra el historial 


print("Cuantos productos va a ingresar") #Aqui pido que ingrese la cantidad de productos que va a ingresar a  la tienda
cuantos = int(input())
time.sleep(1.0) #Aqui usando la funcion "Time" importada, El sistema reconoce, que debe esperar (2.0) para seguir su ruta
os.system("cls") #Una vez acabado ese tiempo, se borra el historial


items = 1 #Inicio un contador en uno para que le muestre al usuario en que items = Producto, de la tienda va agregando
for i in range(cuantos): # Con el paso anterior de ingrese la cantidad de productos, inicio un ciclo for para que dependiendo de la cantidad, repita ese mismo numero, las siguientes preguntas y cada resultado de eso se guarda en la listas
    
    print("Items de tienda numero: ",items,) #Aqui le digo al usuario en que producto va
    print("Nombre del producto")
    nom=str(input())
    Nombre.append(nom) #Aqui agrego la respuesta del usuario a la lista correspondiente 

    print("Precio del producto")
    pre = int(input())
    Precio.append(pre)  #Aqui agrego la respuesta del usuario a la lista correspondiente 

    print("Cuantos productos son")
    can = int(input())
    Cantidad.append(can)  #Aqui agrego la respuesta del usuario a la lista correspondiente 

    items += 1 #Al finalizar las preguntas, le sumo al contador uno, para que asi cuando se vuelva a repetir las preguntas, arriba le muestre que va en el item 2 y asi sucesivamente
    time.sleep(1.5) #Aqui usando la funcion "Time" importada, El sistema reconoce, que debe esperar (2.0) para seguir su ruta
    os.system("cls") #Una vez acabado ese tiempo, se borra el historial



for i in range(cuantos): #Aqui por medio de este ciclo for, y dependiendo de la cantidad de veces que se va a repetir en "cuanto"; saco todos los productos que fueron guardados en la lista al usuario 
    print(" ")
    print("Nombre del producto",{Nombre[i]},) #El {Nombre} es la lista que se llama y dentro de este [i] ese "i" es para que saque todo lo que hay dentro 
    print(" ")

    print("Precio del producto:",{Nombre[i]},) #El {Precio} es la lista que se llama y dentro de este [i] ese "i" es para que saque todo lo que hay dentro 
    print({Precio[i]})

    print("Cantidad del producto:",{Nombre[i]},) #El {Cantidad} es la lista que se llama y dentro de este [i] ese "i" es para que saque todo lo que hay dentro 
    print({Cantidad[i]})
    print("=============================================")

