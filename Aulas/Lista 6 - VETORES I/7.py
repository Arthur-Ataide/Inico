vetor = []
impar = []
for c in range(1, 21):
    vetor.append(c)
for c in range(20):
    if vetor[c] % 2 != 0:
        impar.append(vetor[c] ** 2)
print(vetor)
print(impar)
