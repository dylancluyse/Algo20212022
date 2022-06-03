aantalAppels = int(input())

aantalKisten = aantalAppels // 20
aantalPaletten = aantalKisten // 35
aantalKistenMetOvergeblevenAppels = (aantalAppels // 20) % 35
aantalRest = aantalAppels % 20

print(aantalPaletten)
print(aantalKistenMetOvergeblevenAppels)
print(aantalRest)