def app():
    #crear el archivo
    archivo = open ("archivo.txt", "w") # w es una escritura, si no existe lo creara 

    #generar numeros en archivos
    for i in range(0,20):
        archivo.write("esta es la linea" + str(i)+ "\r\n" )

    #Cerrar el archivo
    archivo.close()
app()