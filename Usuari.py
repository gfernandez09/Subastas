class Usuari:
    # Constructor.
    def __init__(self, nom, credit):
        self.__nom = nom
        self.credit = credit
    
    # Método incrementar Credito.
    def incrementarCredit(self, quantitat):
        self.credit += quantitat
    
    # Método decrementar Credito.
    def decrementarCredit(self, quantitat):
        self.credit -= quantitat
    
    # Getters & Setters.
    def getNom(self):
        return self.__nom

    def getCredit(self):
        return self.credit

    def setCredit(self, credit):
        self.credit = credit
    
    # Str de la clase.
    def __str__(self):
        return str(self.__nom)
