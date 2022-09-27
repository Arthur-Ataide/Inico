vetor = [0 for a in range(100)]
for c in range(100):
    n = float(input())
    if n > 10:
        vetor[c] = n
    else:
        vetor[c] = n
        print(f'A{[c]} = {vetor[c]:.1f}')
