def omgekeerd(dict):
    omgekeerdeDict = {}
    for key in dict:
        omgekeerdeDict[str(dict[key])] = str(key)

    return(omgekeerdeDict)

def code39(zin, sleutel):
    listZin = list(str(zin))
    newZin = ""

    for i in range(len(listZin)):

        if i == len(listZin)-1:
            newZin += sleutel[listZin[i].upper()]
        else:
            newZin += sleutel[listZin[i].upper()] + 's'

    return newZin

def decode39(zin, sleutel):
    
    omgekeerdeSleutel = omgekeerd(sleutel)

    listZin = list(str(zin))
    newZin = ''


    woord = ''
    for i in range(len(listZin)):

        woord += listZin[i]

        if len(woord) == 10:
            newZin += str(omgekeerdeSleutel[woord[:-1]])
            woord = ''

        if i == len(listZin) - 1 and len(woord) == 9:
            newZin += str(omgekeerdeSleutel[woord])

    return newZin