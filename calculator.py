check = False;
number1=0
number2=1
number3=1
number4=1
while not check:
    try:
        number1 = float(input("What is your first number to input?"))
        check = True;
        break;
    except ValueError:
        print("Please enter a number")
        continue

check1 = False;
while not check1:
    try:
        number2 = float(input("What is your second number to input?"))
        check1 = True;
        break;
    except ValueError:
        print("Please enter a number")
        continue

check2 = False;
while not check2:
    try:
        number3 = int(input("Would you like to add, subtract, multiply, or divide the numbers? Enter 1 for add, 2 for subtract, 3 to multiply, or 4 to divide."))
        check2 = True;
        break;
    except ValueError:
        print("Please enter a correct integer")
        continue

if (number3) == 1:
    number4 = number1 + number2

if (number3) == 2:
    number4 = number1 - number2

if (number3) == 3:
    number4 = number1 * number2

if (number3) == 4:
    number4 = number1/number2

print("the answer is:")
print(number4)
