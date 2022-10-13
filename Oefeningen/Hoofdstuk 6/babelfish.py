woordenboek = {}

def vertalingToevoegen(woord1, woord2, woordenboek):
    woordenboek[woord1] = woord2

def vertaling(woord, woordenboek):
    if woord in woordenboek:
        return woordenboek[woord]
    else:
        return '???'