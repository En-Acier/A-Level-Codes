def binarysearch(findme,numbers,found):
    tries = 1
    bottom = 0
    top = len(numbers) + 1
    while found == False and bottom <= top:
        mid = (bottom + top) // 2
        if (numbers[mid]==findme):
            found = True
        elif (numbers[mid]<findme):
            bottom = mid+1
            tries = tries + 1
        else:
            top = mid-1
            tries = tries + 1

    print(found,"after",tries,"tries")


numbers = [2,5,7,12,14,21,28,31,36]
findme = 7
found = False
tries= (binarysearch(findme,numbers,found))


