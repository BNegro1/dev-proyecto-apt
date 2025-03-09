## ciclo para ---> for
'''
for num in range(3):
    print(num," hola")

print(num)

print("Ingrese cuantas personas compraran entradas: ")
entradas = int(input())

for i in range(entradas):
    edad = int(input(f"Ingrese su edad de la persona {i+1}:"))
'''

num = int(input("Ingrese numero de la tabla: "))
for i in range(1,11):
    #print( i,"x",num,"=",num*i)
    print(f"{i}x{num}={num*i}") # {}---> van las variables o formulas

## ciclo Mientras ---> while
conta = 0
while conta < 3:
    conta = conta + 1
    print("hola")
print()
## tabla multiplicar con while
print("TABLA MULTIPLICAR CON WHILE")
num = int(input("Ingrese numero a multiplicar: "))
conta = 0
while conta < 10:
    conta = conta + 1 
    #print(f"{conta}x{num}={conta*num}")
    print(conta,"x",num,"=",conta*num)

## repetir ---> While True
'''cont = 0
while True:
    
    cont = cont + 1
    print(cont)
    #break
'''
while True:
    try:
        print("  MENU   ")
        print("*********")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Salir")
        opc = int(input("Ingrese opción"))
        if opc >0 and opc < 4:
            if opc == 1:
                print("haga la opción 1")
            else:
                if opc == 2:
                    print("haga la opción 2")
                else:
                    if opc == 3:
                        break
        else:
            print("La opcion debe estar entre 1 y 3")
    except:
        print("Debe ser numero la opcion a elegir")


