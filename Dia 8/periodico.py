mensualidad = 60  # Aqui esta el precio de la mensualidad
mensua = 0  # Inicio mensua como 0 para no tener problemas con definirla
Resp = ""  # Variable para respuesta del usuario
import os  # Importo el módulo os para ejecutar comandos del sistema
import re  # Importo el módulo de expresiones regulares que usare en la contraseña
nom = input()  # Solicitamos al usuario que ingrese su nombre

boleanito = True  # Inicia un ciclo que ejecutará el programa principal
nombre = []  # Creo una lista vacía para almacenar los regalos

while boleanito: 
    
    print("/------------------------------------------------/")
    print("/                                                /")
    print("/             BIENVENIDO AL PERIODICO            /")
    print("/                   NEWSPAPER                    /")
    print("/                                                /")
    print("/------------------------------------------------/")
    print("        Seleccione una opción a ejecutar          ")   
    print("                                                  ") # Muestro al usuario el menú principal
    print("/------------------------------------------------/")
    print("/ (1) Crear Cuenta                               /")
    print("/ (2) Iniciar Sesión                             /")
    print("/ (3) Comprar Mensualidad                        /")
    print("/ (4) Regalar Mensualidad                        /")
    print("/ (5) Mostrar Mensualidades Compradas            /")
    print("/ (0) Cerrar Programa                            /")
    print("/------------------------------------------------/")
    opc = input()  # Solicito al usuario que elija una opción
    
    os.system("cls")  # Por medio de este comando , limpio pantalla
    
    
    def verificar_contraseña(contraseña):  # Función para verificar que la contraseña cumpla con ciertos requisitos
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', contraseña):
            return True
        else:
            return False

    if opc == "1": # Creación de cuenta
        
        print("Por favor crea tu nombre de usuario")
        Nombre = input()  # Solicito al usuario que ingrese su nombre
        Año = int(input("Ingrese en qué año está creando su cuenta: "))  # Solicito al usuario que ingrese el año de creación de la cuenta
        while Año < 1990 or Año > 2020:
            print("Lo siento, el año debe estar entre 1990 y 2020.")
            Año = int(input("Ingrese nuevamente el año: "))  # Verifico que el año esté en el rango permitido
        
        
        contraseña_valida = False  # Solicito la contraseña hasta que cumpla con los requisitos
        while not contraseña_valida:
            contra = input("Por favor crea una contraseña (debe contener al menos una letra, un número y un carácter especial, y tener al menos 8 caracteres): ")
            if verificar_contraseña(contra):
                contraseña_valida = True
            else:
                print("La contraseña debe contener al menos una letra, un número y un carácter especial, y tener al menos 8 caracteres.")

        os.system("cls")  # Limpiamos la pantalla

    if opc == "2":   # Inicio de sesión
      
        ingreso_exitoso = False  # Variable para verificar si el inicio de sesión fue exitoso
        while not ingreso_exitoso:
            print("/-----------------------/")
            print("/ Ingresa tu nombre     /")
            nom2 = input()  # Le pido al usuario que ingrese su nombre
            print("/ Ingresa tu contraseña /")
            con2 = input()  # Solicito al usuario que ingrese su contraseña
            
            # Verifico que el nombre y la contraseña coincidan con los registrados
            if nom2 != Nombre or con2 != contra:
                print("Nombre o contraseña incorrectos.")
                print("Presione (N) para intentarlo de nuevo o cualquier otra tecla para volver al menú principal.")
                Resp = input()
                if Resp != "N":
                    break  # Rompo el bucle y volvemos al menú principal
            else:
                ingreso_exitoso = True
                print("Bienvenido Señor:", nom2, "Un gusto conocerlo :)")
                input()
    
    if opc == "3":
        # Compra de mensualidades
        print("Cuantas mensualidades desea comprar")
        print("Cada mensualidad cuesta ", mensualidad, " Pesos")
        mensua = int(input())  # Solicitamos al usuario que ingrese la cantidad de mensualidades a comprar
        print("Total a pagar ", mensualidad * mensua, " Pesos")  # Mostramos el total a pagar

    elif opc == "4":
        # Regalo de mensualidades
        print("Rellene los siguientes campos para el envío")
        print("-------------------------------------------")
        print("Usuario de la persona")
        usu = input()  # Solicitamos al usuario que ingrese el nombre de la persona a la que quiere regalar las mensualidades
        print("Cantidad de mensualidades a comprar para", usu)
        menusu = int(input())  # Solicitamos al usuario que ingrese la cantidad de mensualidades a regalar
        print("Se han comprado", menusu, "mensualidades para", usu)  # Mostramos un mensaje confirmando la compra
        
        nombre.append((usu, menusu))  # Guardamos el nombre de la persona y la cantidad de mensualidades regaladas en la lista 'nombre'

    elif opc == "5": # Mostrar mensualidades compradas y regaladas
        
        print("Mensualidades compradas:")
        print("Para el usuario principal", nom, ":")
        print("Total:", mensua, "mensualidades")  # Muestro las mensualidades compradas por el usuario principal

        print("Mensualidades regaladas:")
        for regalo in nombre:
            print("Para el usuario", regalo[0], "- Total:", regalo[1], "mensualidades")  # Le enseño las mensualidades regaladas

    if opc == "0": # Finalizo el programa el programa
        
        print("Gracias por preferirnos señor ", Nombre ,)
        boleanito = False  # Terminamos el ciclo y cerramos el programa
