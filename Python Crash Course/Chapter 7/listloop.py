responses = {}

active_pool = True
while active_pool:

    name = input('What is your name?\n>>>')
    response = input('What is your favorite car?\n>>>') 
    responses[name.lower()] = response.lower()

    repeat = input('Would you like to let another person respond? (yes/no): ')
    if repeat == 'no':
        active_pool = False

print("\n---Pool results---")
for name, response in responses.items():
    print(f'{name.title()} likes {response.title()}')