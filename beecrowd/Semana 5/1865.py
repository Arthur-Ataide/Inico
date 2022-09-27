n = int(input())
cont = 0
while cont < n:
    nome, forca = map(str, input().split())
    if nome == 'Thor':
        print('Y')
    else:
        print('N')
    cont += 1
