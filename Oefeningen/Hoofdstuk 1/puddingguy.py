aantalGekochteStuks = int(input("Geef het aantal gekochte stuks van een bepaald product: "))
kostprijsPerStuk = float(input("Geef de kostprijs in: "))
aantalBarcodes = int(input("Geef het aantal barcodes in dat nodig is voor een frequent flyer coupon: "))
aantalMijl = int(input("Geef het aantal mijlen in dat men ontvangt per frequent flyer coupon: "))

kost = float(aantalGekochteStuks * kostprijsPerStuk)
frequentFlyerMijlen = int(aantalGekochteStuks / aantalBarcodes) * aantalMijl

print("Phillips spendeerde $" + str(kost) + " voor " + str(frequentFlyerMijlen) + " frequent flyer mijlen.")
