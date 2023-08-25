import re


class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
          self.nombre= nombre
          self.categoria = categoria
          self.precio = precio  #Default: Public, PROTECTED, PRIVATE

    def mostrar_informacion (self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria }, Precio: {self.precio}") 
    # GETTERS Y SETTER - Get = Obtiene un valor, Set = Agrega un valor
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio 

#crear una clase hijo de Restaurant

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, piscina): 
        super().__init__(nombre, categoria, precio)
        self.piscina = piscina
    
    #Reescribir un metodo (Debe llamarse igual)
    def mostrar_informacion (self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria}, Precio: {self.precio}, piscina: {self.piscina}")

    #Agregar un metodo que solo exista en hotel.
    def get_piscina(self):
        return self.piscina

hotel = Hotel("Hotel POO", "5 starts", 200, "si") 
hotel.mostrar_informacion()
piscina = hotel.get_piscina()
print(piscina) 