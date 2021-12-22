import random

MAX_GUESSES = 10
MAX_DIGITS = 1

def main():
    print(f'''
I am thinking of a {MAX_DIGITS}-digit number.

    Here are some clues:

When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.

You have {MAX_GUESSES} to get it.
''')

    while True:
        number = getNum()
        guess = 1
        while guess <= MAX_GUESSES:
            print(f"Guess #{guess}")
            user_number = ''
            while len(user_number) != MAX_DIGITS or not user_number.isdecimal():
                user_number = input("> ")

            if number == user_number:
                print("Yes! You're right!")
                break
            clues = getClues(number, user_number)
            print(clues)
            guess += 1
            if guess > MAX_GUESSES:
                print(f"You ran out of guesses. The number was {number}!")
        answer = ''
        while answer != 'yes' and answer != 'no':
            answer = input("Do you want to play again? (yes/no)\n> ").lower().strip()
        if answer == 'no':
            break


def getNum():
    if MAX_DIGITS == 1:
        number = random.choice(range(0, 10))
    else:
        start_num = int('1' + (MAX_DIGITS - 1)*'0')
        end_num = int('1' + MAX_DIGITS * '0')
        number = random.choice(range(start_num, end_num))
    return str(number)

def getClues(number, user_number):
    clues = []
    for i in range(MAX_DIGITS):
        if user_number[i] == number[i]:
            clue = 'Fermi'
            clues.append(clue)
        elif user_number[i] in number:
            clue = 'Pico'
            clues.append(clue)
    if len(clues) == 0:
        return 'Bagels'
    else:
        return ','.join(clues)

if __name__ == '__main__':
    main()