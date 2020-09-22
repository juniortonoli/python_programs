print('Task List 0.01')
while True:
    print()
    print('1 - Register Task')
    print('2 - List Task')
    print('3 - Remove Task')
    print('4 - Close Program')
    option = int(input('Type the number: '))
    if option == 1:
        with open('task.txt', 'a+') as file:
            task = input('Task: ')
            file.write(f'{task} \n')
    if option == 2:
        with open('task.txt', 'r+') as file:
            print(file.read(), end='')
    if option == 3:
        cont = 0
        with open('task.txt', 'r+') as file:
            lista = file.readlines()
            for item in lista:
                print(f'{cont} - {item}', end='')
                cont = cont + 1
        deloption = int(input('Type the number of the task you want delete: '))
        with open("task.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != lista[deloption]:
                    f.write(i)
            f.truncate()
    if option == 4:
        break
