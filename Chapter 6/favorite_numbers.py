fav_num = {
    'Maksim': [5],
    'Artyom': [7, 3, 16],
    'Leha': [10, 153, 154, 2]
    }
for person, num in fav_num.items():
    if len(num) == 1:
        print(f"{person.title()}'s favorite number is:")
    else:
        print(f"{person.title()}'s favorite numbers are:")
    print(str(num).strip('[]'))