print('The Deli has run out of pastrami\n')
sandwich_orders = ['tuna','pastrami', 'beef','pastrami', 'pork', 'vegan', 'pastrami']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    if sandwich == 'pastrami':
        continue
    else:    
        print(f'I made your {sandwich} sandwich')
        finished_sandwiches.append(sandwich)
print('')
for sandwich in finished_sandwiches:
    print(f'Your {sandwich} sandwich is ready')
