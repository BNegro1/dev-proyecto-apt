while True:
    try:
        cantidadPasajes = int(input("Ingrese cantidad de pasajes: "))
        break
    except  ValueError as ErrorDigito:
        print("Ingrese un número válido")
total  =0
for i in range(cantidadPasajes):
    
    while True:
        try:
            #print("Ingrese pasaje: ",(i+1))
            precioPasaje = int(input(f"Ingrese pasaje {(i+1)}: "))
            break
        except:
            print("ingrese un precio de pasaje válido")
    total = total + precioPasaje

print("El total de los pasajes es: ",total)