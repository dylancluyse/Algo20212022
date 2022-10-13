class QueueList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende
    
    def __init__(self):
        self.kop = None
        self.staart = None

    def empty(self):
        return self.kop is None
    
    def enqueue(self, data):
        hulp = self.Knoop(data)

        if self.empty():
            self.kop = hulp
            self.staart = hulp  
        else:
            self.staart.volgende = hulp
            self.staart = hulp
    
    def front(self):
        return self.kop.data
    
    def dequeue(self):
        if not self.empty():
            x = self.kop.data
            if self.kop == self.staart:
                self.kop = None
                self.staart = None
            else:
                self.kop = self.kop.volgende
            return x

    def invert(self):
        if not self.empty():
            vorige = None
            huidige = self.kop

            while huidige.volgende is not None:
                volgende = huidige.volgende
                huidige.volgende = vorige
                vorige = huidige
                huidige = volgende
            
            huidige.volgende = vorige
            self.kop, self.staart = self.staart, self.kop

