def beweeg(tupel, beweging):
    
    x = tupel[0]
    y = tupel[1]

    if beweging == '<':
        tupel = (x - 1, y)
    elif beweging == '^':
        tupel = (x, y + 1)
    elif beweging == 'v':
        tupel = (x, y - 1)
    elif beweging == '>':
        tupel = (x + 1, y)
    else:
        tupel

    return tupel

def teruggekeerd(lijst):
    nieuwePositie = (0, 0)
    for beweging in lijst:
        nieuwePositie = beweeg(nieuwePositie, beweging)
        
    if nieuwePositie == (0,0):
        return True
    else:
        return False

def laatste_levende_positie(lijst):
    
    
    teller = 1

    n = len(lijst)
    stop = False

    nieuwePositie = (0,0)

    for i in range(0, n):
        if stop == True:
            break

        if i+1 < n:
            if (lijst[i] == '<' and lijst[i+1] == '>') or (lijst[i] == '>' and lijst[i+1] == '<') or (lijst[i] == 'v' and lijst[i+1] == '^') or (lijst[i] == '^' and lijst[i+1] == 'v'):
                nieuwePositie = beweeg(nieuwePositie, lijst[i])
                stop = True
            else:
                teller += 1
                nieuwePositie = beweeg(nieuwePositie, lijst[i])
        
        if i == n-1:
            nieuwePositie = beweeg(nieuwePositie, lijst[n - 1])
        
    return (teller, nieuwePositie[0], nieuwePositie[1])