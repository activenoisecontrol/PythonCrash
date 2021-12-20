
print("Give me two numbers, and i'll devide them.")
print("Enter 'q' to quit.")

def check(value, msg):
    """Является ли значения числом"""
    while True:
        try: 
            float(value)
        except ValueError:
            """Если появляется такая ошибка, значит введено не число. Запрашиваем новое значение, пока не будет введено число."""
            print("You need to use only numbers!")
            value = input(f"{msg}: ")
            if value == 'q':
                """Если вводится 'q', то записываем в value, и возвращаем программе, цикл прерывается."""
                break
        else:
            """Если изначально было введено число, цикл прерывается, а число возвращается обратно программе."""
            break
    return value
        
while True:
    msg1 = "First number: "
    msg2 = "Second number: "

    first_number = input(f"\n{msg1}")
    if first_number == 'q':             ###Проверяем до функции 
        break
    first_number = check(first_number, msg1)
    if first_number == 'q':                 ###Если q было введено в процессе проверки значения на ее числовой характер
        break

    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    second_number = check(second_number, msg2)
    if second_number == 'q':
        break
    try:                        ###Когда введены 2 числа, пробуем поделить одно на другое
        answer = float(first_number)/float(second_number)
    except ZeroDivisionError:     ###Если делили на 0, то выдаем сообщение
        print("You can't divide by zero!")    
    else:       ###Если все норм, выдаем ответ
        print(answer)