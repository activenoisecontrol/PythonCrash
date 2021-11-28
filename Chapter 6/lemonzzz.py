lemons = [
    {
    'color': 'green',
    'size': 'small',
    'age_mnth': 1
    },
     {
    'color': 'green',
    'size': 'small',
    'age_mnth': 2
    },
    {
    'color': 'green',
    'size': 'medium',
    'age_mnth': 3
    },
    {
    'color': 'green',
    'size': 'medium',
    'age_mnth': 4
    },
    {
    'color': 'yellow',
    'size': 'big',
    'age_mnth': 5
    }
    ]

lmsgs = []
lmsgm = []
lmsyb = []
for lemon in lemons:
    if lemon['age_mnth'] < 2:
        lmsgs.append(lemon)
    elif lemon['age_mnth'] <= 4:
        lmsgm.append(lemon)
    else:
        lmsyb.append(lemon)

print(f"Now you have {len(lmsgs)} small green, {len(lmsgm)} medium and {len(lmsyb)} big yellow lemons.")

lmsgs = []
lmsgm = []
lmsyb = []
for lemon in lemons:
    if lemon['age_mnth'] < 2:
        lemon['age_mnth'] = lemon['age_mnth'] + 1
        lmsgs.append(lemon)
    elif lemon['age_mnth'] < 4:
        lemon['size'] = 'medium'
        lemon['age_mnth'] = lemon['age_mnth'] + 1
        lmsgm.append(lemon)
    else:
        lemon['color'] = 'yellow'
        lemon['size'] = 'big'
        lemon['age_mnth'] = lemon['age_mnth'] + 1
        lmsyb.append(lemon)

print(f"\nAfter one mounth you will have {len(lmsgs)} small green, {len(lmsgm)} medium and {len(lmsyb)} big yellow lemons.\n")
