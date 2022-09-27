fib = []
ant = 0
prox = 1
soma = 0
n = int(input())
for c in range(61):
    fib.append(ant)
    soma = ant + prox
    ant = prox
    prox = soma
for c in range(n):
    num = int(input())
    print(f'Fib({num}) = {fib[num]}')
