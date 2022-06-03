getal = int(input())

beleefdheid = 0
for i in range (1, getal):
    som = 0
    for j in range (i, getal):
        som += j
        if som > getal:
            break
        elif som == getal:
            beleefdheid += 1
            break

print(beleefdheid)