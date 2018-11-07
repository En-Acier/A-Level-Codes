ciper = "GAGDCNNQPVCTIGV"
new = ""
x = -25
while x < 25:
    x = x + 1
    new = ""
    for i in range(len(ciper)):
        value = ord(ciper[i])
        value = value + x
        letter = chr(value)
        new = new + letter
    print(new)