class Usuari:
    def __init__(self, nom, credit):
        self.__nom = nom
        self.credit = credit

    def incrementarCredit(self, quantitat):
        self.credit += quantitat

    def decrementarCredit(self, quantitat):
        self.credit -= quantitat

    def getNom(self):
        return self.__nom

    def getCredit(self):
        return self.credit

    def setCredit(self, credit):
        self.credit = credit

    def __str__(self):
        return str(self.__nom)
