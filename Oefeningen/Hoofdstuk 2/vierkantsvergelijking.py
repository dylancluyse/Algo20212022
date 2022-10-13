import math

a = float(input())
b = float(input())
c = float(input())

if ((b ** 2) - 4 * a * c) < 0:
    print('geen wortels')
elif ((b ** 2) - 4 * a * c) == 0:
    print('een wortel')
    wortel1 = (-b / (-2 * -a))
    print(wortel1)
else:
    print('twee wortels')
    wortel1  = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    wortel2 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    
    if wortel1 < wortel2:
        print (wortel1)
        print (wortel2)
    else:
        print(wortel2)
        print(wortel1)