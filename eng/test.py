from random import choice
import json

def choose_lang(lang):
    if lang == 'eng':
        i_wo = 0
        i_tr = 1
    else:
        i_wo = 1
        i_tr = 0
    choose_word(i_wo, i_tr)

def choose_word(i_wo, i_tr):
    while True:
        chosen_word = choice(words_list)
        word = chosen_word[i_wo]
        translate = chosen_word[i_tr]
        test(word, translate)

def test(word, translate):
    print(f">>>{word}")
    user_translate = ''
    while user_translate.lower().strip() != translate:
        user_translate = input(">>>")

with open('eng/words.json', encoding='ascii') as file:
    words = json.load(file)
words_list = list(words.items())

length = len(words_list)
print(length)

lang = ''
while lang.lower().strip() != 'eng' and lang.lower().strip() != 'rus':
    print(lang)
    lang = input(f"Выберите язык (eng/rus): ")
choose_lang(lang)




