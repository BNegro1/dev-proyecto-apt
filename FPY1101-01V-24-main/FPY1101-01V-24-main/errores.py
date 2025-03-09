'''
try:
    bloque de codigo
except:
    se maneja el error
else:
    que no pasa nada
finally:
    este bloque siempre se ejecuta 
'''
while True:
    try:
        num = int(input("Ingrese un numero: "))
        #break
    except:
        print("Solo numeros debes ingresar")
    else:
        print("Estamos bien!")
        break
    finally:
        print("Que tenga un buen dia")
'''
div = 10/0
print(div)
'''