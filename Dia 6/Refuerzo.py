
print("Dar numeros a la lista")
Num = input()

lista = []
lista.append(Num)
print("Esta es la lista original ", Num )

Valoresborrado = set(Num)
print("Asi quedo la lista despues de borrarlos ", Valoresborrado)

Nuevalista = list(Valoresborrado)
print("Asi queda al final ", Nuevalista)


# Realizado por Julian Delgado

#Profe tiene un error, pero cumple al hecho de eliminar datos repetidos
#En mi casa creo el resto de procesos, ycumplo con las condicionales