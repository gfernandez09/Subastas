from Usuari import Usuari
from Subasta import Subasta


class Test:
    Toni = Usuari("Toni", 100)
    Pep = Usuari("Pep", 150)
    Enric = Usuari("Enric", 300)
    s1 = Subasta("Telefon Movil", Toni)
    print(str(s1.licitar(Pep, 100)))
    print(str(s1.getLicitacioMajor()))

    print(str(s1.licitar(Enric, 50)))
    print(str(s1.getLicitacioMajor()))
    print(str(s1.executar()))

    print(str(s1.licitar(Enric, 200)))
    s2 = Subasta("Impresora 3D", Pep)
    print(str(s2.licitarUsuari(Enric)))
    print(str(s2.executar()))

    usuaris = [Toni, Pep, Enric]
    for usuari in usuaris:
        print("Usuari: " + str(usuari))
        print("Crèdit actual de l'usuari " + str(usuari.getCredit()))
    licitacions = [s1, s2]
    for licitacio in licitacions:
        print(licitacio)
