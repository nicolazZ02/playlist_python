playlist = {} #Diccionario vacio
playlist["canciones"] = [] #lista vacia de canciones


#Funcion Principal
def app():
       
       #Agregar playlist
       agregar_playlist = True
       
       while agregar_playlist:
           nombre_playlist = input("¿Como deseas nombrar la playlist? \r\n")    
           if nombre_playlist:
             playlist["nombre"] = nombre_playlist
             #Ya tenemos un nombre desactivar el True
             agregar_playlist= False
             #mandar a llamar la funcion para agregar canciones.
             agregar_canciones()
def agregar_canciones():
  #Bandera para agregar canciones
  agregar_cancion = True
  
  while agregar_cancion:
    #Preguntar al usuario que cacion desea agregar
    nombre_playlist = playlist["nombre"]
    pregunta = f"\r\nAgrega canciones para la playlist {nombre_playlist} \r\n" 
    pregunta += "escribe 'x' para dejar de agregar canciones \r\n"
    cancion = input(pregunta)
    if cancion == "X":
      #Dejar de agregar canciones
      agregar_cancion = False
      #Mostrar resumen de la playlist
      mostrar_resumen()

    else:
      #Agregar canciones
      playlist["canciones"].append(cancion)

def mostrar_resumen():
  nombre_playlist = playlist["nombre"]
  print(f"Playlist: {nombre_playlist}\r\n")
  print("canciones:\r\n")
  for cancion in playlist["canciones"]:
    print(cancion)
    


app()

