deuda = 100000
saldo = 100000

while True:
    try:
        print("           MENU           ")
        print("**************************")
        print("1. Pago Tarjeta de crédito")
        print("2. Simulación de Compras")
        print("3. Salir")
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            print("PAGA")
            while True:
                try:
                    print("Su saldo es: $",saldo)
                    print("Su deuda es: $",deuda)
                    montoPago = int(input("Ingrese monto a pagar: "))
                    if montoPago < 0 :
                        print("El monto debe ser mayor a cero")
                    else:
                        if montoPago > deuda:
                            print("Pago excede deuda")
                        else:
                            deuda = deuda - montoPago # deuda -= montoPago
                            print("Ud pago: $",montoPago)
                            saldo = saldo + montoPago
                            print("Su saldo es: $",saldo)
                            break  # cuando funciona coloco el break        

                except:
                    print("Ingrese un monto a pagar válido")
        else:
            if opcion == 2 :
                print("COMPRA")
                cantidadCompras=int(input("Ingrese cantidad de compras: "))
                for i in range(cantidadCompras):
                    print("Compra ",(i+1))
                    try:
                        montoCompra = int(input("Ingrese el monto de la compra: "))
                        if montoCompra <= 0:
                            print("El monto debe ser mayor a cero")
                        else:
                            if saldo >= montoCompra:
                                deuda = deuda + montoCompra
                                saldo = saldo - montoCompra
                                print("UD compro un monto de $",montoCompra)
                            else:
                                print("Saldo insuficiente")
                    except:
                        print("Debe ingresar un valor numerico al valor de la compra")
            else:
                if opcion == 3 :
                    print("Saliendo....")
                    break
    except:
        print("Debe ingresar una opción válida del 1 al 3")
        