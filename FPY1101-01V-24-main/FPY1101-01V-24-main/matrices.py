matriz = [
    [1,2,3],
    [4,5,6]
]

print(matriz)

for elemento in matriz:
    print(elemento)

for fila in range(2):
    for columna in range(3):
        print(matriz[fila][columna])
    print()

# for i in range(2):
#     for j in range(3):
#         print(matriz[i][j])
#     print()

for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")