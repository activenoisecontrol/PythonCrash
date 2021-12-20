def cicof(city, country):
    cc = f'{city.title()}, {country.title()}'
    return cc

cicod = {}

while len(cicod) < 3:
    ci = input("Введите город: ")
    if ci == 'q':
        break
    co = input("Введите страну: ")
    if co == 'q':
        break
    cicod[ci] = co

for city, country in cicod.items():
    cicov = cicof(city, country)
    print(cicov)
