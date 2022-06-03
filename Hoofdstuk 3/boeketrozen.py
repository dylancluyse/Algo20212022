totaalWitRood = int(input())
totaalWitBlauw = int(input())
operator = str(input())

blauw = rood = wit = 0
vlag = False

while blauw <= totaalWitBlauw:
    while rood <= totaalWitRood:
        while wit <= totaalWitRood:
           
            if operator == ">":
                if blauw + rood > wit + blauw and blauw + wit == totaalWitBlauw and wit + rood == totaalWitRood and blauw >= 2 and wit >= 2 and rood >= 2:
                    vlag = True
                    break
            else:
                if blauw + rood < wit + blauw and blauw + wit == totaalWitBlauw and wit + rood == totaalWitRood and blauw >= 2 and wit >= 2 and rood >= 2:
                    vlag = True
                    break
            wit += 1
        if vlag == True:
            break
        wit = 0
        rood += 1
    if vlag == True:
        break
    rood = 0
    blauw += 1

print(blauw)
print(wit)
print(rood)