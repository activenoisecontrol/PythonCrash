filename = 'guest.txt'

while True:
    """Prompting while not exit"""
    print("This program writes names in a guest book.")
    print("You can write 'exit' to exit from program.")
    guest = input("Welcome! What's your name?\n")
    
    if guest.lower() == 'exit':
        break
    else:
        print(f"Welcome {guest.title()}! You have been added to the list!")
        with open(filename, 'w') as file_obj:
            file_obj.write(f'{guest.title()}\n')
        ask = input("Do you want to write one more guest? y/n\n")
        if ask.lower() == 'n':
            break
        elif ask.lower() == 'y':
            while True:
                """Write one more guest"""
                guest = input("What is your name?\n")
                if guest.lower() == "exit":
                    break
                else:
                    print(f"Welcome {guest.title()}! You have been added to the list!")
                    with open(filename, 'a') as file_obj:
                        file_obj.write(f'{guest.title()}\n')
                    ask = input("Do you want to write one more guest? y/n\n")
                    if ask.lower() == 'y':
                        continue
                    elif ask.lower() == 'n':
                        break
            break