arreglo3D = [
    [
        [1,2,3],
        [4,5,6],
    ],
    [
        [7,8,9],
        [10,11,12]
    ],
    [
        [13,14,15],
        [16,17,18]
    ]

]

print(arreglo3D[1][1][2])

for capa in arreglo3D:
    for fila in capa:
        for elemento in fila:
            print(elemento, end = " ")
        print()
    print()

