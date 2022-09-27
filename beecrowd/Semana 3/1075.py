N = int(input())
if N < 10000:
    for a in range(1, 10000):
        if a % N == 2:
            print(a)
