toonladder = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']




def ontleding(akkoord):

    listTxt = list(str(akkoord))
    
    grondnoot = ''
    type = ''

    for i in range (len(listTxt)):
        if i == 0:
            grondnoot = listTxt[i]

        if i == 1 and listTxt[i] == '#':
            grondnoot +=  listTxt[i]

        if i != 0 and listTxt[i] != '#':
            type += listTxt[i]
        

    return(grondnoot, type)


def noten(grondnoot, lijst):
    arr = []
    
    plaats = 0

    for i in range(len(toonladder)):
        if grondnoot == toonladder[i]:
            plaats = i

    for letter in lijst:
        arr.append(toonladder[(plaats + letter) % 12])

    return arr


def akkoord(akkoord, bibTypesAkkoorden, bibSymVoor):
    strAkk = ontleding(akkoord)
    return tuple(noten(strAkk[0], bibTypesAkkoorden[bibSymVoor[strAkk[1]]]))
    

akkoordtypes = {'majeur':[0, 4, 7], 'mineur':[0, 3, 7], 'dominant septiem':[0, 4, 7, 10], 'mineur septiem':[0, 3, 7, 10], 'majeur septiem':[0, 4, 7, 11]}
akkoordsymbolen = {'':'majeur', 'm':'mineur', '7':'dominant septiem', 'm7':'mineur septiem', 'M7':'majeur septiem'}

print(akkoord('Gm7', akkoordtypes, akkoordsymbolen))