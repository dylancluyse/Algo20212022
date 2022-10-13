ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())
cx = int(input())
cy = int(input())
dx = int(input())
dy = int(input())

#meest linkse
if ax <= bx:
    #hoogste
    if ay >= by:
        lbR1 = [ax, ay]
        roR1 = [bx, by]
    else:
        lbR1 = [ax, by]
        roR1 = [bx, ay]
else:
    if ay >= by:
        lbR1 = [bx, ay]
        roR1 = [ax, by]
    else:
        lbR1 = [bx, by]
        roR1 = [ax, ay]

#meest rechtse
if ax >= bx:
    #laagste
    if ay <= by:
        loR1 = [bx, ay]
        rbR1 = [ax, by]
    else:
        loR1 = [bx, by]
        rbR1 = [ax, ay] 
else:
    if ay <= by:
        loR1 = [ax, ay]
        rbR1 = [bx, by]
    else:
        loR1 = [ax, by]
        rbR1 = [bx, ay]

#Part twee
#meest linkse
if cx <= dx:
    #hoogste
    if cy >= dy:
        lbR2 = [cx, cy]
        roR2 = [dx, dy]
    else:
        lbR2 = [cx, dy]
        roR2 = [dx, cy]
else:
    if cy >= dy:
        lbR2 = [dx, cy]
        roR2 = [cx, dy]
    else:
        lbR2 = [dx, dy]
        roR2 = [cx, cy]

#meest rechtse
if cx >= dx:
    #laagste
    if cy <= dy:
        loR2 = [dx, cy]
        rbR2 = [dx, dy]
    else:
        loR2 = [dx, dy]
        rbR2 = [cx, cy] 
else:
    if cy <= dy:
        loR2 = [cx, cy]
        rbR2 = [dx, dy]
    else:
        loR2 = [cx, dy]
        rbR2 = [dx, cy]

#Part Drie: middens bepalen:

mLinks = [loR2[0], int((loR2[1] + lbR2[1]) / 2)]
mTop = [int((lbR2[0] + rbR2[0]) / 2), lbR2[1]]
mBot = [int((lbR2[0] + rbR2[0]) / 2), loR2[1]]
mRechts = [roR2[0], int((loR2[1] + lbR2[1]) / 2)]


#situatie: linkerbovenhoek in rechteronderhoek
if lbR2[0] > loR1[0] and lbR2[0] < roR1[0] and lbR2[1] > roR1[1] and lbR2[1] < rbR1[1]:
    print('botsing')
#situatie: rechterbovenhoek in linkeronderhoek
elif rbR2[0] > loR1[0] and rbR2[0] < roR1[0] and rbR2[1] > roR1[1] and rbR2[1] < rbR1[1]:
    print('botsing')
#situatie: rechteronderhoek in linkerbovenhoek
elif roR2[0] > lbR1[0] and roR2[0] < rbR1[0] and roR2[1] > loR1[1] and roR2[1] < lbR1[1]:
    print('botsing')
#situatie: linkeronderhoek in rechterbovenhoek
elif loR2[0] > lbR1[0] and loR2[0] < rbR1[0] and loR2[1] > roR1[1] and loR2[1] < rbR1[1]:
    print('botsing')
#middens erin
elif mLinks[0] > lbR1[0] and mLinks[0] < rbR1[0] and mLinks[1] > loR1[1] and mLinks[1] < lbR1[1]:
    print('botsing')
elif mTop[0] > lbR1[0] and mTop[0] < rbR1[0] and mTop[1] > loR1[1] and mTop[1] < lbR1[1]:
    print('botsing')
elif mBot[0] > lbR1[0] and mBot[0] < rbR1[0] and mBot[1] > loR1[1] and mBot[1] < lbR1[1]:
    print('botsing')
elif mRechts[0] > lbR1[0] and mRechts[0] < rbR1[0] and mRechts[1] > loR1[1] and mRechts[1] < lbR1[1]:
    print('botsing')
elif lbR1 == lbR2 and rbR1 == rbR2 and loR1 == loR2 and roR1 == roR2:
    print('botsing') 
else:
    print('geen botsing')