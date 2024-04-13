#Le doy al usuario la bienvenida al programa. 
#Formo una interfaz 
print("/---------------------------------------------------/")
print("/                Hola, Bienvenido                   /")
print("/ Por favor ingrese su billete para darle su cambio /")
print("/---------------------------------------------------/")
Dinero=int(input()) #De aqui recolecto su numero

while Dinero < 0: #Si el numero es menor a 0 (Negativo) este bulce se repetira hasta que me de un numero positivo
    print("Uy, ¿hay plata en negativo?, IT'S UNBELIEVABLE!!!")
    print("Agregue otro numero, por favor")
    Dinero = 0 #regreso el numero a 0 para que no ponga problemas de cache
    Dinero=int(input())
    
    


if Dinero > 0: # Si el numero ingresado por el usuario es mayor a 0 (positivo), se ejecutara el programa

    if Dinero >= 10: # Si el dinero es mayor o igual a 10 se correra esto
        queda1 = Dinero // 10 #Primero se saca una division entera para que no me cuente el residuo
        print("se necesita ", str(queda1) , " monedas de 10") #Imprimo al usuario por medio de la variable "Queda" el numero de monedas que necesito
        Dinero = Dinero % 10

    if Dinero >= 5: # Si el dinero es mayor o igual a 5 se correra esto
        queda2 = Dinero // 5 #Primero se saca una division entera para que no me cuente el residuo
        print("Se necesitan ", str(queda2) , " monedas de 5") #Imprimo al usuario por medio de la variable "Queda" el numero de monedas que necesito
        Dinero = Dinero % 5

    if Dinero >= 1: # Si el dinero es mayor o igual a 1 se correra esto
        queda3 = Dinero // 1 #Primero se saca una division entera para que no me cuente el residuo
        print("Se necesitan ", str(queda3) , " monedas de 1") #Imprimo al usuario por medio de la variable "Queda" el numero de monedas que necesito
        Dinero = Dinero % 1

resultado = queda1 + queda2 + queda3 #Aqui sumos los queda (Monedas) y guardo el dato en resultado.
print(" ")
print("--------------------------------------------------------")
print("Se necesitan ", int(resultado) , " monedas" ) #Luego le muestro al usuario las monedas que se usan para eso 
print("--------------------------------------------------------")





