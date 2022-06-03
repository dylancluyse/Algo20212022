import math

def nieuw_kaartspel(arrKleuren, arrWaarden):
    
    arr = []

    for kleur in arrKleuren:
        for waarde in arrWaarden:
            arr.append(kleur + waarde)

    return arr


def splits_kaartspel(arr):
    if (len(arr)) == 1:
        return ([], arr)
    else:
        scheiding = math.floor(len(arr) / 2)
        
        arr1 = []
        arr2 = []

        for i in range(scheiding):
            arr1.append(arr[i])
        
        for i in range(scheiding, len(arr)):
            arr2.append(arr[i])

        return (arr1, arr2)


def faro_shuffle(arr1, arr2):
    newSpel = []
    teller = 0
    shuffleOngoing = True

    if arr1 == []:
        return arr2

    while shuffleOngoing:

        if teller <= len(arr1) - 1:
            newSpel.append(arr1[teller])
        newSpel.append(arr2[teller])
        
        if teller == len(arr2)-1:
            break
        else:
            teller += 1

    return newSpel