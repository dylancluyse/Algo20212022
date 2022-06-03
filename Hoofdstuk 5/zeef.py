import math
from math import factorial

def driehoek(n):

    assert type(n) != str, "ongeldig aantal rijen"
    assert type(n) != float, "ongeldig aantal rijen" 
    assert n >= 0, "ongeldig aantal rijen" 

    driehoek = []

    for i in range(n):
        laag = []
        for j in range(i+1):
            laag.append(factorial(i)//(factorial(j)*factorial(i-j)))
        driehoek.append(laag)

    return driehoek


def zeshoek(a, b):
    newdriehoek = driehoek(a + 5)
    
    #print(newdriehoek)

    assert b + 1 < len(newdriehoek[a]), 'ongeldige interne positie'
    assert a > 2, 'ongeldige interne positie'

    return [newdriehoek[a-2][b-2], newdriehoek[a-2][b-1], newdriehoek[a-1][b], newdriehoek[a][b], newdriehoek[a][b-1], newdriehoek[a-1][b-2]]



def kwadraat(a, b):
    sixhook = zeshoek(a,b)
    
    product = 0

    for i in range(len(sixhook)):
        if i == 0:
            product = sixhook[0]
        else:
            product *= sixhook[i]
    
    return f'{sixhook[0]} x {sixhook[1]} x {sixhook[2]} x {sixhook[3]} x {sixhook[4]} x {sixhook[5]} = {product} = {int(math.sqrt(product))} x {int(math.sqrt(product))}'

