from os import makedirs
import os


#Mayusculas es constante.
CARPETA ='contactos/' #carpeta de contactos
EXTENSION = ".txt" #Extension de archivos

#Clase de contactos
class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre= nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    
    #Revisa si la carpeta existe o no.
    crear_directorio()

    #Muestra el menu de opcione.
    mostrar_menu ()

    #preguntar al usuario la accion a realizar

    preguntar = True
    while preguntar: 
        opcion = input("Selecione una opcion: \r\n")
        opcion = int(opcion)

        #ejecutar las opciones.
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('Editar contacto')
            preguntar = False
        elif opcion == 3:
            print('Ver contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar contacto')
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')


def agregar_contacto():
    print("escribe los datos para agregar el nuevo contacto")
    nombre_contacto = input("Nombre del contacto:\r\n")

    with open (CARPETA + nombre_contacto+ EXTENSION, "w") as archivo:

        #Resto de los campos.
        telefono_contacto=input("Agrega el telefono:\r\n")
        categoria_contacto= input("Categoria contacto: \r\n")

        #Instanciar la clase
        contacto= Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

        #Escribir en el archivo.
        archivo.write("Nombre:" + contacto.nombre + '\r\n')
        archivo.write("Telefono:" + contacto.telefono + '\r\n')
        archivo.write("Categoria:" + contacto.categoria + '\r\n')

        #Mostrar un mensaje de exito.
        print("\r\n Contacto creado conrrectamente \r\n")

def mostrar_menu ():
    print("Seleccione del menu lo que desea hacer: ")
    print('1) Agregar nuevo contacto')
    print('2) Editar un contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')


def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear la carpeta.
        os.makedirs(CARPETA)


app()