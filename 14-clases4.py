import re


class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
          self.nombre= nombre
          self.categoria = categoria
          self.__precio = precio  #Default: Public, PROTECTED, PRIVATE

    def mostrar_informacion (self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria }, Precio: {self.__precio}") 
    # GETTERS Y SETTER - Get = Obtiene un valor, Set = Agrega un valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio 

#crear una clase hijo de Restaurant

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio): 
        super().__init__(nombre, categoria, precio)

hotel = Hotel("Hotel POO", "5 starts", 200) 
hotel.mostrar_informacion()

