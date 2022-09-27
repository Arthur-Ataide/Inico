lista = []
M, N = map(int, input().split())
while M > 0 and N > 0:
    if M > N:
        lista = list(range(N, M + 1))

    elif N > M:
        lista = list(range(M, N + 1))

    lista2 = ' '.join(map(str, lista))
    print(f'{lista2} Sum={sum(lista)}')

    M, N = map(int, input().split())
