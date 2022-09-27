vetor = []
for i in range(15):
    n = int(input(' '))
    vetor.append(n)
for i in range(15):
    cont_p = 0
    for j in range(1, vetor[i]+1):
        if vetor[i] % j == 0:
            cont_p += 1
    if cont_p == 2:
        print(f'O elemento da posiçao {i} é primo e seu valor é {vetor[i]}')
