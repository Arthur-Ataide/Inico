vetor = []
ordem = []
for c in range(15):
    vetor.append(int(input(' ')))
for c in range(15):
    if c == 0:
        ordem.append(vetor[0])
    elif vetor[c] not in ordem:
        if vetor[c] > ordem[c-1]:
            ordem.append(vetor[c])
        elif vetor[c] < ordem[0]:
            ordem.insert(0, vetor[c])
        else:
            while vetor[c] not in ordem:
                for b in range(15):
                    if ordem[b] < vetor[c] < ordem[b+1]:
                        ordem.insert(b+1, vetor[c])
                        break
    else:
        for b in range(c):
            if vetor[c] == ordem[b]:
                ordem.insert(b, vetor[c])
                break
print(ordem)
