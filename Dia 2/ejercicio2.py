#Segundo Ejercicio

#Juego Interactivo

import random 

NumeroAleatorio = random.randint(1,100)

def intro():
    print("*"*40)
    print(" "*10,"ADIVINA EL NUMERO", " "*10)
    print("*"*40)

def Juegamos():
    intentos = 0
    while True:
        NomUsuario = int(input("inserta un numero entre el 1 y el 100: "))
        if NomUsuario > NumeroAleatorio: 
            intentos += 1
            print("El numero a acertar es mas pequeño, intentelo de nuevo.")
        elif NomUsuario < NumeroAleatorio:
            intentos += 1
            print("El numero a acertar es mas grande, pruebe de nuevo. ")
                
        else: 
            intentos += 1
            print (f"Felicidades acertaste el numero, el numero era el {NumeroAleatorio}, lo adivinaste en {intentos} intentos.")    
            break 
  


intro()    
Juegamos()

