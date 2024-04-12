#Le doy al usuario la bienvenida al programa. 

print("/---------------------------------------------------/")
print("/                Hola, Bienvenido                   /")
print("/ Por favor ingrese su billete para darle su cambio /")
print("/---------------------------------------------------/")
cambio=int(input())

while cambio < 0:
    print("Uy, ¿hay plata en negativo?, IT'S UNBELIEVABLE!!!")
    print("Agregue otro numero, por favor")
    cambio=(input())
    

if cambio >= 10:
    queda = cambio // 10
    print("En la caja hay "+ str(queda)+ " monedas de 10")
    dinero = cambio % 10

if cambio >= 5:
    queda = cambio // 5
    print("En la caja hay "+ str(queda)+ " monedas de 5")
    dinero = cambio % 5

if cambio >= 1:
    queda = cambio // 1
    print("En la caja hay "+ str(queda)+ " monedas de 1")
    dinero = cambio % 1





    



