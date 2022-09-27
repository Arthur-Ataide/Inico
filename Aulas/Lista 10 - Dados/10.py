DNA = input('Coloque a fita 1: ')
fita1 = []
fita2 = []
print(DNA)
for i in DNA:
    fita1.append(i)
for i in range(len(DNA)):
    if fita1[i] == 'A':
        fita2.append('T')
    elif fita1[i] == 'C':
        fita2.append('G')
    elif fita1[i] == 'G':
        fita2.append('C')
    elif fita1[i] == 'T':
        fita2.append('A')
    print(fita2[i], end='')
