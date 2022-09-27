matriz = [[0 for j in range(3)] for i in range(3)]
for j in range(3):
    for i in range(3):
        matriz[i][j] = int(input(f'Digite o numero {i}, {j}: '))
for j in range(3):
    for i in range(3):
        print(f'{matriz[i][j]}', end= ' ')
    print()