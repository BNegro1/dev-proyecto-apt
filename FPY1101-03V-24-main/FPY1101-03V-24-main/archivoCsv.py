import csv

with open('datos_csv.csv','w',newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Nombre','Edad','Comuna'])
    escritor_csv.writerows([
        ['Juan',24,'Valpo'],
        ['Maria',15,'Limache'],
        ['Diego',41,'Quilpue'],
        ['Pedro',12,'Vina'],
        ['Fran',31,'Villa Alemana']
    ])

#abrir archivo
with open('datos_csv.csv','r',newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)



