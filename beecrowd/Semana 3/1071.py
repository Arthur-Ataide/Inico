lista = []
X = int(input())
Y = int(input())

if X > Y and Y % 2 == 0:
    lista = list(range(Y + 1, X, 2))
    print(sum(lista))

elif X > Y:
    lista = list(range(Y + 2, X, 2))
    print(sum(lista))

elif X % 2 == 0:
    lista = list(range(X+1, Y, 2))
    print(sum(lista))

else:
    lista = list(range(X + 2, Y, 2))
    print(sum(lista))
