#Vignèrecodering
def decodeer(t, s):
    chars = ['A','B','C','D','E','F','G','H','I','J','K','L', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    a = list(str(s))
    b = list(str(t))
    nieuweSleutel = []
    for i in range(0, len(a)):
        nieuweSleutel.append(a[i])
    #Verlengen van sleutelwoord
    for i in range (0, len(b) - len(a)):
        for j in range(0, len(a)):
            if len(list(nieuweSleutel)) >= len(b):
                break
            nieuweSleutel.append(a[j])
        
    codeerdeTekst = []
    for i in range(0, len(b)):
        if b[i] == " ":
            codeerdeTekst.append(" ")
        elif b[i] == '!' or b[i] == ',' or b[i] == ':' or b[i] == ';' or b[i] == '.' or b[i] == '?' or b[i] == "'" or b[i] == '-':
            codeerdeTekst.append(b[i])
        else:
            for tellerTekst in range (0, len(chars)):
                if b[i] == chars[tellerTekst]:
                    waarde = numbs[tellerTekst]
            for tellerSleutel in range (0, len(chars)):
                if nieuweSleutel[i] == chars[tellerSleutel]:
                    waarde -= numbs[tellerSleutel]
            
            waarde = waarde % 26
            codeerdeTekst.append(chars[waarde])
    s = ""
    
    return(str(s.join(codeerdeTekst)))   

def codeer(t, s):
    chars = ['A','B','C','D','E','F','G','H','I','J','K','L', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    a = list(str(s))
    b = list(str(t))
    nieuweSleutel = []
    for i in range(0, len(a)):
        nieuweSleutel.append(a[i])
    #Verlengen van sleutelwoord
    for i in range (0, len(b) - len(a)):
        for j in range(0, len(a)):
            if len(list(nieuweSleutel)) >= len(b):
                break
            nieuweSleutel.append(a[j])
        
    codeerdeTekst = []
    for i in range(0, len(b)):
        if b[i] == " ":
            codeerdeTekst.append(" ")
        elif b[i] == '!' or b[i] == ',' or b[i] == ':' or b[i] == ';' or b[i] == '.' or b[i] == '?' or b[i] == "'" or b[i] == '-':
            codeerdeTekst.append(b[i])
        else:
            waarde = 0
            for tellerTekst in range (0, len(chars) - 1):
                if b[i] == chars[tellerTekst]:
                    waarde += numbs[tellerTekst]
            for tellerSleutel in range (0, len(chars) - 1):
                if nieuweSleutel[i] == chars[tellerSleutel]:
                    waarde += numbs[tellerSleutel]
            
            waarde = waarde % 26
            codeerdeTekst.append(chars[waarde])
    s = ""
    
    return(str(s.join(codeerdeTekst)))