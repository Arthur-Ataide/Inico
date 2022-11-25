import heapq as hp

# deu errado

n = int(input())
A = list(map(int, input().split()))

hp._heapify_max(A)
cont = 0

while(len(A)-1 > 1):
    x = hp.heappop(A)
    y = hp.heappop(A)
    x-=1
    y-=1

    if x != 0:
        hp.heappush(A, x)
    if y != 0:  
        hp.heappush(A, y)
    
    cont+=1

print(cont)
