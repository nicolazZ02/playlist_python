class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
          self.nombre= nombre
          self.categoria = categoria
          self.precio = precio  #Default: Public, PROTECTED

    def mostrar_informacion (self):
        print(f"Nombre: {self.nombre}, categoria: {self.categoria }, Precio {self.precio}") 

#Instanciar la clase
restaurant = Restaurant("Pizzeria Zuarez", "Comida Italiana", 4000)
print(restaurant.precio)
restaurant.precio = 5000
restaurant.mostrar_informacion()


restaurant2 = Restaurant("Rapido Hamburguesas", "Comida Casual", 3000)
print(restaurant2.precio)
restaurant2.precio = 6000
restaurant2.mostrar_informacion()  