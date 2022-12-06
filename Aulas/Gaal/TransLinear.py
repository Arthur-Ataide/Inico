for i in range(3):
    x = int(input())
    y = int(input())
    z = int(input())

    trans = [x, y, z]
    matriz = [0, 0, 0]

    matriz[0] = 7*y - 6*z
    matriz[1] = -x + 4*y
    matriz[2] = 2*y - 2*z

    print(trans)
    print(matriz)
