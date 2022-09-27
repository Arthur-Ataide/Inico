n = int(input())
print(n)
if n > 0 and n < 1000000:
    a = n // 100
    print(f'{a} nota(s) de R$ 100,00')

    a = (n % 100) // 50
    print(f'{a} nota(s) de R$ 50,00')

    a = (n % 100) %50 // 20
    print(f'{a} nota(s) de R$ 20,00')

    a = (n % 100) %50 % 20 // 10
    print(f'{a} nota(s) de R$ 10,00')

    a = (n % 100) %50 %20 %10 // 5
    print(f'{a} nota(s) de R$ 5,00')

    a = (n % 100) %50 %20 %10 %5// 2
    print(f'{a} nota(s) de R$ 2,00')

    a = (n % 100) %50 %20 %10 %5 %2
    print(f'{a} nota(s) de R$ 1,00')
