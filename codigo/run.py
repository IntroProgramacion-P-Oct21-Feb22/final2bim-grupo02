"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:

Para declarar métodos utilizamos la palabra reservada en Python def nombre_de_la_funcion (parámetros a recibir),
en caso de los procedimientos solamente presentamos la acumulación de los datos al final de nuestro procedimiento,
en cambio si vamos a crear una función debesmos guardar todo en una variable, para esta finalmente retornarla al main.
    """


def crear_facebook():
    """
     El ejercicio nos pide crear una función, es decir que va a retornar un valor.
     La función crear_facebook va a solicitar los siguientes datos: nombre de usuario,
     edad, ciudad, pais, correo electrónico. Cada una de estos datos van ser pedidos
     por teclado y se van a guardar en las variables nombre_user, edad_user, ciudad_user,
     pais_user, correo_user, datos_obtenidos respectivamente. Finalmente almacena en la
     variable datos_obtenidos para ser retornada al método main.

    """
    print("Creando cuenta de Facebook\n")
    bandera = True
    respuestas_positivas = ["SI", "si", "Si", "sI", "Siuu"]
    datos_obtenidos = ""
    while bandera:
        nombre_user = input("Ingresar el nombre de usuario: ")
        edad_user = int(input("Edad del usuario: "))
        ciudad_user = input("Ingresar la ciudad de origen del Usuario: ")
        pais_user = input("Ingresar el país de origen del usuario: ")
        correo_user = input("Ingresar el correo electrónico del Usuario: ")
        datos_obtenidos = ("-------------------\n"
                           "Datos Ingresados:\nNombre: {}\nEdad: {}\nCiudad: {}\nPaís: {}\nCorreo Electrónico: {}"
                           .format(nombre_user, edad_user, ciudad_user, pais_user, correo_user))
        answer_user = input("¿Los datos ingresados son correctos? Ingrese [SI] para confirmar "
                            "o [No] para volver a ingresar los datos correctamente")
        if answer_user in respuestas_positivas:
            bandera = False
    return datos_obtenidos


def crear_twitter():
    """
    Explicación de método
        En este apartado, realizamos el método crear_twitter,
        el cual no devuelve un valor como lo indica su principal característica.
        En este apartado pedimos por teclado el nombre de usuario, nombres, apellidos, edad,
        ciudad, pais, idioma, correo electrónico. Todos estos datos ingresados
        por teclado serán asimilados respectivamente en las variables nombre_user,
        nombre, apellido, edad_user, ciudad_user, pais_user, idioma,  correo_user.
        Una vez realizado este proceso, se acumulan todos los datos obtenidos en una cadena acumuladora,
        que en este caso sería datos_obtenidos. Por consiguiente se procede a presentar en
        pantalla los datos_obtenidos y se finaliza el método.
    """
    bandera = True
    respuestas_positivas = ["SI", "si", "Si", "sI", "Siuu"]
    datos_obtenidos = ""
    while bandera:
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
                           "País: {}\nIdioma: {}\nCorreo Electrónico: {}".format(nombre_user, nombre, apellido,
                                                                                 edad_user, ciudad_user,
                                                                                 pais_user, idioma, correo_user))

        answer_user = input("¿Los datos ingresados son correctos? Ingrese [SI] para confirmar "
                            "o [No] para volver a ingresar los datos correctamente")
        if answer_user in respuestas_positivas:
            bandera = False
    print(datos_obtenidos)


def crear_whatsapp():
    """
        Explicación del método:
    crear_whatsapp es una función ya que va a retornar un valor, en esta fucnión vamos a pedir por teclado
    los siguientes datos: nombre de usuario, número de teléfono, edad, ciudad, pais,
    los cuales serán almacenados en las variables nombre_user, numero_user, edad_user, ciudad_user,
    pais_user respectivamente. Finalmente para retornar los datos obtenidos hemos declarado una variable acumuladora,
    en este caso datos_obtenidos, la cual va a ser retornada al método principal.
    """
    print("Proceso Inicial")
    bandera = True
    respuestas_positivas = ["SI", "si", "Si", "sI", "Siuu"]
    datos_obtenidos = ""
    while bandera:
        nombre_user = input("Ingresar el nombre de Usuario: ")
        numero_user = input("Ingresar número de Teléfono: ")
        edad_user = int(input("Ingresar la edad del usuario: "))
        ciudad_user = input("Ingresar la ciudad de Origen del Usuario: ")
        pais_user = input("Ingresar el país de origen del usuario: ")
        datos_obtenidos = ("-------------------\n"
                           "Datos Ingresados:\nNombre: {}\nNúmero de teléfono: {}\n"
                           "Edad del Usuario: {}\nCiudad: {}\nPaís:{}"
                           .format(nombre_user, numero_user, edad_user, ciudad_user, pais_user))
        answer_user = input("¿Los datos ingresados son correctos? Ingrese [SI] para confirmar "
                            "o [No] para volver a ingresar los datos correctamente")
        if answer_user in respuestas_positivas:
            bandera = False
    return datos_obtenidos


def crear_telegram():
    """
    Explicación de método
        En este apartado, realizamos el método crear_telegram,
        el cual no devuelve un valor como lo indica su principal característica.
        En este apartado pedimos por teclado el nombre de usuario, número de teléfono,
        ciudad, pais, área de interés. Todos estos datos ingresados por teclado
        serán asimilados respectivamente en las variables nombre_user, numero_tel,
        ciudad_user, pais_user, area_inte. Una vez realizado este proceso,
        se acumulan todos los datos obtenidos en una cadena acumuladora,
        que en este caso sería datos_obtenidos.
        Por consiguiente se procede a presentar en pantalla los datos_obtenidos y se finaliza el método.
    """
    print("Proceso inicial: ")
    bandera = True
    respuestas_positivas = ["SI", "si", "Si", "sI", "Siuu"]
    datos_obtenidos = ""
    while bandera:
        nombre_user = input("Ingresar el nombre de usuario: ")
        numero_tel = input("Ingrese su número de teléfono: ")
        ciudad_user = input("Ingresar la ciudad de origen del Usuario: ")
        pais_user = input("Ingresar el país de origen del usuario: ")
        area_inte = input("Ingrese su área de interés: ")

        datos_obtenidos = ("-------------------\n"
                           "Datos Ingresados:\nUsuario: {}\nNúmero de teléfono: {}\nCiudad: {}\n"
                           "País: {}\nÁrea de Interés: {}"
                           .format(nombre_user, numero_tel, ciudad_user, pais_user, area_inte))
        answer_user = input("¿Los datos ingresados son correctos? Ingrese [SI] para confirmar "
                            "o [No] para volver a ingresar los datos correctamente")
        if answer_user in respuestas_positivas:
            bandera = False
    print(datos_obtenidos)


def crear_signal():
    """
    Explicación del método
        El método crear_signal es considerado función, ya que nos va a retornar un valor,
        un dato que nosotros hayamos decidido retornar. crear_signal va a solicitar
        los siguientes datos para ser ingresados por el usuario: nombre de usuario,
        número de teléfono, ciudad, pais, hobby principal los cuales serán almacenados
        en la variables: nombre_user, numero_user, ciudad_user, pais_user, hobby_user respectivamente.
        Luego los datos obtenidos lo vamos a almacenar en una variable de tipo cadena datos_obtenidos,
        para finalmente retornar la misma al método principal o main.
    """
    print("proceso inicial: ")
    bandera = True
    respuestas_positivas = ["SI", "si", "Si", "sI", "Siuu"]
    datos_obtenidos = ""
    while bandera:

        nombre_user = input("Ingresar el nombre de Usuario: ")
        numero_user = input("Ingresar número de Teléfono: ")
        ciudad_user = input("Ingresar la ciudad de Origen del Usuario: ")
        pais_user = input("Ingresar el país de origen del usuario: ")
        hobby_user = input("Ingresar el hobby principal del Usuario: ")
        datos_obtenidos = ("-------------------\n"
                           "Datos Ingresados:\nNombre: {}\nNúmero de teléfono: {}\n"
                           "Ciudad: {}\nPaís:{}\nHobby del Usuario: {}"
                           .format(nombre_user, numero_user, ciudad_user, pais_user, hobby_user))
        answer_user = input("¿Los datos ingresados son correctos? Ingrese [SI] para confirmar "
                            "o [No] para volver a ingresar los datos correctamente")
        if answer_user in respuestas_positivas:
            bandera = False

    return datos_obtenidos


def crear_instagram():
    """
     explicación de método
        En este apartado, realizamos el método crear_instagram, el cual no devuelve un valor
        como lo indica su principal característica.
        En este apartado pedimos por teclado el nombre de usuario, ciudad, edad, correo electrónico.
        Todos estos datos ingresados por teclado serán asimilados respectivamente en las variables
        nombre_user, ciudad_user, edad_user, correo_user. Una vez realizado este proceso,
        se acumulan todos los datos obtenidos en una cadena acumuladora,
        que en este caso sería datos_obtenidos.
        Por consiguiente se procede a presentar en pantalla los datos_obtenidos y se finaliza el método.

        """
    print("proceso inicial: ")
    bandera = True
    respuestas_positivas = ["SI", "si", "Si", "sI", "Siuu"]
    datos_obtenidos = ""
    while bandera:
        nombre_user = input("Ingresar el nombre de usuario: ")
        ciudad_user = input("Ingresar la ciudad de origen del Usuario: ")
        edad_user = int(input("Edad del usuario: "))
        correo_user = input("Ingresar el correo electrónico del Usuario: ")
        datos_obtenidos = ("-------------------\n"
                           "Datos Ingresados:\nNombre: {}\nCiudad: {}\nEdad: {}\nCorreo Electrónico: {}"
                           .format(nombre_user, ciudad_user, edad_user, correo_user))
        answer_user = input("¿Los datos ingresados son correctos? Ingrese [SI] para confirmar "
                            "o [No] para volver a ingresar los datos correctamente")
        if answer_user in respuestas_positivas:
            bandera = False
    print(datos_obtenidos)


def crear_flickr():
    """
     Explicación del método:
        En este apartado, realizamos la función crear_flickr,
        el cual retorna un valor como lo indica su principal característica.
        En este apartado pedimos por teclado el nombre de usuario y correo electrónico.
        Todos estos datos ingresados por teclado serán asimilados respectivamente
        en las variables nombre_user, correo_user. Una vez realizado este proceso,
        se acumulan todos los datos obtenidos en una cadena acumuladora,
        que en este caso sería datos_obtenidos. Por consiguiente se procede a retornar hasta
        el main los datos obtenidos  y así finalizar la función.
    """
    print("proceso inicial: ")
    bandera = True
    respuestas_positivas = ["SI", "si", "Si", "sI", "Siuu"]
    datos_obtenidos = ""
    while bandera:
        nombre_user = input("Ingresar el nombre de usuario: ")
        correo_user = input("Ingresar el correo electrónico del Usuario: ")

        datos_obtenidos = ("-------------------\n Datos Ingresados:\nUsuario: {}\n"
                           "Correo Electrónico: {}".format(nombre_user, correo_user))
        answer_user = input("¿Los datos ingresados son correctos? Ingrese [SI] para confirmar "
                            "o [No] para volver a ingresar los datos correctamente")
        if answer_user in respuestas_positivas:
            bandera = False
    return datos_obtenidos


def crear_mensaje(a):
    """
    Explicación del método
        crear_mensaje es una función, ya que var a devolver un valor, en este caso un valor de tipo String
        al método principal. crear_mensaje recibe como parámetros solamente el contador, el cual nos da
        la cantidad de cuentas creadas por el usuario para que, con condicionales, discriminar el tipo de
        campaña y finalmente devolver en la variable cadena_campana de tipo cadena, la cual va a devolverse al main
        para presentar el mensaje que se le dio en este apartado.
    """
    mensaje_final = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    cadena_campana = ""

    if 1 <= a <= 5:
        cadena_campana = ("{}".format(mensaje_final[0]))
    elif 5 < a <= 16:
        cadena_campana = ("{}".format(mensaje_final[1]))
    elif a > 16:
        cadena_campana = ("{}".format(mensaje_final[2]))
    return cadena_campana


def main():
    print("proceso inicial: ")
    options = [1, 2, 3, 4, 5, 6, 7]
    cadena_campana = ""
    contador = 0
    bandera = True
    respuestas_negativas = ["No", "no", "NO", "nO"]
    while bandera:
        respuesta = int(input("Ingrese un número del 1 al 7 para registrar datos en la cuenta que desee\n"
                              "[1]Facebook\n[2]Twitter\n[3]Whatsapp\n[4]Telegram\n[5]Signal\n"
                              "[6]Instagram\n[7] Flickr\n"))
        contador += 1
        if respuesta not in options:
            print("Dato ingresado no admitido, ingresar un número del 1 al 7.")
            contador -= 1
        elif respuesta == 1:
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
            cadena_campana = crear_mensaje(contador)

    print("Se ha registrado un total de {} cuenta/as\n{}\nGracias por registrar cuetas en nuestro programa"
          .format(contador, cadena_campana))


if __name__ == "__main__":
    main()
