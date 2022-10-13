class HashSet:

    DELETED = -9999

    def __init__(self, max_size=10):
        self.max = max_size
        self.arr = [None] * max_size
        self.nb = 0

    def add(self, item):
        #volle lijst?
        if self.nb == self.max:
            raise ValueError()
        index = hash(item) % self.max
        while self.arr[index] != None or self.arr[index] != self.DELETED:
            index = (index + 1) % self.max
        self.arr[index] = item
        self.nb += 1
        return index


    def index_of(self, item):
        index = hash(item) % self.max
        
        #start bijhouden in het geval van een volle lijst
        startIndex = index

        while(self.arr[index] != item):
            
            #waarde niet in de cluster
            if self.arr[index] == None:
                return -1
            
            index = (index + 1) % self.max
            
            #waarde niet gevonden in de array
            if startIndex == index:
                return -1
        
        return index

    def delete(self, item):
        index = self.index_of(item)
        if index == -1:
            return False
        else:
            self.arr[index] == HashSet.DELETED
            self.nb -= 1
            return True