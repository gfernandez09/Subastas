class Puja:

    def __init__(self, Usuari, quantitatOferida):
        self.Usuari = Usuari
        self.quantitatOferida = quantitatOferida

    def getUsuari(self):
        return self.Usuari

    def getQuantitatOferida(self):
        return self.quantitatOferida

    def __str__(self):
        return str(self.Usuari) + ", " + str(self.quantitatOferida)
