vetor = [0 for a in range(10)]
for c in range(10):
    n = int(input(' '))
    if n > 0:
        vetor[c] = n
    else:
        vetor[c] = 1
    print(f'X[{c}] = {vetor[c]}')
