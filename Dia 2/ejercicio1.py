#Primer Ejercicio 

#Ciclo Fibonansi



print("Bienvenido Señor Usuario")
print("Porfavor ingrese su nombre")
nombre = input()
print("Hola,", nombre, "Bienvenido al programa de fibonacci.")

x = 0
y = 1
z = 0

while True: 
    print("Por favor ingrese un numero mayor a uno")
    n=int(input())
    if n>1: 
        break 
print("1")
for i in range(0,n):
    z=x+y
    print(f"{z}", end=" ")
    x=y
    y=z
print(" ")

