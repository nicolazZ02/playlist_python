#Revisar si una condicion es mayor a.
balance = 500
if balance > 0:
    print("puedes pagar")
else:
    print("no tienes saldo")

#Likes
likes = 200
if likes >= 200:
    print("enahora buena has ganado 200 likes")
else:
    print("Casi llegas a los 200 likes")

#If con texto
lenguaje = "php"
if not lenguaje == "python":
    print("excelente desicion")

#Evaluar un Booleano.
usuario_autenticado = True
if usuario_autenticado:
    print("Ha Accedido al sistema")

else:
    print("debes inicar sesion") 

#Evaluar un elemento de una lista.
lenguajes = ["Python", "Php", "JavaScript", "Java", "GO"]
if "GO" in lenguajes:
    print("Go si existe")
else:
    print("No esta en la lista")

#If Anidados.
usuario_autenticado = False
usuario_admin = False
if usuario_autenticado:
    if usuario_admin:
        print("ACCESO TOTAL")
    else:
        print("Acceso al sistema")
else:
    print("debes inicar sesion") 


