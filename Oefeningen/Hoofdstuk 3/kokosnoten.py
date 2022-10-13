aantalPirates = int(input())
aantalKokos = int(input())
aantalNoten = 1

for x in range (1, aantalPirates + 1): 
    deelVanBuit = int(aantalKokos // aantalPirates)
    notenVoorAap = int(aantalKokos % aantalPirates)

    if notenVoorAap == 0:
        outputNotenVoorAap = "geen noten "
    elif notenVoorAap == 1:
        outputNotenVoorAap = "1 noot "
    else:
        outputNotenVoorAap = str(notenVoorAap) + " noten "

    print (str(aantalKokos) + ' noten = ' + str(deelVanBuit) + ' noten voor piraat#' + str(x) + ' en ' 
    + str(outputNotenVoorAap) + 'voor de aap')
    aantalKokos = aantalKokos - deelVanBuit - notenVoorAap

kokosPerPiraat = int(aantalKokos / aantalPirates)
kokosVoorAap = int(aantalKokos % aantalPirates)

if kokosVoorAap == 0:
        outputNotenVoorAap = "geen noten "
elif kokosVoorAap == 1:
        outputNotenVoorAap = "1 noot "
else:
        outputNotenVoorAap = str(kokosVoorAap) + " noten "

print('elke piraat krijgt ' + str(kokosPerPiraat) + ' noten en ' + str(outputNotenVoorAap) + ' voor de aap')

