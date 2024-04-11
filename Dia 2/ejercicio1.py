#Primer Ejercicio 
#Ciclo Fibonansi


#Le pido sutilmente al usuario que me de su nombre, y le doy la bienvenida a mi programa.
print("Bienvenido Señor Usuario")
print("Porfavor ingrese su nombre")
nombre = input()
print("Hola,", nombre, "Bienvenido al programa de fibonacci.")
print(" ")
print("/------------------------------------------------------------------------/")
print(" ¿Que es Fibonacci? ")
print("En matemática, la sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597…/")
print("/------------------------------------------------------------------------/")
print(" ")
#Defino unas variables para usarlas mas adelante
x = 0
y = 1
z = 0
#Abro un ciclo, para hacer que se repita los procedemientos
while True: 
    print("Por favor ingrese un numero mayor a uno")# Aqui hago un ciclo para obligar que si o si el numero ingresado debe ser mayor a 1
    n=int(input())
    if n>1: 
        break 
print("1")
for i in range(0,n): # Si se cumple lo anterior, se empieza el programa
    z=x+y
    print(f"{z}", end=" ")
    x=y
    y=z
print(" ")

#Desarrollado por Julian David Delgado Villamizar

#CC 1093591977