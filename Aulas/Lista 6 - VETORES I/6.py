vetor = []
n = int(input(' '))
for c in range(n):
    num = int(input(' '))
    if num % 2 == 0:
        vetor.append(num)
print(sum(vetor))
