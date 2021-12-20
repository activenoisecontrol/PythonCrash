favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
peoples = ['ken', 'sarah', 'edward', 'sasha']
for people in peoples:
    if people in favorite_languages.keys():
        print(f'{people.title()}!\n\tThank you for responding.')
    else:
        print(f'{people.title()}!\n\tPlease, take the poul.')