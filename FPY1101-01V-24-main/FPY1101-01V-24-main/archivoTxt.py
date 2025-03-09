datos = """
    Este curso es el mejor de todos, me siento
    orgulloso de ser su profesor!!!
    promedio del curso 5.5
"""

with open('datos.txt','w') as archivo:
    archivo.write(datos)

# lectura de archivo txt
#opcion 1 
with open("datos.txt","r") as archivo:
    contenido = archivo.read()
print(contenido)

#opcion 2
archivo = open("datos.txt","r")
contenido2 = archivo.read()
print(contenido2)
archivo.close()
