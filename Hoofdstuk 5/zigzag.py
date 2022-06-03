# Niet afgewerkt!!

def iszigzag(array):

    n = len(array)
    fouten = 0

    for i in range(n):
        if i == 0:
            if array[i+1] > array[i]:
                fouten += 1

        elif i == n - 1:
            if i % 2 == 0:
                if array[i-1] > array[i]:
                    fouten += 1
            else:
                if array[i-1] < array[i]:
                    fouten += 1

        elif i % 2 == 0:
            if array[i-1] > array[i] and array[i+1] < array[i]:
                fouten += 1
        
        elif i % 2 == 1:
            if array[i-1] > array[i] and array[i+1] < array[i]:
                fouten += 1
    
    if fouten > 0:
        return False
    
    return True


def zigzag_traag(reeks):
    
    reeks.sort()
    n = len(reeks)

    if n % 2 == 1:
        n -= 1

    for i in range(0, n-1, 2):
        reeks[i], reeks[i+1] = reeks[i+1], reeks[i]

def zigzag_snel(reeks):
    n = len(reeks)


    for i in range(0, n-1):     
        if i % 2 == 0: 
            if i == 0 and reeks[i] <= reeks[i+1]:
                reeks[i], reeks[i + 1] = reeks[i+1], reeks[i]

            elif reeks[i] <= reeks[i+1]:
                reeks[i], reeks[i + 1] = reeks[i+1], reeks[i]

            if not i == 0  and reeks[i] <= reeks[i-1]:
                reeks[i], reeks[i - 1] = reeks[i-1], reeks[i]
            elif reeks[i] <= reeks[i-1]:
                reeks[i], reeks[i - 1] = reeks[i-1], reeks[i]