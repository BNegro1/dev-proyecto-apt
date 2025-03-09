import json

datos = {
    "nombre" : "Juan",
    "edad":25,
    "comuna":"valpo",
    "estudios":["Liceo A-1","DUOC-UC","Diplomado DUOC UC","MIT","NASA"]
}
with open("archivo.json","w") as archivo:
    json.dump(datos,archivo) 

# lectura de json
with open("archivo.json","r") as archivo:
    datos_leidos = json.load(archivo)

print(datos_leidos)