import csv
import json

# Leer datos desde el archivo CSV y clasificar empresas
segmentacion_empresas = {
    "Pequeño Contribuyente": [],
    "Mediano Contribuyente": [],
    "Gran Contribuyente": []
}

with open('listadoRutEmpresa.csv', 'r') as archivo:
    escritor = csv.DictReader(archivo)
    for fila in escritor:
        ventas = int(fila['ventas'])
        clasificacion = None
        if ventas <= 100000000:
            clasificacion = "Pequeño Contribuyente"
        elif ventas <= 200000000:
            clasificacion = "Mediano Contribuyente"
        else:
            clasificacion = "Gran Contribuyente"
        
        empresa = {
            "rut": fila['rut'],
            "nombre": fila['nombre'],
            "ventas": ventas
        }
        segmentacion_empresas[clasificacion].append(empresa)

# Guardar datos clasificados en un archivo JSON
with open('segmentacionEmpresas.json', 'w') as archivo:
    json.dump(segmentacion_empresas, archivo,indent=4)

print("Archivo 'segmentacionEmpresas.json' creado exitosamente.")
