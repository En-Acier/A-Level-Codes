valid1 = False
valid2 = False
valid3 = False
while valid1 == False:
    num1 = input("Please enter the first number")
    try:
        num1 = int(num1)
        valid1 = True
    except:
        print("That number was not valid!!")

while valid2 == False:
    num2 = input("Please enter the second number")
    try:
        num2 = int(num2)
        valid2 = True
    except:
        print("That number was not valid!!")
valid2 = False
while valid3 == False:
    choice = input("Menu... Press 1 for addition. Press 2 for multiplication. Press 3 for division")
    if choice == "1":
        ans = num1 + num2
        print(ans)
        valid3 = True
    elif choice == "2":
        ans = num1 * num2
        print(ans)
        valid3 = True
    elif choice == "3":
        ans = num1 / num2
        print(ans)
        valid3 = True
    else:
        print("You did not select a valid option!")