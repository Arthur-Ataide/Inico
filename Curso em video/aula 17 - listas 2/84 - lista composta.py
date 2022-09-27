perfil = []
todos = []
cont = 'S'
pessoas = 0
maior = 0
menor = 0
while cont == 'S':
    nome = input('Qual o nome? ')
    peso = float(input('Qual o peso? '))
    if len(todos) == 0:
        maior = peso
        menor = peso
    elif maior < peso:
        maior = peso
    elif menor > peso:
        menor = peso
    perfil.append(nome)
    perfil.append(peso)
    todos.append(perfil[:])
    perfil.clear()
    cont = input('Vai continuar? ')
print(len(todos))
print(todos)
print(maior)
for p in todos:
    if p[1] == maior:
        print(p[0])
print(menor)
for p in todos:
    if p[1] == menor:
        print(p[0])
