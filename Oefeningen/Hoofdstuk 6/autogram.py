def enkelLetters(zin):
    nieuweZin = []

    for letter in zin:
        if letter.isalnum():
            nieuweZin.append(letter.lower())
    
    return nieuweZin


def letterfrequenties(zin):
    dict = {}
    
    zin = list(str(zin))

    zin = enkelLetters(zin)


    for letter in zin:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    
    return dict


def letterposities(zin):
    dict = {}

    zin = list(str(zin))

    teller = 0

    for letter in zin:

        if letter.isalnum():
            if letter.lower() in dict:
                dict[letter.lower()].add(teller)
            else:
                dict[letter.lower()] = {teller}
        
        teller += 1
    
    return dict