cont = 0
media = 0
while True:
    try:
        nome = str(input())
        dist = float(input())
        cont += 1
        media += dist
    except:
        break
print(f'{(media/cont):.1f}')
