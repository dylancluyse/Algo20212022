import heapq

class AchtPuzzel:

    BUREN = {0 : {("R", 1),("O", 3)},   1 : {("L", 0),("R", 2),("O", 4)},   2 : {("L",1),("O",5)},
             3 : {("B",0),("R",4),("O",6)}, 4 : {("B",1),("L", 3),("R", 5),("O",7)}, 5 : {("B",2),("L", 4),("O",8)},
             6 : {("B",3),("R",7)},   7 : {("B",4),("L",6),("R",8)},   8 : {("B",5),("L",7)} 
            }

    def __init__(self, bord="123456780"):
        self.bord = bord


    def __str__(self):
        return self.bord[:3] +  "\n" + self.bord[3:6] + "\n" + self.bord[6:]

    def __repr__(self):
        return f"AchtPuzzel(bord='{self.bord}')"


    def __eq__(self, other):
        if isinstance(other, AchtPuzzel):
            return self.bord == other.bord
        return False


    def __hash__(self):
        return hash(self.bord)

    #geef een set terug van paren, elk paar staat voor een actie 'a' en 
    #een nieuwe achtpuzzel 's'
    def opvolgers(self):
        index_0 = self.bord.find('0')
        opv = set()

        for(actie, index) in AchtPuzzel.BUREN[index_0]:
            minn = min(index_0, index)
            maxx = max(index_0, index)
            nieuwe_puzzel = self.bord[:minn] + self.bord[:maxx] + self.bord[minn + 1:maxx] + self.bord[minn] + self.bord[maxx + 1:]
            opv.add((actie, AchtPuzzel(nieuwe_puzzel)))
        return opv
    
    def aantal_verkeerd(self, other):
        aantal = 0
        for ind, char in enumerate(self.bord):
            if char != '0' and char != other.bord[ind]:
                aantal += 1
        return aantal

    def manhattan_heuristiek(self, other):
        totale_afstand = 0
        for indice1, char in enumerate(self.bord):
            if char != '0':
                indice2 = other.bord.find(char)
                totale_afstand += AchtPuzzel.manhattan_distance(indice1, indice2)
        return totale_afstand

    @staticmethod
    def manhattan_distance(indice1, indice2):
        x1, y1 = indice1 // 3, indice1 % 3
        x2, y2 = indice2 // 3, indice1 % 3
        return abs(x1 - x2) + abs (y1 - y2)


class Plan:

    def __init__(self, toestand, voorganger=None, actie=None, kost=0, h_waarde=float("inf")):
        self.toestand = toestand
        self.voorganger = voorganger
        self.actie = actie
        self.kost = kost
        self.h_waarde = h_waarde

    ## Vergelijk op basis van cost + heuristic
    def __lt__(self, other):
        return self.kost + self.h_waarde < other.kost + other.h_waarde

    def geef_actie_sequentie(self):
        acties = []
        huidig = self
        while huidig.actie:
            acties.append(huidig.actie)
            huidig = huidig.voorganger
        return acties[::-1]
    
def a_ster_zoeken(start_toestand, is_doel, heuristiek, kost= lambda s,a : 1):
    plannen = []
    toestanden = set() #geslotenlijst
    heapq.heappush(plannen, Plan(start_toestand))

    while len(plannen) > 0:
        huidig_plan = heapq.heappop(plannen)
        if is_doel(huidig_plan):
            return huidig_plan.geef_actie_sequentie(), huidig_plan.kost
        else:
            if huidig_plan.toestand not in toestanden:
                toestanden.add(huidig_plan.toestand)
                for actie, opvolger in sorted(huidig_plan.toestand.opvolgers()):
                    nieuw_plan = Plan(toestand=opvolger, voorganger=huidig_plan, actie=actie, kost=huidig_plan.kost + kost(huidig_plan, actie), h_waarde=heuristiek(opvolger))
                    heapq.heappush(plannen, nieuw_plan)
    return None
