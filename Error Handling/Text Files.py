valid = False
while valid == False:
    file = input("Would you like to open the boys file or the girls file?")
    if file == "boys":
        text_file = open("boys.txt", "r")
        valid = True
    elif file == "girls":
        text_file = open("girls.txt," "r")
        valid = True
    else:
        print("That wasn't a valid input!")
x = text_file.readline()
while x != "":
    print(x)
    x = text_file.readline()

