vetor = [0 for a in range(10)]
n = int(input())
for c in range(10):
    vetor[c] = (2 ** c) * n
    print(f'N[{c}] = {vetor[c]}')
