import funciones as fn
import csv
# lista = []

# lista = ["juan",23,"masculino","femenino",45]

# print(lista[0])
# print(lista[3])

# print(lista)

# dato = input("Ingrese un dato: ")

# lista.append(dato)
# print(lista)

# lista2 = [1,2,3,4]

# print("------")
# for dato in lista:
#     print(dato)
# print("*******")
# for i in range(len(lista)):
#     print(lista[i])

#"matrices"
    
matriz = [
    [1,2,3],
    [4,5,6]
]

print(matriz)

print(matriz[1][2])


matriz.append([7,8,9])

print(matriz)
print(matriz[2][2])
#print(matriz,end='')

for fila in matriz:
    for dato in fila:
        print(dato)

print("------")
for i in range(3):
    for j in range(3):
        print(matriz[i][j])


print("diccionarios")
# diccionarios
        
alumno = {
    "rut" : "123-1",
    "nombre" : "juan",
    "carrera" : "Ingenieria"

}

print(alumno)

listaAlumnos = []

resp = "si"
while resp == "si":
    rut = input("Ingrese su rut: ")
    nombre = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")
    print()
    resp = input("Desea ingresar otro alumno? (si/no): ").lower()

    alumno = {
        "rut" : rut,
        "nombre" : nombre,
        "carrera" : carrera
    }

    listaAlumnos.append(alumno)

print(listaAlumnos)
print("---FOR----")
for dato in listaAlumnos:
    print(dato)


fn.saludo()

##archivo
campos = listaAlumnos[0].keys()

with open("archivo.csv","w") as archivo:
    escritor = csv.DictWriter(archivo,fieldnames=campos)
    escritor.writeheader() ## se usa para diccionarios 
    #escritor.writerow(["rut","nombre","carrera"]) se usa para archivos planos.
    escritor.writerows(listaAlumnos)



