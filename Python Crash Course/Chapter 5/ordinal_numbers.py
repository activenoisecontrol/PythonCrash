ordinal = list(range(1,10))
for number in ordinal:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    elif number < 10:
        print(f'{number}th')