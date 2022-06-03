def csom(x):
    a = list(str(x))
    n = len(a)

    som = x


    while n != 1:
        som = 0
        for i in range(0, n):
            som += int(a[i])
        a = list(str(som))
        n = len(a)
    
    return som