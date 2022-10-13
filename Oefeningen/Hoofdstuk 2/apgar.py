a = str(input())
p = int(input())
g = str(input())
a2 = str(input())
r = str(input())

score = 0
ongeldig = 0

if a == "zwak":
    score = score + 1
elif a == "goed doorhuilen":
    score = score + 2
elif a == "geen":
    score = score
else:
    ongeldig = ongeldig + 1

if p >= 100:
    score = score + 2
elif p < 100 and p > 0:
    score = score + 1
elif p == 0:
    score = score
else:
    ongeldig = ongeldig + 1


if g == "enige flexie":
    score = score + 1
elif g == "actieve beweging":
    score = score + 2
elif g == "slap":
    score = score
else:
    ongeldig = ongeldig + 1

if a2 == "extremiteiten":
    score = score + 1
elif a2 == "roze":
    score = score + 2
elif a2 == "blauw" or a2 == "bleek":
    score = score
else:
    ongeldig = ongeldig + 1

if r == "enige beweging":
    score = score + 1
elif r == "krachtig huilen":
    score = score + 2
elif r == "geen":
    score = score
else:
    ongeldig = ongeldig + 1

if ongeldig > 0:
    print("ongeldige invoer")
elif score < 4:
    print("alarm")
else:
    print(score)
