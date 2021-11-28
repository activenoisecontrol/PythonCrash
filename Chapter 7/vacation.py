active = True
results = {}
while active:
    name = input('What is your name?\n>>>')
    place = input('What is the most desired place in the world that you want to visit?\n>>>')
    results[name] = place

    ask = input('Would you let to answer anyone else? (yes/no) ')
    if ask.lower() == 'no':
        active = False

for name, place in results.items():
    print(f'{name.title()} wish to visit {place.title()}')