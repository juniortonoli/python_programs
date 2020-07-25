#draft of guessing game

word = 'perfume'
quantityword = len(word)
hideword = ['*'] * quantityword
matrixattempt = []
attempt = 0
correct = 0

print(f'The word has {quantityword} letters')
while correct < len(word):
    print(f'The word is {hideword}')
    print(f'You already wrote the following letters:: {sorted(matrixattempt)} ')
    print(f'Attempts: {attempt}')
    chute = str(input(f'Guess a letter:'))
    if chute in matrixattempt:
        print('You already wrote this letter. Type another letter.')
    else:
        matrixattempt.append(chute)
    attempt = attempt + 1
    for key, c in enumerate(word):
        if c == chute:
            print(f'Correct! The letter {chute} it is in the position {key + 1}!')
            hideword[key] = c
            correct = correct + 1
    if chute not in word:
        print(f'WRONG!!')
print(f'You guess the word {word} with {attempt} attempts')

