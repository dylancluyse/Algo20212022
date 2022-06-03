def evenOneven(getal):
    l = list(str(getal))
    tellerEven = tellerOneven = 0
    
    for i in range (0, len(l)):
        if int(l[i]) % 2 == 1:
            tellerOneven += 1
        #elif int(l[i]) == 0:
        #    pass
        elif int(l[i]) % 2 == 0:
            tellerEven += 1
    return (tellerEven, tellerOneven)           


def volgende(getal):
    l = list(str(getal))
    aantalGetallen = len(l)
    tellerEven = tellerOneven = 0
    
    for i in range (0, aantalGetallen):
        if int(l[i]) % 2 == 1:
            tellerOneven += 1
        elif int(l[i]) % 2 == 0:
            tellerEven += 1

    return int(str(tellerEven) + str(tellerOneven) + str(aantalGetallen))

def stappen(getal):
    teller = 0
    while getal != 123:
        getal = volgende(getal)
        teller += 1
    return teller