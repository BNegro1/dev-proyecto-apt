import csv

with open("archivo_csv.csv","w",newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Nombre","Edad","Comuna"])
    escritor_csv.writerows([
        ["Juan",24,"Valpo"],
        ["Maria",16,"Vina"],
        ["Pedro",30,"Quilpue"],
        ["Diego",18,"Limache"],
        ["Fran",26,"Calera"]
    ])



#lectura de csv
with open("archivo_csv.csv","r",newline="") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)