from random import choice
import json

def lang_page():
    """Page to choose language"""
    lang = ''
    while lang.lower().strip() != 'eng' and lang.lower().strip() != 'rus':
        lang = input(f"Выберите язык (eng/rus): ")
        if lang == 'menu':
            main_menu()
            break
        elif lang == 'exit':
            break
        elif lang == 'eng':
            i_wo = 0
            i_tr = 1
        elif lang =='rus':
            i_wo = 1
            i_tr = 0
        choose_word(i_wo, i_tr)

def choose_word(i_wo, i_tr):
    while True:
        chosen_word = choice(words_list)
        word = chosen_word[i_wo]
        translate = chosen_word[i_tr]
        exit = test(word, translate)
        if exit == 'exit':
            break
        

def test(word, translate):
    print(f">>>{word}")
    user_translate = ''
    while user_translate.lower().strip() != translate:
        user_translate = input(">>>")
        if user_translate == 'menu':
            main_menu()
            return 'exit'
        elif user_translate == 'exit':
            return 'exit'

def save():
    with open('eng/words.json','w', encoding='ascii') as file:
        json.dump(words, file)

def write_words():
    print("Input 'save' when ready")
    while True:
        new_word = input('New word in English: ').lower()
        if new_word == 'menu':
            main_menu()
            break
        elif new_word == 'exit':
            break
        elif new_word == 'save':
            save()
            continue
        elif new_word in words:
            print("It's already exists.")
            continue
        new_trans = input('Translate: ').lower()
        if new_trans == 'menu':
            main_menu()
            break
        elif new_trans == 'exit':
            break
        elif new_trans == 'save':
            save()
        else:
            words.update({new_word: new_trans})
            print(words)

def main_menu():
    print("""You can type 'menu' everywhere to jump here, or 'exit' to exit programm.\nChoose what do you want to do:
    1 = test yourself
    2 = add new words
    3 = exit""")
    while True:
        initialize = input(">>> ")
        if initialize == '3':
            pass
        elif initialize == '2':
            write_words()
        elif initialize == '1':
            lang_page()
        else:
            print("Please, input 1, 2 or 3")
            continue
        break

with open('eng/words.json', encoding='ascii') as file:
    words = json.load(file)
words_list = list(words.items())

main_menu()







