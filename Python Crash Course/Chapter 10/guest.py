filename = 'guest.txt'

while True:
    """Prompting while not exit"""
    guest = input("Welcome! What's your name?\n")
    
    if guest.lower() == 'exit':
        break
    else:
        with open(filename, 'w') as file_obj:
            file_obj.write(f'{guest.title()}\n')
        ask = input("Do you want to write one more guest? y/n\n")
        if ask.lower() == 'n':
            break
        elif ask.lower() == 'y':
            while True:
                """Write one more guest"""
                guest = input("What is his or her name?\n")
                with open(filename, 'a') as file_obj:
                    file_obj.write(f'{guest.title()}\n')
                ask = input("Do you want to write one more guest? y/n\n")
                if ask.lower() == 'y':
                    continue
                elif ask.lower() == 'n':
                    break
            break