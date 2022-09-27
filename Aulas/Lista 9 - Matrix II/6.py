Matrix = [[0 for j in range(50)] for i in range(3)]
comprar = []
for i in range(50):
    for j in range(3):
        if j == 0:
            Matrix[i][j] = str(input('Qual o nome? '))
        elif j == 1:
            Matrix[i][j] = int(input('Qual o estoque ideal? '))
        else:
            Matrix[i][j] = int(input('Qual a quantidade? '))
for i in range(50):
    comprar.append(Matrix[i][1] - Matrix[i][2])
    if comprar[i] < 0:
        comprar[i] = 0
print(comprar)



