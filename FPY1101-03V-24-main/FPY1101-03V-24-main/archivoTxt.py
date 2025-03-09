# datos = """
#     Esta seccion cada vez son menos...deben sentirse orgullosos
#     somos los mejores    
# """

# with open('datos.txt','w') as archivo:
#     archivo.write(datos)

#ver archivo o abriendo
#opcion 1
with open('datos.txt','r') as archivo:
    contenido = archivo.read()
print(contenido)

#opcion 2
archivo = open('datos.txt','r')
contenido = archivo.read()
print(contenido)
archivo.close()





