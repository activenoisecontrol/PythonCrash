def sandwiches(*ingridients):
    """Creates sandwich entry with chosen ingridients"""
    print("Building a sandwich with ingredients listed below:")
    for ingr in ingridients:
        print(f'-{ingr.title()}')

sandwiches('chees')
sandwiches('chees','sauce')
sandwiches('chess','sauce','pikle','beacon')