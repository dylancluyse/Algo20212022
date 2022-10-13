def controleren(code):
    if code[:3] not in {'978', '979'}:
        return False

    cijfer = 0
    for i in range(12):
        if i % 2:
            cijfer += 3 * int(code[i])
        else: 
            cijfer += int(code[i])
    
    cijfer = cijfer % 10
    cijfer = (10 - cijfer) % 10
    return cijfer == int(code[-1])


def overzicht(codes):

    onderverdeling = {}

    for id in range(11):
        onderverdeling[id] = 0

    for code in codes:
        if controleren(code) == False:
            onderverdeling[10] += 1
        else:
            onderverdeling[int(code[3])] += 1

    totaalEngels = onderverdeling[0] + onderverdeling[1]
    totaalOverig = onderverdeling[6] + onderverdeling[8] + onderverdeling[9]

    print(f'Engelstalige landen: {totaalEngels}')
    print(f'Franstalige landen: {onderverdeling[2]}')
    print(f'Duitstalige landen: {onderverdeling[3]}')
    print(f'Japan: {onderverdeling[4]}')
    print(f'Russischtalige landen: {onderverdeling[5]}')
    print(f'China: {onderverdeling[7]}')
    print(f'Overige landen: {totaalOverig}')
    print(f'Fouten: {onderverdeling[10]}')
