# Game of questions and answers made with lists.

from random import randint
# question, possible answers, position of correct answer
q = [['Quanto é 2+2?', 3, 4, 6, '2'],
     ['Quanto é 3 + 3?', 3, 4, 6, '3'],
     ['Quanto é 4 + 3?', 5, 6, 7, '3'],


]

repetead = []
while True:
    askthequestion = False
    #checking if the question already appeared
    while askthequestion == False:
        questao = randint(0, 2)
        if questao not in repetead:
            askthequestion = True
            repetead.append(questao)
            print('Passou como nao repetida')
    print(f'{q[questao][0]}')
    print(f'1: {q[questao][1]}')
    print(f'2: {q[questao][2]}')
    print(f'3: {q[questao][3]}')
    resposta = str(input(f'Digite a resposta correta para parar: '))
    #checking correct answer
    if resposta == q[questao][4]:
        print('RIGHT Answer!')
    else:
        print('WRONG Answer!')