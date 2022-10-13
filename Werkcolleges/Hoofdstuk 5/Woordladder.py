#Hoofdstuk 5: Graafalgoritmes

#Woordladder
def precies_een_verschillend(woord1, woord2):
    #Lengte identiek?
    if len(woord1) != len(woord2):
        return False
    verschilTeller = 0

    #woord overlopen, letter per letter
    for i in range (len(woord1)):
        if woord1[i] != woord2[i]:
            verschilTeller += 1
    return verschilTeller == 1


def maak_graaf(woorden):

    #dictionary aanmaken
    #we genereren alle woorden in deze dictionary
    dict = {
        woord:set() for woord in woorden
    }

    for positie, woord1 in enumerate(woorden):
        for positie2 in range(positie + 1, len(woorden)):
            woord2 = woorden[positie2]
            if(precies_een_verschillend(woord1, woord2)):
                dict[woord1].add(woord2)
                dict[woord2].add(woord1)
    return dict
    
def kortste_pad(graaf, startWoord):
    #Afstand bijhouden
    D = {w : -1 for w in graaf}
    
    #Voorganger bijhouden
    P = {w : None for w in graaf}
    D[startWoord] = 0
    P[startWoord] = startWoord

    #Wachtrij aanmaken
    Q = []
    Q.append(startWoord)

    #Zolang de wachtrij niet leeg is
    while len(Q) > 0:
        v = Q.pop(0)
        for w in sorted(graaf[v]):
            if D[w] == -1:
                D[w] = D[v]+1
                P[w] = v
                Q.append(w)
    return P


def geef_pad(voorgangers, doelWoord):
    #Array aanmaken die we gaan gebruiken voor het pad
    pad = [doelWoord]
    
    #Woord waar we momenteel op staan
    huidigwoord = doelWoord
    
    #
    voorganger = voorgangers[huidigwoord]

    #Zolang dat het woord niet gelijk staat aan zijn voorganger, plaats opschuiven
    while huidigwoord != voorganger:
        #Voorganger toevoegen en plaatsje opschuiven
        pad.insert(0, voorganger)
        huidigwoord = voorganger
        voorganger = voorgangers[huidigwoord]
    return pad