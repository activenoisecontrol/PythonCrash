def album(artist, album, song_num = None):
    """Составляет словарь с информацией об альбоме"""
    albumd = {'Исполнитель': artist.title() ,'Альбом': album.title()}
    if song_num:
        albumd |= {'Количество песен': song_num}
    return albumd

print("Введите информацию об альбоме")
print("(введите 'q' в любое время для выхода)")
while True:
    ar = input("Введите исполнителя: ")
    if ar == 'q':
        break
    al = input("Введите альбом: ")
    if al == 'q':
        break
    num = input("Введите количество песен в албоме: ")
    if num == 'q':
        break
    albumd = album(ar, al, num)
    print(albumd)
