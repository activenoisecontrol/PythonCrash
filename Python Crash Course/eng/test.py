import os
from random import choice
import json

def lang_page(words_list):
    """Page to choose language"""
    lang = ''
    while lang != 'eng' and lang != 'rus' and lang != 'menu' and lang != 'exit':
        lang = input(f"Выберите язык (eng/rus): ").lower().strip()
    if lang == 'menu':
        main_menu()
        return
    elif lang == 'exit':
        return
    elif lang == 'eng' or lang == 'rus':
        if lang == 'eng':
            i_wo = 0
            i_tr = 1
        elif lang =='rus':
            i_wo = 1
            i_tr = 0
        choose_word(i_wo, i_tr, words_list)

def choose_word(i_wo, i_tr, words_list):
    """Choose random word from a list."""
    answered = []
    while True:
        if len(answered) == len(words_list):
            print("Cool! You're done.")
            ack = ''
            while ack != 'yes' and ack != 'no':
                ack = input("Do you wanna test again? (yes/no)\n> ").lower().strip()
            if ack == 'yes':
                answered = []
                continue
            break
        chosen_word = choice(words_list)
        word = chosen_word[i_wo]
        if word in answered:
            continue
        answered.append(word)
        translate = chosen_word[i_tr]
        exit = test(word, translate)
        if exit == 'exit':
            break
        else:
            print("You're right!")

def test(word, translate):
    """Compare user's input with translate value."""
    print(f">>> {word}")
    user_translate = ''
    while user_translate != translate:
        user_translate = input(">>> ").lower().strip()
        if user_translate == 'menu':
            main_menu()
            return 'exit'
        elif user_translate == 'exit':
            return 'exit'
        elif user_translate != translate:
            print("You're wrong. Input again")

def save(words):
    """Save words in file."""
    print("Saving...")
    with open('words.json','w', encoding='ascii') as file:
        json.dump(words, file)
    print("Done!")    
    return 

def write_words(words):
    """Input new words."""
    print("Input 'save' when ready")
    while True:
        new_word = input('New word in English: ').lower().strip()
        if new_word == 'menu':
            main_menu()
            break
        elif new_word == 'exit':
            break
        elif new_word == 'save':
            save(words)
            continue
        elif new_word in words:
            print("It's already exists.")
            continue
        new_trans = input('Translate: ').lower().strip()
        if new_trans == 'menu':
            main_menu()
            break
        elif new_trans == 'exit':
            break
        elif new_trans == 'save':
            save(words)
        else:
            words.update({new_word: new_trans})

def main_menu():
    """Main menu."""
    with open('words.json', encoding='ascii') as file:
        words = json.load(file)
    words_list = list(words.items())
    print("""You can type 'menu' everywhere to jump here, or 'exit' to exit programm.\nChoose what do you want to do:
    1 = test yourself
    2 = add new words
    3 = exit""")
    while True:
        initialize = input(">>> ")
        if initialize == '3':
            pass
        elif initialize == '2':
            write_words(words)
        elif initialize == '1':
            lang_page(words_list)
        else:
            print("Please, input 1, 2 or 3")
            continue
        break

def newbee():
    words = {}
    print("Seems you're new here! Input some words to save.")
    print("Input 'save' when ready")
    while True:
        new_word = input('New word in English: ').lower()
        if new_word == 'menu':
            try:
                with open('words.json', encoding='ascii') as file:
                    words = json.load(file)
                main_menu()
                break
            except FileNotFoundError:
                print("First you need to save something.")
                continue
        elif new_word == 'exit':
            break
        elif new_word == 'save':
            if words != {}:
                save(words)
                continue
            else:
                print("First you need to input something.")
                continue
        elif new_word in words:
            print("It's already exists.")
            continue
        new_trans = input('Translate: ').lower()
        if new_trans == 'menu':
            try:
                with open('words.json', encoding='ascii') as file:
                    words = json.load(file)
                main_menu()
                break
            except FileNotFoundError:
                print("First you need to save something.")
                continue
        elif new_trans == 'exit':
            break
        elif new_trans == 'save':
            if words != {}:
                save(words)
            else:
                print("First you need to input something.")
                continue
        else:
            words.update({new_word: new_trans})

if __name__ == '__main__':

    dirname = os.path.dirname(__file__)
    os.chdir(dirname)

    try:
        with open('words.json', encoding='ascii') as file:
            main_menu()
    except FileNotFoundError:
        newbee()