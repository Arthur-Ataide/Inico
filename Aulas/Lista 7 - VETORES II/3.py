vetor = []
n = int(input())
vetor.append(n)
maior = n
menor = n
for c in range(14):
    n = int(input())
    vetor.append(n)
    if menor > n:
        menor = n
    elif maior < n:
        maior = n
for c in range(15):
    if vetor[c] == maior:
        print(f'O maior valor é {maior} na posiçao {c}')
    if vetor[c] == menor:
        print(f'O maior valor é {menor} na posiçao {c}')



