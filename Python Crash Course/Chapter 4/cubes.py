cubes = []
for value in range (1, 11):
	cube = value**3
	cubes.append(cube)
	print(cube)
reverse = sorted(cubes, reverse = True)
print(f'\nReversed list of cubes: {reverse}')
print('\nTop 3 cubes are:')
for cube in reverse[:3]:
	print(cube)
top3 = [cube for cube in reverse[:3]]
top3.append('lol')
print(cubes)
print(reverse)
print(top3)