# NIET VOLLEDIG AFGEWERKT!!!!!!!!!!

def varkenswoord(woord):
    opgesplitst = list(str(woord))

    extra = ""
    special_characters = "!@#$%^&*()-+?_=,<>/"

    if opgesplitst[-1] in special_characters:
        extra = opgesplitst[-1]
        del opgesplitst[-1]

    if opgesplitst[0] in ('a', 'e', 'u', 'o', 'i', 'A', 'E', 'O', 'U', 'I'):
        opgesplitst.append('way')
    else:
        for i in range(0, len(opgesplitst)):
            if opgesplitst[i] not in ('a', 'e', 'u', 'o', 'i', 'A', 'E', 'I', 'O', 'U'):
                
                if opgesplitst[i] in special_characters:
                    opgesplitst.append(opgesplitst[i])
                elif i == 0:
                    opgesplitst.append(opgesplitst[i].lower())
                else:
                    opgesplitst.append(opgesplitst[i])
            else:
                break 
        for j in range(0, i):
            if(opgesplitst[0].isupper()):
                opgesplitst.pop(0)
                if opgesplitst[0] == 'a':
                    opgesplitst[0] = 'A'
                elif opgesplitst[0] == 'e':
                    opgesplitst[0] = 'E'
                elif opgesplitst[0] == 'u':
                    opgesplitst[0] = 'U'
                elif opgesplitst[0] == 'i':
                    opgesplitst[0] = 'I'
                elif opgesplitst[0] == 'o':
                    opgesplitst[0] = 'O'
            else:
                opgesplitst.pop(0)
            
        opgesplitst.append('ay')
        opgesplitst.append(extra)

    return ''.join(opgesplitst)


def varkenslatijn(zin):
    
    woorden = zin.split(' ')
    nieuweZin = []

    for i in range(len(woorden)):
        if i == 0:
            nieuweZin.append(varkenswoord(woorden[i]).capitalize())
        else:
            nieuweZin.append(varkenswoord(woorden[i]))
 
    return ' '.join(nieuweZin)

