print('Input toppings those you want')
while True:
    top = input('>>>')
    if top.lower() == 'quit':
        break
    elif top == '':
        continue
    else:
        print(f"I'll add {top} to your pizza.")
        continue