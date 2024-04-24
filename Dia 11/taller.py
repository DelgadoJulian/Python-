import time
import os
import json

print("Seleccione una opcion a ejecutar")
time.sleep(2.0)
os.system("cls")

print("-----------------------")
print("(1) Crear Archivo")
print("(2) Actualizar Datos)")
print("(3) Revisar Datos")
print("(4) Eliminar Datos")
print("------------------------")
num = input()

if num == '1':

    with open('large-file.json','r') as openfile:
        miJSON= json.load(openfile)
    #print(type(miJSON))
    '''
    for i in range (5):
    print(miJSON[i])
    '''
    crearEventos=[]
    for i in range (len(miJSON)):
        if(miJSON[i]['type']=='CreateEvent'):
            crearEventos.append(miJSON[i])

    #print(crearEventos[5]['actor']['id'])

    for q in range (5):
        print("#######################")
        print("#### Evento # ",q+1 ,"##")
        print("#######################")
        print("ID: ",crearEventos[q]['id'])
        print("Tipo:",crearEventos[q]['type'])
        print("Actor:")
        print("------- ID:",crearEventos[q]['actor']['id'])

    crearEventos[0]['id']=256
    with open("eventos.json","w") as outfile:
        json.dump(crearEventos,outfile)