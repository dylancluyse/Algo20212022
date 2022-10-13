x1 = int(input("Geef het eerste getal in:"))
x2 = int(input("Geef het tweede getal in:"))
x3 = int(input("Geef het derde getal in:"))
x4 = int(input("Geef het vierde getal in:"))
x5 = int(input("Geef het vijfde getal in:"))
x6 = int(input("Geef het zesde getal in:"))
x7 = int(input("Geef het zevende getal in:"))
x8 = int(input("Geef het achtste getal in:"))
x9 = int(input("Geef het negende getal in:"))

controlecijfer = (x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 + 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9) % 11

print(controlecijfer)