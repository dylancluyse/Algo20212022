aantalTjirps = int(input("Geef het aantal tjirps per minuut in"))
temperatuurFah = 50 + ((aantalTjirps - 40) / 4)
temperatuurCelc = 10 + ((aantalTjirps - 40) / 7)

print("temperature (Fahrenheit): " + str(temperatuurFah))
print("temperature (Celsius): " + str(temperatuurCelc))