vetor = []
for c in range(5):
    num = int(input(' '))
    vetor.append(num)
n = int(input(' '))
if vetor.__contains__(n) == True:
    print(vetor.index(n))
else:
    print('Erro')
