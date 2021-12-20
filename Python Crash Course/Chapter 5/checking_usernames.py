current_users = ['artyom227', 'maksim123', 'admin', 'leha228', 'egor1337']
new_users = ['new_uSeR1337', 'Maksim123', 'leha228', 'rita291']
for user in new_users:
    if user.lower() in current_users:
        print(f'Username {user} is taken by someone else. Choose another name')
    else:
        print(f'Username {user} is available and now it\'s yours')