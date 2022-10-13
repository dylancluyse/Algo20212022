class Bifid:
    def __init__(self, nummer, grid):
        assert 2 <= nummer <= 10, 'er moet gelden dat 2 <= n <= 10'
        assert nummer * nummer == len(grid), 'aantal symbolen komt niet overeen met grootte van het rooster'

        self.nummer = nummer

        lijst = list(str(grid))

        grote = []
        for i in range(0, len(lijst), nummer):
            kleine = []
            for j in range(i, nummer + i):
                kleine.append(lijst[j])
            grote.append(kleine)
        self.grid = grote

    def symbool(self, getal1, getal2):
        assert getal1 >= 0, "ongeldige positie in rooster"
        assert getal2 >= 0, "ongeldige positie in rooster"
        assert len(self.grid) > getal1 and len(self.grid[0]) > getal2, "ongeldige positie in rooster"
        return self.grid[getal1][getal2]

    def positie(self, woord):
        special_characters = "@#^&*+_<>/~"
        assert len(woord) == 1, 'symbool moet uit 1 karakter bestaan'
        assert woord not in special_characters, f"onbekend symbool: '{woord}'"
        for rij in range(len(self.grid)):
            for kolom in range(len(self.grid[rij])):
                if self.grid[rij][kolom] == woord:
                    return (rij, kolom)

    def codeer(self, string):
        zin = list(str(string))
        
        arrayRijen = []
        arrayKolommen = []

        for i in range(0, len(zin)):
            arrayRijen.append(self.positie(zin[i])[0])
            arrayKolommen.append(self.positie(zin[i])[1])

        array = (arrayRijen + arrayKolommen)

        zin = []

        for i in range(0, len(array) - 1, 2):
            zin.append(self.symbool(array[i], array[i+1]))
     
        return ''.join(zin)


    def decodeer(self, string):
        zin = list(str(string))
        
        array = []

        for i in range(0, len(zin)):
            array.append(self.positie(zin[i])[0])
            array.append(self.positie(zin[i])[1])

        middle_index = len(array) // 2

        arrayRijen = array[:middle_index]
        arrayKolommen = array[middle_index:]

        
        zin = []
        
        for i in range(len(arrayRijen)):
            zin.append(self.symbool(arrayRijen[i], arrayKolommen[i]))

        return ''.join(zin)

