def mk_pzz(size, *topings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in topings:
        print(f"- {topping}")