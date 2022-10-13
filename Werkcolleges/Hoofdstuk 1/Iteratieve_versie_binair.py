def zoekBinair(rij, zoekItem):
    n = len(rij)
    l = 0
    r = n - 1

    while l != r:
        print(f"{l}, {r}")
        m = (l+r)//2
        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m
    
    if rij[l] == zoekItem:
        index = l
    else:
        index = -1

    return index