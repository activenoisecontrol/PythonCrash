aliens =[]

for alien_n in range(30):
    alien_n = {'color': 'green','speed': 'slow','points': '10'}
    aliens.append(alien_n)

for alien in aliens[::3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '15'
print(f"Color of the 4'th alien is {aliens[3]['color']}.") 
for alien in aliens[:5]:
    print(alien)