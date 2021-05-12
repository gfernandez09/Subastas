from Puja import Puja
from Usuari import Usuari


class Subasta:
    def __init__(self, nomProducte, usuariPropietari):
        self.nomProducte = nomProducte
        self.usuariPropietari = usuariPropietari
        self.estat = True
        self.licitacions = []
        self.licitacioMajor = Puja(Usuari, 0)

    def setNomProducte(self, NomProducteNou):
        self.nomProducte = NomProducteNou

    def getNomProducte(self):
        return self.nomProducte

    def getUsuariPropietari(self):
        return self.usuariPropietari

    def getLicitacioMajor(self):
        return self.licitacioMajor

    def setLicitacioMajor(self, mayorlicitacio):
        self.licitacioMajor = mayorlicitacio

    def getLicitacions(self):
        return self.licitacions

    def licitar(self, Usuario, credit):
        if self.estat:
            if Usuario.getCredit() > credit:
                if Usuario.getNom() != self.usuariPropietari:
                    if credit > self.getLicitacioMajor().getQuantitatOferida():
                        puja = Puja(Usuario, credit)
                        self.setLicitacioMajor(puja)
                        self.licitacions.append(puja)
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def licitarUsuari(self, Usuario):
        if self.licitacioMajor == Puja:
            if Usuario.getCredit() > self.licitacioMajor:
                puja = Puja(Usuario, self.licitacioMajor.getQuantitatOferida() + 1)
                self.setLicitacioMajor(puja)
                self.licitacions.append(puja)
            else:
                return False
        else:
            puja = Puja(Usuario, 1)
            self.setLicitacioMajor(puja)
            self.licitacions.append(puja)
            return True

    def executar(self):
        if not self.estat:
            return False
        else:
            self.estat = False
            self.licitacioMajor.getUsuari().decrementarCredit(self.licitacioMajor.getQuantitatOferida())
            self.usuariPropietari.incrementarCredit(self.licitacioMajor.getQuantitatOferida())
            return True

    def __str__(self):
        return str(self.nomProducte) + ", licitacio creada per l'usuari: " + str(self.getUsuariPropietari())
