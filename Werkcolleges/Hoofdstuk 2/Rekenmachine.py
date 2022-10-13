def evalueer_postfix(expressie):
    uitvoer = []
    for symbool in expressie:
        if symbool.isnumeric():
            uitvoer.append(symbool)
        else:
            getal1 = uitvoer.pop()
            getal2 = uitvoer.pop()
            uitkomst = voerBewerkingUit(float(getal1), float(getal2), symbool)
            uitvoer.append(uitkomst)
    return uitvoer.pop()

def voerBewerkingUit(getal1, getal2, operator):
    if operator == '*':
        return getal1 * getal2
    elif operator == '/':
        return getal2 / getal1
    elif operator == '+':
        return getal1 + getal2
    else:
        return getal2 - getal1

def infix_naar_postfix(expressie):
    stapel = []
    uitvoer = []
    for symbool in expressie:
        if symbool.isnumeric():
            uitvoer.append(symbool)
        else:
            if symbool == ")":
                bovenste = stapel.pop()
                while bovenste != "(":
                    uitvoer.append(bovenste)
                    bovenste = stapel.pop()
            elif len(stapel) == 0 or prioriteit(symbool) > prioriteit(stapel[-1]) or symbool == "(":
                stapel.append(symbool)
            else:
                while len(stapel) > 0 and (prioriteit(stapel[-1]) >= prioriteit(symbool)):
                    uitvoer.append(stapel.pop())
                stapel.append(symbool) 
    while len(stapel) > 0:
        uitvoer.append(stapel.pop())
    return uitvoer

def prioriteit(symb):
    if symb == "*" or symb == "/":
        return 2
    elif symb == "+" or symb == "-":
        return 1
    else:
        return 0
def rekenmachine(s):
    infix = s.split()
    postfix = infix_naar_postfix(infix)
    return evalueer_postfix(postfix)
