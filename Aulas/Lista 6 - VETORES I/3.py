vetor = []
troca = [0 for a in range(1, 11)]
for c in range(1, 11):
    n = int(input('Digite um numero: '))
    vetor.append(n)
    troca[10 - c] = n
print(vetor)
print(troca)
