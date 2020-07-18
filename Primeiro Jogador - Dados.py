#The first version of a dice game that defines who is the first player.
#I feel there is much to improve, but is already working =]
#Later I will add the feature that only players that tie roll the dice again.

from random import randint
from operator import itemgetter

lista = []
listadesempate = []
player = []
desempate = 0
rerolagem = 0
qplayers = int(input(f'Quantidade de jogadores: '))
for d in range(qplayers):
    nome = str(input(f'Nome do jogador {d + 1}: '))
    dados = randint(1, 3)
    player.append(nome)
    dados = str(dados)
    player.append(dados)
    listadesempate.append(dados)
    lista.append(player[:])
    player.clear()
for i in range(1, 4):
    repetido = listadesempate.count(str(i))
    if repetido > 1:
        desempate += 1
while True:
    listadesempate.clear()
    desempate = 0
    rerolagem += 1
    print(f'Rerolagem {rerolagem}')
    for c in range(qplayers):
        lista[c][1] = str(randint(1, 3))
        listadesempate.append(lista[c][1])
    for i in range(1, 4):
        repetido = listadesempate.count(str(i))
        if repetido > 1:
            desempate += 1
    if desempate == 0:
        break
print('Bora la pro ranking')
ranking = sorted(lista, key=itemgetter(1), reverse=True)
for c in range(qplayers):
    print(f'{ranking[c][0]} tirou {ranking[c][1]}')
# The first version of a dice game that defines who is the first player.
# I feel there is much to improve, but is already working =]
# Later I will add the feature that only players that tie roll the dice again.

from random import randint
from operator import itemgetter

lista = []
listadesempate = []
player = []
desempate = 0
rerolagem = 0
qplayers = int(input(f'Quantidade de jogadores: '))
for d in range(qplayers):
    nome = str(input(f'Nome do jogador {d + 1}: '))
    dados = randint(1, 3)
    player.append(nome)
    dados = str(dados)
    player.append(dados)
    listadesempate.append(dados)
    lista.append(player[:])
    player.clear()
for i in range(1, 4):
    repetido = listadesempate.count(str(i))
    if repetido > 1:
        desempate += 1
while True:
    listadesempate.clear()
    desempate = 0
    rerolagem += 1
    print(f'Rerolagem {rerolagem}')
    for c in range(qplayers):
        lista[c][1] = str(randint(1, 3))
        listadesempate.append(lista[c][1])
    for i in range(1, 4):
        repetido = listadesempate.count(str(i))
        if repetido > 1:
            desempate += 1
    if desempate == 0:
        break
print('Bora la pro ranking')
ranking = sorted(lista, key=itemgetter(1), reverse=True)
for c in range(qplayers):
    print(f'{ranking[c][0]} tirou {ranking[c][1]}')

# original version without roll the dice again

# from random import randint
# from operator import itemgetter
#
# lista = []
# player = []
# qplayers = int(input(f'Quantidade de jogadores: '))
# for d in range(qplayers):
#     nome = str(input(f'Nome do jogador {d + 1}: '))
#     dados = randint(1, 2)
#     player.append(nome)
#     dados = str(dados)
#     player.append(dados)
#     lista.append(player[:])
#     player.clear()
# print('Bora la pro ranking')
# ranking = sorted(lista, key=itemgetter(1), reverse=True)
# for c in range(qplayers):
#     print(f'{ranking[c][0]} tirou {ranking[c][1]}')
