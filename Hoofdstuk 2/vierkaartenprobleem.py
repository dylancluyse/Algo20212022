kenmerk = str(input())

if kenmerk == "waarde":
    getal = int(input())
    if getal == 8 or getal % 2 == 0:
        stelling = str(input())
        if stelling == "ja":
            print('Juist: kaarten met waarde ' + str(getal) + ' moeten gedraaid worden.')
        else:
            print('Fout: kaarten met waarde ' + str(getal) + ' moeten gedraaid worden.')
    else:
        stelling = str(input())
        if stelling == "ja":
            print('Fout: kaarten met waarde ' + str(getal) + ' moeten niet gedraaid worden.')
        else:
            print('Juist: kaarten met waarde ' + str(getal) + ' moeten niet gedraaid worden.')

if kenmerk == "kleur":
    kleur = str(input())
    if kleur != 'rood':
        stelling = str(input())
        if stelling == "ja":
            print('Juist: kaarten met kleur ' + str(kleur) + ' moeten gedraaid worden.')
        else:
            print('Fout: kaarten met kleur ' + str(kleur) + ' moeten gedraaid worden.')
    else:
        stelling = str(input())
        if stelling == "ja":
            print('Fout: kaarten met kleur ' + str(kleur) + ' moeten niet gedraaid worden.')
        else:
            print('Juist: kaarten met kleur ' + str(kleur) + ' moeten niet gedraaid worden.')
