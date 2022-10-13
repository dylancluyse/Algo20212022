waardeKaart = int(input())
eindeSpel = False
som = waardeKaart


while som < 21:
    waardeKaart = int(input())
    if waardeKaart == 0:
        break
    som += waardeKaart

if som < 21:
    print('Voorzichtig gespeeld (' + str(som) + ')')
elif som == 21:
    print('Gewonnen!')
else:
    print('Verbrand (' + str(som) + ')')