N = int(input())
ant = 0
num = 1
soma = 0
for i in range(N-1):
  print(ant, end=(' '))
  soma = ant + num
  ant = num 
  num = soma
print(ant)
