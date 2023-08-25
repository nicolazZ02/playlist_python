lenguajes = ["Python", "Php", "JavaScript", "Java"]

print(lenguajes)

#Los arrays (list) comienzan en la posicion 0.

print(lenguajes[0]) #Python

#Ordenar los elementos.

lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto. 

aprender = f"Estoy aprendiendo {lenguajes[3]}"
print(aprender)

#Modificando valores de un arreglo (list).

lenguajes[1] = "Kotlin"
print(lenguajes)

#Agregar elementos a un arreglo (list). 

lenguajes.append("Ruby")
print(lenguajes)

#Eliminar un arreglo (list). 
del lenguajes[1]
print(lenguajes)

#Eliminar un arreglo (list). 
lenguajes.pop() #Eliminar el ultimo elemento.
print(lenguajes)

#Eliminar con pop en cualquier posicion.
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombres.
lenguajes.remove("Php")
print(lenguajes)