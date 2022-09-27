vetor = []
cont = 0
n = int(input())
for i in range(n):
    vetor.append(int(input()))
while True:
    for i in range(n):
        quant = 0
        if vetor[cont] == vetor[i]:
            quant += 1
            if quant != 1:
                del vetor[i]
    cont += 1

