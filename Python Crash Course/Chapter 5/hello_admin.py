logins = []
if logins:
    for login in logins:
        if login == 'admin':
            print(f'Hello {login.upper()}! Do you want to see last report?')
        else:
            print(f'Hello {login.title()}! Welcome back!')
else:
    print('We need to find some users!')