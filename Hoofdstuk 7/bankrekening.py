class BankRekening:
    def __init__(self, naam, code, bedrag = 0):
        self.naam = naam
        self.code = code
        self.bedrag = bedrag

    def storten(self, add):
        self.bedrag += add

    def afhalen(self, bedrag):
        self.bedrag -= bedrag

    def __str__(self) -> str:
        return (f"{self.naam}, {self.code}, bedrag: {self.bedrag}")

    def __repr__(self) -> str:
        return f"BankRekening('{self.naam}', '{self.code}', {self.bedrag})"
