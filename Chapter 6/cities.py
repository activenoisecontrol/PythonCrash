cities = {
    'минск': {
        'country': 'беларусь',
        'popultation': '2 миллиона',
        'fact': 'город - герой'
        },
    'киев':
        {
        'country': "украина",
        'popultation': "3 миллиона",
        'fact': "леха живет там"
        },
    'людиново':
        {
        'country': "россия",
        'popultation': "41 тыща",
        'fact': "андрюха живет там"
        }
    }
for city, facts in cities.items():
    print(f"Город {city.title()}. Несколько фактов о нем:")
    for fact, value in facts.items():
        print(f"\t{fact.title()}: {value.title()}")