deuda = 100000
saldo = 100000

while True:
    try:
        print("     MENU     ")
        print("**************")
        print("1. Pago tarjeta de crédito")
        print("2. Simulación de compras")
        print("3. Salir")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            print("PAGA")
            while True:
                try:
                    print("Su saldo es: $",saldo)
                    print("Su deuda es: $",deuda)
                    montoPago = int(input("Ingrese el monto a pagar: "))
                    if montoPago < 0 :
                        print("El monto debe ser mayor a cero")
                    else:
                        if montoPago > deuda :
                            print("Pago excede deuda")
                        else:
                            deuda = deuda - montoPago # deuda -= montoPago
                            print("Ud pago: $",montoPago)
                            saldo = saldo + montoPago # saldo += montoPago
                            break # cuando funcionan las cosas
                except:
                    print("Ingrese el monto valido a pagar")
        else:
            if opcion == 2:
                print("COMPRA")
                cantidadCompra= int(input("Ingrese cantidad de compras: "))
                for i in range(cantidadCompra):
                    print("Compra ",(i+1))
                    try:
                        montoCompra = int(input("Ingrese monto de compra: "))
                        if montoCompra <= 0 :
                            print("El monto de compra debe ser mayor a cero")
                        else:
                            if saldo >= montoCompra:
                                deuda = deuda + montoCompra
                                saldo = saldo - montoCompra
                                print("Ud compro un monto de $",montoCompra)
                            else:
                                print("Saldo insuficiente")
                    except ValueError:
                        print("Dene ingresar un valor numerico para comprar")
                    

            else:
                if opcion == 3:
                    print("Saliendo...")
                    break

    except:
        print("Ingrese una opcion válida del 1 al 3")
