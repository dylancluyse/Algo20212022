ehprijsBoek = 24.95
percent = 0.6
aantal = 60

totaleAankoopKosten = (float(ehprijsBoek) * float(percent)) * aantal
totaleVervoerKosten = 3 + ((aantal - 1) * 0.75)
totaleSom = float(totaleAankoopKosten) + float(totaleVervoerKosten)
print(totaleSom)