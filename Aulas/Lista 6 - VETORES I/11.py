lista = []
for a in range(15):
    n = int(input())
    if n >= 0:
        lista.append(n**(1/2))
    else:
        lista.append(-1)
print(lista)
