#Creando un diccionario simple.
cancion = {
    "G musical" : "Electronica", #Llave y Valor
    "cancion" : "slime to side",
    "Lanzamiento" : 2020,
    "Likes" : 4000
    }

#Acceder a los elementos del diccionario.
print (cancion["G musical"])
print (cancion["Lanzamiento"])

#Mezclar con un string.

artista = cancion["G musical"]
print(f"Estoy escuchando{artista}")  


#Agregar nuevos valores.
cancion ["playlist"] = "hevy metal"
print (cancion)

#Reemplazar valor existente.
cancion["cancion"] = "Seek & destroy" 
print(cancion)

del cancion["Lanzamiento"]
print (cancion)
