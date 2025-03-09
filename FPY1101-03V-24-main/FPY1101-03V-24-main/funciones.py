def validar_lista_numeros():
    while True:
        try:
            numeros = input("Ingrese una lista de numeros separados por espacio: ").split()
            # que hace el split:
            # 3 4 5 ----> ['3','4','5']
            # 345 ---> ['345'] no funciona! 
            for i in range(len(numeros)):
                numeros[i] = int(numeros[i])
                #          = int(numeros[0])
                #          = int('3')
                #numeros[0]= 3 
            return numeros # ---> aca se rompe el ciclo ( no solo con break)
        except ValueError:
            print("Por favor ingrese un numero entero")

def calcularEdad(anoActual,anoNac):
    edad = anoActual - anoNac
    print("Su edad es: ",edad," app")
    
