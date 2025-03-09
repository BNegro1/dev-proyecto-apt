# condiciones anidadas
# calcular edad

añoActual = int (input("Ingrese año actual: "))
añoNac = int(input("Ingrese año de nacimiento: "))

edad = añoActual - añoNac

print("Ud tiene ",edad," años app")

if edad >= 18:
    print("Ud es mayor de edad")
else:
    if edad > 0 and edad <= 4:
        print("ud es un bebé")
    else:
        if edad > 4 and edad <= 13:
            print("ud es un niño")
        else:
            if edad >13 and edad <18:
                print("ud es un adolescente")


'''
Tipo de datos: 
    int --> integer ---> entero
    float --> real o decimales
    str ---> string o caracteres o input()
    valor = True
    valor = False ---> logicos ---> boolean 

operaciones:
    + --> suma
    - --> resta
    / --> division
    * --> mutliplicacion

operadores logicos:
    < menor
    > mayor
    <= menor o igual
    >= mayor igual
    == igual
    = asignacion
    != distinto


'''

