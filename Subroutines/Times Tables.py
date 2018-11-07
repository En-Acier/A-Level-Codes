def multiples(table,startnum,endnum,pupilName):
    print("Hi",pupilName,"here is your times table")
    while startnum <= endnum:
        answer = startnum * table
        print(table,"x",startnum,"=",answer)
        startnum = startnum + 1

pupilName = input("What is your name?")
table = int(input("Please enter the times table"))
startnum = int(input("What is the starting number?"))
endnum = int(input("What is the end number?"))
multiples(table,startnum,endnum,pupilName)
