vetor = []
troca = [0 for a in range(20)]
for c in range(20):
    n = int(input())
    vetor.append(n)
    troca[19 - c] = n
for c in range(20):
    print(f'N[{c}] = {troca[c]}')
