fav_lang = {
    'jen': ['python', 'ruby'],
    'tom': ['c'],
    'aliaksei' : ['python', 'sql'],
    'leha': ['php','javascript']
}

for person, langs in fav_lang.items():
    if len(langs) > 1:
        print(f"{person.title()}'s favourite languages are:")
    else:
        print(f"{person.title()}'s favaurite language is:")
    
    for lang in langs:
        if lang != 'php' and lang != 'sql':
            print(f'\t{lang.title()}')
        else:
            print(f'\t{lang.upper()}')