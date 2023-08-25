import re


class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
          self.nombre= nombre
          self.categoria = categoria
          self.__precio = precio  #Default: Public, PROTECTED, PRIVATE

    def mostrar_informacion (self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria }, Precio {self.__precio}") 
    # GETTERS Y SETTER - Get = Obtiene un valor, Set = Agrega un valor
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio 


#Instanciar la clase
restaurant = Restaurant("Pizzeria Zuarez", "Comida Italiana", 4000)
#restaurant.__precio= 8000 #No es posible modificarlo con PRIVATE __ 
restaurant.mostrar_informacion()
restaurant.set_precio(5000)
restaurant.get_precio()


restaurant2 = Restaurant("Rapido Hamburguesas", "Comida Casual", 3000)
restaurant2.mostrar_informacion()
restaurant.set_precio(4000)
restaurant2.get_precio()  