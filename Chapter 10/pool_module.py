def erase(filename):
    with open(filename, 'w') as file_object:
        file_object.write('')

def pool(filename, pool_quest):
    print("Type 'exit' to exit")
    while True:
        ask = input(f"{pool_quest}\n")
        if ask.lower() == 'exit':
            break
        else:
            with open(filename, 'a') as file_object:
                file_object.write(f'{ask}\n')