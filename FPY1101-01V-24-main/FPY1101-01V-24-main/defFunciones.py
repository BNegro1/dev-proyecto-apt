'''
funciones sin argumentos y sin retorno 1 OK
funciones con argumentos y con retorno 4 OK
funciones con argumentos y sin retorno 2 OK
funciones sin argumentos y con retorno 3 OK

'''

#1 definir una funcion
def saludo():
    print("Hola")
#2
def saludoNombre(nombre):
    print("Hola" , nombre)

#3
def suma():
    suma = 3 + 3
    return suma
#4    
def suma2(num1,num2):
    suma = num1 + num2
    return suma

def validar_lista_numeros():
    while True:
        try:
            numeros = input("Ingrese lista de numeros separados con espacio: ").split()
            # 345 ---> ['345']
            # 3 4 5 
            # split--> numeros = ['3','4','5']
            for i in range(len(numeros)):
                numeros[i]   = int(numeros[i])
                #     ||     =   int(numeros[0])
                #     ||     =  int('3')
                #numeros[0]  = 3
            return numeros
        except ValueError:
            print("Por favor ingrese números válidos enteros")
