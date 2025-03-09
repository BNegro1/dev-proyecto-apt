'''
Crear una salida por pantalla con la siguiente información:
¿Cuál de los siguientes animales vive en el agua?
Perro
Cocodrilo
Conejo
Tiburón
Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, 
si la respuesta es Tiburón asignar +1.0 a puntaje,
 del cualquier otro caso, no asignar valor, 
 finalmente crear una salida por pantalla para mostrar 
 el puntaje obtenido.

'''
print("¿Cuál de los siguientes animales vive en el agua?\n")  # \n ---> salto línea
print("\t 1.Perro")       # \t ---> tabula
print("\t 2.Cocodrilo")
print("\t 3.Conejo")
print("\t 4.Tiburón")
resp = int(input("Ingrese opción: "))
puntaje = 0

if resp == 2:
    puntaje = puntaje + 0.5
else:
    if resp == 4:
        puntaje = puntaje + 1
    else:
        puntaje = 0

print("Su puntaje es: ",puntaje)





