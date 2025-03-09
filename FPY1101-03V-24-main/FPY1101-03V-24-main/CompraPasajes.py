# solicitar la cantidad de pasajes
while True:
    try:
        cantidadPasajes = int(input("Por favor, ingrese cantidad de pasajes: "))
        break
    except ValueError:
        print("Por favor, ingrese un valor númerico")

#inicializar total , esto para calcular total de pasajes.
total = 0
# for para iterar la cantidad de pasajes ingresados
for i in range(cantidadPasajes):
    while True:
        try:
            precioPasaje = int(input(f"Ingrese el precio del pasaje {i+1}: "))
            #Acumular precio de los pasajes
            total = total + precioPasaje
            break
        except:
            print("Por favor, ingrese un valor númerico válido")

#mostrar el total de ingresos por la venta de pasajes
#print("El monto total de ventas de pasajes es: ",total)
print(f"El monto total de ventas de pasajes es: {total}")


