num = int(input("Ingrese un número: "))

if num>1 and num < 101:
    if num%2== 0 : # num mod(modulo o resto) 2 = 0 
        print("es par")
    else:
        print("es impar")
else:
    print("El número esta fuera de rango debe estar entre 1 y 101")