num1 = int(input("Ingrese un número para sumar: "))
num2 = int(input("Ingrese otro número para sumar: "))

if num1 >0:
    if num2 >0:
        suma  = num1 + num2
        print("La suma es : ",suma)
    else:
        print("Los numeros deben ser positivos")
else:
    print("El num1 debe ser positivo")


