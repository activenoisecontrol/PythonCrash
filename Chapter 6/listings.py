favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print('The following languages have been mentioned:')
for lang in set(favorite_languages.values()):
    print(f'\t{lang.title()}')