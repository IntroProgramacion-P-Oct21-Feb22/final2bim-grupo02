"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""


def crear_facebook():
    """
        explicación de método
    """
    print("Creando cuenta de Facebook\n")
    nombre_user = input("Ingresar el nombre de usuario: ")
    edad_user = int(input("Edad del usuario: "))
    ciudad_user = input("Ingresar la ciudad de origen del Usuario: ")
    pais_user = input("Ingresar el país de origen del usuario: ")
    correo_user = input("Ingresar el correo electrónico del Usuario: ")
    datos_obtenidos = ("-------------------\n"
                       "Datos Ingresados:\nNombre: {}\nEdad: {}\nCiudad: {}\nPaís: {}\nCorreo Electrónico: {}"
                       .format(nombre_user, edad_user, ciudad_user, pais_user, correo_user))
    return datos_obtenidos


def crear_twitter():
    """
        explicación de método
    """
    nombre_user = input("Ingresar el nombre de usuario: ")
    nombre = input("Ingresar nombres (solo nombres): ")
    apellido = input("Ingresar sus apellidos: ")
    edad_user = int(input("Edad del usuario: "))
    ciudad_user = input("Ingresar la ciudad de origen del Usuario: ")
    pais_user = input("Ingresar el país de origen del usuario: ")
    idioma = input("Ingrese su idioma: ")
    correo_user = input("Ingresar el correo electrónico del Usuario: ")

    datos_obtenidos = ("-------------------\n"
                       "Datos Ingresados:\nUsuario: {}\nNombre: {}\nApellido: {}\nEdad: {}\nCiudad: {}\n"
                       "País: {}\nIdioma: {}\nCorreo Electrónico: {}"
                       .format(nombre_user, nombre, apellido, edad_user, ciudad_user, pais_user, idioma, correo_user))
    print(datos_obtenidos)


def crear_whatsapp():
    print("Proceso Inicial")
    nombre_user = input("Ingresar el nombre de Usuario: ")
    numero_user = input("Ingresar número de Teléfono: ")
    edad_user = int(input("Ingresar la edad del usuario: "))
    ciudad_user = input("Ingresar la ciudad de Origen del Usuario: ")
    pais_user = input("Ingresar el país de origen del usuario: ")
    datos_obtenidos = ("-------------------\n"
                       "Datos Ingresados:\nNombre: {}\nNúmero de teléfono: {}\n"
                       "Edad del Usuario: {}\nCiudad: {}\nPaís:{}"
                       .format(nombre_user, numero_user, edad_user, ciudad_user, pais_user))
    return datos_obtenidos


def crear_telegram():
    print("Proceso inicial: ")
    nombre_user = input("Ingresar el nombre de usuario: ")
    numero_tel = int(input("Ingrese su número de teléfono: "))
    ciudad_user = input("Ingresar la ciudad de origen del Usuario: ")
    pais_user = input("Ingresar el país de origen del usuario: ")
    area_inte = input("Ingrese su área de interés: ")

    datos_obtenidos = ("-------------------\n"
                       "Datos Ingresados:\nUsuario: {}\nNúmero de teléfono: {}\nCiudad: {}\n"
                       "País: {}\nÁrea de Interés: {}"
                       .format(nombre_user, numero_tel, ciudad_user, pais_user, area_inte))
    print(datos_obtenidos)


def crear_signal():
    print("proceso inicial: ")
    nombre_user = input("Ingresar el nombre de Usuario: ")
    numero_user = input("Ingresar número de Teléfono: ")
    ciudad_user = input("Ingresar la ciudad de Origen del Usuario: ")
    pais_user = input("Ingresar el país de origen del usuario: ")
    hobby_user = int(input("Ingresar el hobby principal del Usuario: "))
    datos_obtenidos = ("-------------------\n"
                       "Datos Ingresados:\nNombre: {}\nNúmero de teléfono: {}\n"
                       "Ciudad: {}\nPaís:{}\nHobby del Usuario: {}"
                       .format(nombre_user, numero_user, ciudad_user, pais_user, hobby_user))
    return datos_obtenidos


def crear_instagram():
    print("proceso inicial: ")
    nombre_user = input("Ingresar el nombre de usuario: ")
    ciudad_user = input("Ingresar la ciudad de origen del Usuario: ")
    edad_user = int(input("Edad del usuario: "))
    correo_user = input("Ingresar el correo electrónico del Usuario: ")
    datos_obtenidos = ("-------------------\n"
                       "Datos Ingresados:\nNombre: {}\nCiudad: {}\nEdad: {}\nCorreo Electrónico: {}"
                       .format(nombre_user, ciudad_user, edad_user, correo_user))
    print(datos_obtenidos)


def crear_flickr():
    print("proceso inicial: ")

    nombre_user = input("Ingresar el nombre de usuario: ")
    correo_user = input("Ingresar el correo electrónico del Usuario: ")

    datos_obtenidos = ("-------------------\n Datos Ingresados:\nUsuario: {}\n"
                       "Correo Electrónico: {}".format(nombre_user, correo_user))
    return datos_obtenidos


def main():
    print("proceso inicial: ")
    cadena_campana = ""
    contador = 0
    bandera = True
    mensaje_final = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    respuestas_negativas = ["No", "no", "NO", "nO"]
    while bandera:
        respuesta = int(input("Ingrese un número del 1 al 7 para registrar datos en la cuenta que desee\n"
                              "[1]Facebook\n[2]Twitter\n[3]Whatsapp\n[4]Telegram\n[5]Signal\n"
                              "[6]Instagram\n[7] Flickr\n"))
        contador += 1
        if respuesta == 1:
            cuenta_faceboook = crear_facebook()
            print(cuenta_faceboook)
        elif respuesta == 2:
            crear_twitter()
        elif respuesta == 3:
            cuenta_whatsapp = crear_whatsapp()
            print(cuenta_whatsapp)
        elif respuesta == 4:
            crear_telegram()
        elif respuesta == 5:
            cuenta_signal = crear_signal()
            print(cuenta_signal)
        elif respuesta == 6:
            crear_instagram()
        elif respuesta == 7:
            crear_flickr()
        banderin = input("¿Desea registrar más cuentas? [Si][No]")
        if banderin in respuestas_negativas:
            bandera = False
        if 1 <= contador <= 5:
            cadena_campana = ("{}".format(mensaje_final[0]))
        elif 5 < contador <= 16:
            cadena_campana = ("{}".format(mensaje_final[1]))
        elif contador > 16:
            cadena_campana = ("{}".format(mensaje_final[2]))

        print("Se ha registrado un total de {}\n{}".format(contador, cadena_campana))


if __name__ == "__main__":
    main()
