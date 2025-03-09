import csv

with open("archivo_csv.csv","r") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        nombre = fila["Nombre"]
        edad = int(fila["Edad"])
        comuna = fila["Comuna"]
        estado_edad = "Mayor de edad " if edad >= 18 else "Menor de edad"
        print(f"{nombre} tiene {edad} años y es {estado_edad} y vive en {comuna}")