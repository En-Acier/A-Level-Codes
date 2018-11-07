import random

def makeGrid():
    for i in range(3):
        grid.append(["N/A","N/A","N/A",])

def easyMove():
    i = random.randint(0,2)
    j = random.randint(0,2)
    move = False
    while i <= 2 and move!= True:
        while j <= 2 and move!= True:
            if grid[i][j] == "N/A":
                grid[i][j] = "X"
                move = True
            j = j + 1
        i = i + 1
    print("I have placed a cross at",i,j)

def hardMove():
    for i in range(3):
        #Vertical check
        if grid[0][i] == grid[1][i]  and grid[0][i] != "N/A":
            grid[2][i] == "X"
            print("I have placed a cross at 3,",i+1)
        elif grid[0][i] == grid[2][i] and grid[0][i] != "N/A":
            grid[1][i] == "X"
            print("I have placed a cross at 2",i+1)
        elif grid[1][i] == grid[2][i] and grid[1][i] != "N/A":
            grid[0][i] == "X"
            print("I have placed a cross at 1,",i+1)
        #Horizontal Check
        elif grid[i][0] == grid[i][1]  and grid[i][0] != "N/A":
            grid[i][2] == "X"
            print("I have placed a cross at 3,",i+1)
        elif grid[i][0] == grid[i][2] and grid[i][0] != "N/A":
            grid[i][1] == "X"
            print("I have placed a cross at 2",i+1)
        elif grid[i][1] == grid[i][2] and grid[i][1] != "N/A":
            grid[i][0] == "X"
            print("I have placed a cross at 1,",i+1)
        #Check Diagonal
        elif grid[0][0] == grid[1][1] and grid[0][0] != "N/A":
            grid[2][2] == "X"
            print("I have placed a cross at 3,3")
        elif grid[0][0] == grid[2][2] and grid[0][0] != "N/A":
            grid[1][1] == "X"
            print("I have placed a cross at 2,2")
        elif







def playerMove():
    validI = False
    validJ = False
    while validI == False:
        i = input("Please enter the row you want to place the nought")
        try:
            i = int(i)
            if i > 3 or i < 0:
                print("That was not a valid number!")
            else:
                validI = True
        except:
            print("That was not a number!")
    i = i - 1
    while validJ == False:
        j = input("Please enter the column you want to place the nought")
        try:
            j = int(j)
            if j > 3 or j < 0:
                print("That was not a valid number!")
            else:
                validJ = True
        except:
            print("That was not a number!")
    j = j - 1
    if grid[i][j] == "N/A":
        grid[i][j] = "O"
    else:
        print("I already have an X there!")

def checkWin():
    for i in range(3):
        if grid[i][0] == "O" and grid[i][1] == "O" and grid[i][2] == "O":
            win = True
            print("You win!!")
        elif grid[0][i] == "O" and grid[1][i] == "O" and grid[2][i] == "O":
            win = True
            print("You win!!")
        elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
            win = True
            print("You win!!")
        elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
            win = True
            print("You win!!")
        else:
            win = False
        return win

def checkLoss():
    for i in range(3):
        if grid[i][0] == "X" and grid[i][1] == "X" and grid[i][2] == "X":
            loss = True
            print("You lose!!")
        elif grid[0][i] == "X" and grid[1][i] == "X" and grid[2][i] == "X":
            loss = True
            print("You lose!!")
        elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
            loss = True
            print("You lose!!")
        else:
            loss = False
        return loss

print("Let's play naughts and crosses! I'll be the crosses")
win = False
loss = False
count = 0
grid = []
makeGrid()
difficulty = ""
while difficulty.lower() != "easy" and difficulty.lower() != "hard":
    difficulty = input("Would you like easy mode or hard mode?")
for i in range(3):
    print(grid[i])

while win != True and count < 9 and loss != True:
    if difficulty.lower() == "easy":
        easyMove()
    else:
        hardMove()
    for i in range(3):
        print(grid[i])
    playerMove()
    for i in range(3):
        print(grid[i])
    count = count + 1
    win = checkWin()
    loss = checkLoss()


if count >= 9:
    print("No one can win now! There are no more squares!")