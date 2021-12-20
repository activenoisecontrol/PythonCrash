major_rivers = {'amazonas': 'brazil', 'nile': 'egypt', 'mississippi': 'us'}
for river, country in major_rivers.items():
    if country == 'us':
        country = country.upper()
    else:
        country = country.title()
    print(f'The {river.title()} runs through {country}')

print('\nList of countries:')
for river in major_rivers.keys():
    print(f'\t{river.title()}')

print('\nList of rivers:')
for country in major_rivers.values():
    print(f'\t{country.upper() if country == "us" else country.title()}')
    