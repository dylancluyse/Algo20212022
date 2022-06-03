def dubbel(array):
    dict = {}

    for getal in array:
        if getal in dict:
            dict[getal] += 1
        else:
            dict[getal] = 1

    for getal in array:
        if dict[getal] >= 2:
            return getal


def dubbels(array):
    dict = {}

    for getal in array:
        if getal in dict:
            dict[getal] += 1
        else:
            dict[getal] = 1

    #print(dict)

    enkel = {}
    dubbel = {}

    for getal in array:
        #print(getal)
        if dict[getal] >= 2:
            if len(dubbel) == 0:
                dubbel = {getal}
            else:
                dubbel.add(getal)
        else:
            if len(enkel) == 0:
                enkel = {getal}
            else:
                enkel.add(getal)

    if len(enkel) == 0:
        enkel = set()
    
    if len(dubbel) == 0:
        dubbel = set()

    return (enkel, dubbel)