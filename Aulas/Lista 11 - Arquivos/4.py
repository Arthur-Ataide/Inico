ark1 = input()
ark2 = input()
ark1 = open(ark1, 'r')
ark2 = open(ark2, 'w')
for i in ark1:
    ark2.write(i)
ark1.close()
ark2.close()
