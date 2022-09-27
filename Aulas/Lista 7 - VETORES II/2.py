n = int(input())
menor = n
maior = n
for c in range(19):
    n = int(input())
    if menor > n:
        menor = n
    elif maior < n:
        maior = n
print(menor, maior)
