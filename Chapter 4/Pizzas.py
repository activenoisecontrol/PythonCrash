animals = ['snakes', 'lizards', 'turtels', 'alligators', 'the punisher']
for animal in animals:
    print (f'{animal.title()} are cold-blooded.')

print('\nAny of these animals are cold-blooded!')
print(f'The first three items in the list are: {animals[0:3]}')
print(f'Three items from the middle of the list are: {animals[1:4]}')
print(f'The last three items in the list are: {animals[-3:]}')

friend_animals = animals[:]
animals.insert(0, 'sharks')
friend_animals.append('Shrek')

print(f'	Animals: {animals}')
for animal in animals:
    print(animal.title())

print(f'	Friend animals: {friend_animals}')
for friend_animal in friend_animals:
    print(friend_animal.title())
