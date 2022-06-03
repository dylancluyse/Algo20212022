beginUur = int(input())
beginMin = int(input())
eindUur = int(input())
eindMin = int(input())

startMin = float(beginUur + beginMin / 60)
eindMin = float(eindUur + eindMin / 60)

tarief = 0

if startMin < 18 or eindMin < startMin:
    print("ongeldige invoer")
else:
    if eindMin < 21.5:
        tarief = (eindMin - startMin) * 2
        print(tarief)
    elif startMin < 21.5:
        tarief = ((21.5 - startMin) * 2) + ((eindMin - 21.5) * 4)
        print(tarief)
    else:
        tarief = ((eindMin - startMin) * 4)
        print(tarief)


