Xi = [] # Valores da mediçao
N = int(input()) # numero de mediçoes
S = int(input()) # soma desejada
cont = 0
posicao = 0
soma = 0
for c in range(N):
    Xi.append(int(input()))
while posicao != N+1:
    for c in range(N - posicao):
        print(posicao)
print(posicao)


