# # Ejercicio 1: Frecuencia de Palabras en un Texto
# texto = input("Ingrese un texto: ")
# palabras = texto.split()
# #print(palabras)
# frecuencia_palabras = {}
# for palabra in palabras:
#     palabra = palabra.lower()  
#     frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
# print("Frecuencia de palabras:")
# for palabra, frecuencia in frecuencia_palabras.items():
#     print(f"{palabra}: {frecuencia}")


## tuplas
datos_personales = []

while True:
    nombre = input("Ingrese un nombre: ")
    if nombre.lower() == "fin":
        break
    edad = int(input("Ingrese la edad: "))
    datos_personales.append((nombre, edad))

#edades_unicas = {edad for _, edad in datos_personales}
edades_unicas = {edad for _, edad in datos_personales}

print("Edades únicas presentes:", edades_unicas)
