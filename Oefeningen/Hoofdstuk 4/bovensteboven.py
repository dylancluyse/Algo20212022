def bovensteboven(x):
    a = list(str(x))
    n = len(a)
    foutenTeller = 0

    #print(f'{a[i]} en {a[(n-1)-i]}')

    for i in range(0, n):
        if a[i] == '6' and a[(n-1)-i] == '9':
            foutenTeller
        elif a[i] == '9' and a[(n-1)-i] == '6':
            foutenTeller
        elif a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '9':
            foutenTeller += 1
        elif a[i] != a[(n-1)-i]:
            foutenTeller += 1

    if foutenTeller >= 1:
        return False
    else:
        return True

def volgende(x):
    eindeLus = False
    while eindeLus == False:
        x += 1
        if bovensteboven(x) == True:
            return x