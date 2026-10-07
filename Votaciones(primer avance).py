#Registramos el ciudadano con su numero de DNI
def registrar_ciudadanos_con_su_dni():
    ciudadano = int(input("ciudadano Introduzca su numero de DNI  "))
    print ("Su numero de DNI es", ciudadano)
        

registrar_ciudadanos_con_su_dni()

#Verificacion de los DNI y de huella digital
def verificar_el_registro():
    Ciudadano = int(input("Introduzca su numero de DNI   "))
    verificación = int(input("Verifique su numero de DNI    "))

    if Ciudadano == verificación:
       print ("Introduzca su huella digital ")
       huella = input ("Digite su huella    ")
       if huella == huella:
           print ("Bienvenido al sistema    ")
    else:
        print ("Los dni no coinciden    ")
        exit()
        
verificar_el_registro()

#Guardando el voto en la base de datos
LISTA = ["voto1", "voto2", "voto3"]
def verificar_el_registro():
    ciudadano = input (f"Seleccione uno de los voto que quieres votar en la lista {LISTA}").strip().lower()
    if ciudadano not in LISTA:
        print("Ese no es voto de la lista   ")
        return

    confirmacion = input (f"Confirmar voto {ciudadano} (SI/NO)").lower().strip()
    if confirmacion == "si":
        print ("Gracias por votar su voto se guardo en la base de datos ")
    elif confirmacion == "no":
        print ("Vuelve a votar por otro candidato   ")
    else:
        print ("no se registro ninguna confirmación ")


verificar_el_registro()