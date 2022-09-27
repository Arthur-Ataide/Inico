N = int(input(' ')) ##menor
M = int(input(' ')) ##maior
S = int(input(' ')) ##soma das casas
for I in range(M, N-2, -1):
    I = str(I)
    soma = sum(int(i) for i in I)
    if int(I) < N:
        print(-1)
    elif soma == S:
        print(I)
        break
