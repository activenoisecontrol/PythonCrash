def make_car(manufacturer, model, **other_info):
    other_info['manufacturer'] = manufacturer
    other_info['model'] = model
    return other_info
car = make_car('subaru', 'outback', color = 'black', price = '36000$', buy = True)
print(car)