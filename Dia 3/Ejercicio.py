
#Programa General 
print(" ")
print("/----------------------------------------------------/")
print("/       Welcome, Estos son mis programas             /")
print("/                                                    /")
print("/ Selecione una accion a realizar:                   /")
print("/ 1) Programa para determinar un numero primo        /")
print("/ 2) Programa para probar contraseñas                /")
print("/----------------------------------------------------/")

registri=(input())



if registri == 1:
    print("Asi que quieres determinar un numero primo")
    print("El proposito de este programa es saber si el numero ingresado es primo o no")
    print(" ")
    print("Por favor ingrese un numero para determinar si es primo")
    print(" ")

    Num=int(input("Ingrese un numero: "))

    if Num > 1: 
        cont=0
    for i in range (2, Num):
        resto=Num%i
        #print("{} & {} = {}".format(Num, i, resto))
        if resto==0:
            cont+=1
    if cont==0: 
        print("El {} es un numero primo".format(Num))
    else: 
        print("El numumero {} no es un numero primo".format(Num))
else: 
    print("El numumero {} no es un numero primo".format(Num))   




import random

minusculas= "abcdefghijklmnñopqrstuvwxyz"
mayuscula= "ABCDEFHIJKLMNÑOPQRSTUVWXYZ"
numeros= "0,1,2,3,4,5,6,7,8,9"
Simbolos= ""