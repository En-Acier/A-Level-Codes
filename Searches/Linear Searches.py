lists = [2,4,8,12,77,89]
findme = 4
found = False
for i in range(len(lists)):
    if lists[i] == findme:
        found = True
        j = i + 1
        break

print(found,"at position", j)
