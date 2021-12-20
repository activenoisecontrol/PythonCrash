peplos = []

pepel_0 = {'name': 'doge', 'lastname': 'boge', 'age': 10, 'from': 'george'}
pepel_1 = {'name': 'vasia', 'lastname': 'basia', 'age': 53, 'from': 'belarasia'}
pepel_2 = {'name': 'usia', 'lastname': 'dusia', 'age': 154, 'from': 'rusia'}

peplos.append(pepel_0)
peplos.append(pepel_1)
peplos.append(pepel_2)

for pepel in peplos:
    name = pepel['name'].title()
    lname = pepel['lastname'].title()
    age = pepel['age']
    live = pepel['from'].title()
    print(f"{name} {lname} is {age} years old. He is from {live}.")