def maximale_blootstelling(x):
    if x < 80:
        return -1.0
    elif x <=83:
        return 28800.0
    else:
        verschil = x - 83
        hoeveelsteInterval = verschil // 3
        totaal = 8 * 60 * 60
        for i in range(1, hoeveelsteInterval + 2):
            totaal /= 2
        return totaal
