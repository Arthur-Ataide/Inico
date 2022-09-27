D = int(input(' '))  ### diaria no dia 1
A = int(input(' '))   ###dia 2 ate o 15
cont = 0
N = int(input(' ')) ###dia de chegada
if 2 <= N <= 15:
    soma = (31 - N + 1)*(D + (N-1) * A)
elif N == 1:
    soma = 31 * D
else:
    soma = (31 - N + 1) * (D + (15 - 1) * A)
print(soma)
