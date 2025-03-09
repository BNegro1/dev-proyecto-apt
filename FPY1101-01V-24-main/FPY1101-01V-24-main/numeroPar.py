num = int(input("Ingrese un número: "))

if num> 1 and num <101 :
    if num%2 == 0:
        print("Es par") 
    else:
        print("es impar")
else:
    print("El numero esta fuera de rango, debe estar entre 1 y 101")
    