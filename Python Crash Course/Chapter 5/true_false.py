pizza = 'peperoni'
print('Is pizza == bbq? I predict False')
print(pizza == 'bbq')
print('Is pizza == peperoni? I predict True')
print(pizza == 'peperoni')
print('Is pizza == chiken? I predict False')
print(pizza == 'chiken')
print('Is pizza != bbq? I predict True')
print(pizza != 'bbq')
print('Is pizza != peperoni? I predict False')
print(pizza != 'peperoni')
print('Is pep in pizza? I predict True')
print('pep' in pizza)
print('Is name of "pizza" longer or equal to the bbq? I predict True')
print(pizza >= 'bbq')
print('Is name of "pizza" shorter or equal to the chiken? I predict False')
print(pizza <= 'chiken')

print('\nIs 53 >= 100? I predict False')
print(53 >= 100)
print('Is 100 <= 100? I predict True')
print(100 <= 100)
print('Is 153 == 153? I predict True')
print(153 == 153)
print('Is 100 != 100? I predict False')
print(100 != 100)
print('Is 100 <= 100 and 100 < 53? I predict False')
print(100 <= 100 and 100 < 53)
print('Is 100 <= 100 or 100 < 53? I predict True')
print(100 <= 100 or 100 < 53)

groups = ['Sabbaton', 'AC/DC', 'Mettalica', 'Scorpions', 'Disturbed', 'Rammstein']
group1 = 'sabbaton'
group2 = 'prodigy'
print('Is group1 in groups? I predict True')
print(group1.title() in groups)
print('Is group2 not in groups? I predict True')
print(group2.title() not in groups)