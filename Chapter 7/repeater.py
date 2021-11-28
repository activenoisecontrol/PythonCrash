prompt = '''Welcome to repeater!
Enter ? to get help.\n>>>'''
helps = {'<Abc>': 'enter text for repeat','exit': 'end programm'}
flag = True
mess = input(prompt)
while flag:
    if mess == '?': ### Условия вывода вспомогательного списка команд
        for k, v in helps.items():  ### Из словаря helps
            print(f'{k}\t{v}')
        mess = input('>>>')
    elif mess == '':   ### Действие в случае простого нажатия клавиши Enter
        mess = input('>>>') ### Выводит приглашение на ввод и записывает вводимое значение для дальнейшего использования в программе
    elif mess.lower() == 'exit':
        flag = False
    else:
        print(mess)
        mess = input('>>>')
print('Bye!')