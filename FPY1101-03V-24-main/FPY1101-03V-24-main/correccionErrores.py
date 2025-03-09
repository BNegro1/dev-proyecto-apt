
'''
try:
    bloque de codigo a correr
except:
    haga algo si se cae.
else:
    si todo esta bien
finally:
    de cualquier forma se ejecuta esta seccion


while True:
    try:
        num = int(input("Ingrese un número: "))
        #break
    except ValueError:
        print("Solo ingrese números!")
    else:
        print("Todo bien!")
        break
    finally:
        print("Que tenga un buen dia!")

'''
try:
    div = 10/0
except :
    print("Error")