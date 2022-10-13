getal1 = int(input())
getal2 = int(input())

somGetal1 = 0

for x in range(1, getal1):
    if getal1 % x == 0:
        somGetal1 += x

somGetal2 = 0

for x in range(1, getal2):
    if getal2 % x == 0:
        somGetal2 += x

if somGetal1 == getal2 and somGetal2 == getal1:
    print(str(getal1) + ' en ' + str(getal2) + ' zijn bevriende getallen')
else:
    print(str(getal1) + ' en ' + str(getal2) + ' zijn geen bevriende getallen')
