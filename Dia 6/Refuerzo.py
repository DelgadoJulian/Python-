print("Agregue los numeros separados por espacios:")
Numeros = input().split()

# Aqui en esta seccion procedo a filtar los datos invalidos y comvertir los datos a una lista de enteros
DatosBuenos = []
for Rem in Numeros: #itera en cada uno de los datos 
    num = int(Rem) # comvierte los datos a numeros para poder compararlos
    if 0 <= num <= 300: # agrego la condicion
        DatosBuenos.append(num) # agrego datos a la lista
    else: # si no cumplen nada de eso, le agregue que dijieran datos invalidos
        print(f"El numero {num} es inválido. Debe estar entre el rango 0 a 300.")

# Aqui en esta parte, elimino los duplicados y los comvierto a una lista
Resultado = list(set(DatosBuenos))

print("Resultado sin duplicados:", Resultado) #llamo a la variable con sus resultados correctos


# Realizado por Julian Delgado 
# CC 1093591977

