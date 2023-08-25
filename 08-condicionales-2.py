#Ejemplo con Elif.
ocupacion = "desempleado"
if ocupacion == "estudiante":
    print("tienes 50% de descuento")
elif ocupacion == "jubilado":
    print("tienes 70% de descuento")
elif ocupacion == "desempleado":
    print("tienes un 15% de descuento")
else:
    print("debes pagar el 100%")