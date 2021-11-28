unconfirmed_users = []
print ('''Введите ваши ники для внесения в базу регистрации
Введите next для перехода в режим подтверждения.
Введите show для просмотра текущих никнеймов на регистрацию.
Ввдеите delete для удаления последнего добавленного никнейма.''')
while True:
    user = input('Ваш никнейм?\n>>>')
    if user.lower() == 'next':
        break
    elif user.lower() == 'show':
        print(unconfirmed_users)
    elif user.lower() == 'delete':
        unconfirmed_users.pop()
    else:
        unconfirmed_users.append(user)
confirmed_users = []
while unconfirmed_users:
    for user in unconfirmed_users:
        ask = input(f'Вы хотите зарегистрировать {user}? [y/n]: ')
        if ask.lower() == 'yes' or ask.lower() == 'y':
            print(f'{user.title()} успешно зарегистрирован.')
            confirmed_users.append(user)
        elif ask.lower() == 'no' or ask.lower() == 'n':
            print(f'{user.title()} удален.')
        else:
            ask = input('Input y (yes) or n (no)')
    del(unconfirmed_users)

print('\nСписок зарегистрированных юзеров:\n')
for cuser in confirmed_users:
    print(f'{cuser.title()}')