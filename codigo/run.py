"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""

def crearFacebook() :
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
def crearTwitter():
    """
        explicación de método
    """
    cadena = "%s\n" % ("Creando cuenta de Twitter")
    return cadena
def crearWhatsapp():
    
# agregar los métodos faltantes

# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
def main():
    print("proceso inicial: ")

    respuesta = input("Ingrese un número del 1 al 7 para registrar datos en la cuenta que desee\n"
                "[1] Facebook\n"
                "[2] Twitter\n"
                "[3] Whatsapp\n"
                "[4] Telegram\n"
                "[5] Signal\n"
                "[6] Instagram\n"
                "[7] Flickr\n")
    if respuesta == 1:
        cuenta_faceboook = crearFacebook()
        print(cuenta_faceboook)
    elif respuesta == 2:
        crearTwitter()

    elif respuesta == 3:


        """
        Leer las indicaciones para que el proceso cumpla
        lo solicitado.	
        """
if __name__ == "__main__":
    main()



