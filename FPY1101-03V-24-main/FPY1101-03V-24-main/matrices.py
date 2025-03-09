matriz_Sencilla = [
    [1,2,3],
    [4,5,6]

]

for elemento in matriz_Sencilla:
    print(elemento)

print(matriz_Sencilla)

print(matriz_Sencilla[0][2])

for fila in matriz_Sencilla:
    for elemento in fila:
        print(elemento,end=" ")
print()
for i in range(2):
    for j in range(3):
        print(matriz_Sencilla[i][j])
print()
for fila in range(2):
    for columna in range(3):
        print(matriz_Sencilla[fila][columna],end=" ")
