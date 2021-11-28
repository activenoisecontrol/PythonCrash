
def formatted_city_info(city, country, population = ''):
    """Return neatly formatted city info"""
    if population:
        city_info = f"{city}, {country}".title() + f" - population {population}"
    else:
        city_info = f"{city}, {country}".title()
    return city_info

