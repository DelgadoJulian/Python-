#-------------------------------------------------
#--------------DIA CHEAT SHEET PYTHON ************
#-------------------------------------------------

#Imprimir HELLO WORD
print("Hello Wooord")


#datos Primitivos 

#Numero
numerito = 1 #Nombre variable = valor
print (numerito) #imprimir(variable)
print(type(numerito)) #Imprimir(tipo(variable))

#Decimal 
numeritoDecimal = 1.1 
print (numeritoDecimal)
print (type(numeritoDecimal))

#Boleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito)) 

# Cadena de texto
texto = "Mi Tibu"
print(texto)
print(type(texto))


#   /----------------------------------------------------
#   /Ingresar por teclado la informacion (Imput)        /
#   /                                                   /
#   / Comversion de tipos de variable                   /
#   /                                                   /
#   / Bucles For y While                                /
#   /                                                   /
#   / Funciones(4 tipos)                                /
#   /                                                   /
#   /----------------------------------------------------

# Desarrollado por Julian Delgado CC: 1093591977 



# Ejercicio 1 : Ingresar por teclado la informacion (Input)

print("Hola este es mi primer mensaje de python")
print("Porfavor ingrese su nombre: ")

nombre = input() 

print("Bienvenido al sistema ", nombre, ". Gracias por usar mi programa.")

###################################################################
# Ejercicio 2 : Comversion de tipos de variable

f = 57 
print(float(f))

# comvertir flotante a entero
int(390.8)

b = 125.4
c = 254.8

print(int(b))
print(int(c))

# Comversion mediante division

a = 8/2
print(int(a))



#####################################################################
#Bucles For y While 
 #Bucle White
x=0
while(x<5):
    x=x+1
print(x)

#Bucle For

for x in range (2,7):
    print(x)

months = ["jan", "Feb", "Mar", "April", "May", "June"] 
for i, m in enumerate (months):
    i = i+1 
    print(i,m)

######################################################################
#Funciones 4 tipos 
