A = [[0 for modalidade in range(10)]for atleta in range(10)]
for modalidade in range(10):
    for atleta in range(10):
        A[modalidade][atleta] = int(input())
cont = 0
for modalidade in range(10):
    maior = A[modalidade][0]
    for atleta in range(10):
        if maior > A[modalidade][atleta]:
            maior = A[modalidade][atleta]
        print(maior)
