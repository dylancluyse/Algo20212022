waardeF100 = 0
for x in range(1, 101):
    waardeF100 += (1 / x ** 2)

print(waardeF100)

kleinsteWaarde = 0

for x in range(1, 400):
    kleinsteWaarde = 1 / x ** 2
    if(abs(kleinsteWaarde)) <= 0.0001:
        break

print(x)