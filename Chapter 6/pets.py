pet_0 = {'kind': 'cat', 'name': 'alisa', 'owner': 'lexa'}
pet_1 = {'kind': 'cat', 'name': 'shadow', 'owner': 'lexa krupski'}
pet_2 = {'kind': 'dog', 'name': 'buldog', 'owner': 'lexa cherniy'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    name = pet['name'].title()
    kind = pet['kind']
    owner = pet['owner'].title()
    print (f'{name} is a {kind}. It owner is {owner}.')