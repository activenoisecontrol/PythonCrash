def build_profile(first, last, **description):
    description['first name'] = first
    description['last name'] = last
    return description

my_description = build_profile('aliaksei', 'partnou', age = 18, born = 'belarus')
print(my_description)