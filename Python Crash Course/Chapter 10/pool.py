from pool_module import erase, pool

filename = 'color_pool.txt'
pool_quest = "What is your favorite color?"
while True:
    ask_erase = input("Do you want to clear file before use? y/n\n")
    if ask_erase == 'y':
        erase(filename)
        pool(filename, pool_quest)
        break
    else:
        pool(filename, pool_quest)
        break