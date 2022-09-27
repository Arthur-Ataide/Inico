n = int(input())
sal = []
impar = (n+1)/2
media = 0
for i in range(1, n+1):
    num = float(input())
    sal.append(num)
    media += num
print(media/n)
if n % 2 != 0:
    print(sal[impar])
else:
    par = sal[(n/2)] + sal[(n/2)+1]
    print(par/2)
