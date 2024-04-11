#Segundo Ejercicio
#Juego Interactivo


#Saco un numero random de una biblioteca del programa
import random 

#Creo una variable para guardar el numero que elija el sistema
NumeroAleatorio = random.randint(1,100)

#Creo una mini intro para el usuario
def intro():
    print("*"*40)
    print(" "*10,"ADIVINA EL NUMERO", " "*10)
    print("*"*40)

#Empiezo a crear el ejercicio como tal, para ejecutarlo
def Juegamos():
    intentos = 0
    while True: #formo el ciclo de repeticion
        NomUsuario = int(input("inserta un numero entre el 1 y el 100: "))
        if NomUsuario > NumeroAleatorio: 
            intentos += 1
            print(" ")
            print("El numero a acertar es mas pequeño, intentelo de nuevo.")#Formo condionales para darle pistas al usuario del posible numero 
            
        elif NomUsuario < NumeroAleatorio:
            intentos += 1
            print(" ")
            print("El numero a acertar es mas grande, pruebe de nuevo. ")
            
                
        else: #Si al final lo adivina, el programa imprimira esto.
            intentos += 1
            print(" ")
            print (f"Felicidades acertaste el numero, el numero era el {NumeroAleatorio}, lo adivinaste en {intentos} intentos.")    
            
            break 
  

#Ya a lo ultimo llamamos a las variables
intro()    
Juegamos()


#Desarrollado por Julian David Delgado Villamizar

#CC 1093591977