def check(num, msg):
    while True:
        """Check the value if it's a number"""
        try:
            int(num)
        except ValueError:
            print("You can input only numbers.")
            num = input(msg)
        else:
            break
    return int(num)

msg1 = "Input first number: "
msg2 = "Input second number: "
num1 = input(msg1)
num1 = check(num1, msg1)
num2 = input(msg2)
num2 = check(num2, msg2)
ans = num1 + num2
print(f"Answer is: {ans}")
