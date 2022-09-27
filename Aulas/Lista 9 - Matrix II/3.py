Matrix = [[0 for i in range(10)] for j in range(10)]
prod = 1
for i in range(10):
    for j in range(10):
        Matrix[i][j] = int(input())
for i in range(10):
    for j in range(10):
        if j < i:
            prod *= Matrix[i][j]
print(prod)
