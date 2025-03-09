'''Crear un programa de validación de usuario y contraseña 
(consultar usuario y contraseña), los únicos dos usuarios conectados son:
User1: pedro   	Contraseña1: 1234
User2: angel		Contraseña2: a4s1
'''

user = input("Ingrese usuario: ")
passw = input("Ingrese contraseña: ")

if user == "pedro" and passw == "1234":
    print("Usuario conectado")
else:
    if user == "angel" and passw == "a4s1":
        print("Usuario conectado")
    else:
        print("usuario no registrado!")



