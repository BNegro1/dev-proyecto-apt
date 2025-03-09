pikachu = 4500
otaku = 5000
pulpo = 5200
anguila = 4800

contarP = 0
contarO = 0
contarPul = 0
contarA = 0
total = 0

#desc = 0

resp = "si"
while resp == "si":
    contarP = 0
    contarO = 0
    contarPul = 0
    contarA = 0
    total = 0

    while True:
        try:
            print("1. Pikachu Roll $4.500")
            print("2. Otaku Roll $5.000")
            print("3. Pulpo Venenoso Roll $5.200")
            print("4. Anguila Elétrica Roll $4.800")
            print("5. Terminar Pedido")

            opcion = int(input("Ingrese su opción: "))

            if opcion == 1 :
                contarP = contarP + 1
                total = total + pikachu
            else:
                if opcion == 2:
                    contarO = contarO + 1
                    total = total + otaku
                else:
                    if opcion == 3:
                        contarPul = contarPul + 1
                        total = total + pulpo
                    else:
                        if opcion == 4: 
                            contarA = contarA + 1
                            total = total + anguila
                        else:
                            if opcion == 5:
                                break
        except ValueError:
            print("Ingreso de la opción debe ser válida")

    respDesc = input("Tiene codigo de descuento? (si/no)").lower()
    if respDesc == "si":
        while True:
            codigo = input("Ingrese codigo de descuento (soyotaku): ").lower()
            if codigo == "soyotaku":
                desc = total *0.1
                break
            else:
                print("codigo no válido")
                print("Si desea reingresar presione 'ENTER' o salir => presione 'X' : ")
                respX= input().lower()
                if respX == "x":
                    break
    else:
        desc = 0

    totalPagar = total - desc
    sumaCont = contarP + contarO + contarPul + contarA
    print("**************************")
    print(" TOTAL PRODUCTOS ",sumaCont)
    print("**************************")
    print("Pikachu Roll : ",contarP)
    print("Otaku Roll : ",contarO)
    print("Pulpo Venenoso Roll : ",contarPul)
    print("Anguila Eléctrica Roll : ",contarA)
    print("**************************")
    print("Subtotal Por pagar: $",total)
    print("Descuento por código: $",desc)
    print("TOTAL: $",totalPagar)

    resp = input("Desea volver a comprar (si/no): ").lower()

