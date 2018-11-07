valid = False
while valid == False:
    age = input("Please enter your age")
    try:
        age = int(age)
        valid = True
    except:
        print("That was not a number!")

print(age)

