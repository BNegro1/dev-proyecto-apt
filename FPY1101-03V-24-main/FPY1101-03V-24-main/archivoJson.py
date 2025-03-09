import json

datos = {
    "nombre" : "Juan",
    "edad" : 24,
    "comuna" : "valpo",
    "estudios":["liceo A-4","DUOC-UC","Harvard","MIT","NASA"]
}

with open('archivo.json','w') as archivo:
    json.dump(datos,archivo)

# lectura

with open('archivo.json','r') as archivo:
    datos_leidos = json.load(archivo)
print(datos_leidos)

