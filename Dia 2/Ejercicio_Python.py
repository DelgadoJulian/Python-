
#Primer Ejercicio 

#Ciclo Fibonansi

print("Bienvenido Señor Usuario")
print("Porfavor ingrese su nombre")
nombre = input()

print("Hola,", nombre, "bienvenido al programa de fibonanci.")

print("Señor,", nombre, "Por favor ingrese un numero entero")
p = input()

print("Agregue el numero en el que quiere que termine la secuencia")
numero = input()


def fib(numero):
    
    a = p
    b = 1

    for J in range(numero):
        c = a + b 
        a = b 
        b = c

        return b 
    
    for J in range(numero):
     print(fib(J))

