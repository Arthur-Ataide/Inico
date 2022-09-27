t = []
maior = int(input())
menor = maior
t.append(maior)
media = menor
cont = 0
for i in range(120):
    n = int(input())
    media += n
    t.append(n)
    if maior < n:
        maior = n
    if menor < n:
        menor = n
for i in range(121):
    if t[i] < media:
        cont+=1
print(menor, maior, media/121, cont)
