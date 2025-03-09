##calcular edad
print("Calculo de edad")
añoActual = int(input("Ingrese año Actual: "))
añoNac = int(input("Ingrese año Nacimiento: "))
edad = añoActual - añoNac
print("Su edad es: ",edad," app")

## condiciones ---> SI ----> IF

# condiciones anidadas

if edad >= 18:
    print("UD es mayor de edad")
else:
    if edad >0 and edad <= 4:
        print("ud es un bebe")
    else:
        if edad >4 and edad <12:
            print("UD es un niño(a)")
        else:
            if edad >= 13 and edad < 18:
                print("ud es una adolescente")