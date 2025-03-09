datos=["juan",34,5,True,4.5]

datosNum = [3,4,6,9,1]

print(datos)
print(datos[4])
#print(datos[8])
print()
for i in range(5):
    print(datos[i])

print()
for elemento in datos:
    print(elemento)
print()

datos.reverse()
print(datos)
datosNum.sort()
print(datosNum)
nombres = ["maria","pedro","diego","juan","juana","amelia"]
nombres.sort()
print(nombres)
nombre = input("Ingrese nombre: ").lower()
datos.append(nombre)
print(datos)

datos.insert(3,"Karen")
print(datos)


