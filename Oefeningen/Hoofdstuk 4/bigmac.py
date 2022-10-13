def waardering(bigMacPrijs, wisselkoers2):
    wisselkoers1 = float(bigMacPrijs / 4.07)
    waardering = ((wisselkoers1 - wisselkoers2) / wisselkoers2) * 100

    if waardering <= -25:
        return 'sterk ondergewaardeerd'
    elif waardering <= -5:
        return 'ondergewaardeerd'
    elif waardering <= 5:
        return 'ongeveer gelijk'
    elif waardering <= 25:
        return 'overgewaardeerd'
    else:
        return 'sterk overgewaardeerd'


def wisselkoersanalyse(lokaleMunt, wisselkoers):
    lokaleMunt = lokaleMunt.split(' ')
    
    bigMacPrijs = lokaleMunt[0]
    
    munteenheid = ""
    
    for i in range(1, len(lokaleMunt)):
        if i == 1:
            munteenheid += lokaleMunt[i]
        else:
            munteenheid += " " + lokaleMunt[i]
        
        
    
    result = waardering(float(bigMacPrijs), float(wisselkoers))

    return(f'De {str(munteenheid)} is {str(result)} ten opzichte van de dollar.')
