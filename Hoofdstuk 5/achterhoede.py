# Niet afgewerkt!!!

def zien(invoer):

    if isinstance(invoer, str):
        invoer = list(str(invoer))

    n = len(invoer)

    nieuweLijst = []

    for i in range(n-1, -1, -1):
        aantalRood = 0

        for j in range(i-1, -1, -1):
            if invoer[j] == 'R':
                aantalRood += 1
        
        if aantalRood % 2 == 0:
            nieuweLijst.append('B')
        else:
            nieuweLijst.append('R')
        
    nieuweLijst.reverse()

    return tuple(nieuweLijst)
    


zien(('R', 'B', 'R', 'R', 'B'))
zien(['R', 'R', 'B', 'R', 'R', 'B', 'R', 'B', 'R', 'R'])
zien('BBRBRBRBBRBR')
    

def zeggen(invoer):
    if isinstance(invoer, str):
        invoer = list(str(invoer))

    n = len(invoer)
    invoer = list(invoer)

    nieuweLijst = []

    for i in range(0, n):
        zien(invoer)
        nieuweLijst.append(invoer.pop(-1))
            
    nieuweLijst.reverse()

    return tuple(nieuweLijst)
        
    
        
        

zeggen(('B', 'R', 'R', 'B', 'R'))