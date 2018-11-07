card = [7,4,6,8,1,5]
for j in range(6):
    nextcard = card[j]
    i = j - 1
    while i >= 0 and card[i] > nextcard:
        card[i + 1] = card[i]
        i = i - 1
    #End While
    card[i + 1] = nextcard
#End For
print(card)