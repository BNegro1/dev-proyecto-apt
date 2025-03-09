correo = input("Ingrese correo: ")

## con if
print(" CON IF ")
print("********")
if "@" in correo: #juan@gmail.com
    print("Correo válido")
print()
## con for
print(" CON FOR ")
print("********")
for caracter in correo:
    if caracter == "@":
        print("Correo válido")
        break
print()

## con while --> spoiler 3 unidad
contador = 0
while contador < len(correo):
    if correo[contador] == "@":   # --->  h o l a
         print("Correo válido")   # --->  0 1 2 3  --> contador
         break
    contador = contador + 1

#comienza con 9
telefono = input("Ingrese telefono: ")
telefono.startswith("9")
telefono.endswith("8")
# que tenga nueve numeros
len(telefono) <= 9
hola = input("Saludo: ")
palabraMayuscula = hola.upper()
print(palabraMayuscula)
palabraMiniscula = hola.lower()
print(palabraMiniscula)