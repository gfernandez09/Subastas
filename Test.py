from Usuari import Usuari
from Subasta import Subasta


# Creacion clase Test para probar el programa.
class Test:
    # Creación de Usuarios
    Toni = Usuari("Toni", 100)
    Pep = Usuari("Pep", 150)
    Enric = Usuari("Enric", 300)
    # Creación Primera Subasta
    s1 = Subasta("Telefon Movil", Toni)
    print(str(s1.licitar(Pep, 100)))
    print(str(s1.getLicitacioMajor()))

    print(str(s1.licitar(Enric, 50)))
    print(str(s1.getLicitacioMajor()))
    print(str(s1.executar()))

    print(str(s1.licitar(Enric, 200)))
    # Creación Segunda Subasta
    s2 = Subasta("Impresora 3D", Pep)
    print(str(s2.licitarUsuari(Enric)))
    print(str(s2.executar()))
    # Bucle para recorrer los Usuarios y ver su credito actual
    usuaris = [Toni, Pep, Enric]
    for usuari in usuaris:
        print("Usuari: " + str(usuari))
        print("Crèdit actual de l'usuari " + str(usuari.getCredit()))
    # Bucle para recorrer las subastas y ver también sus usuarios propietarios.
    licitacions = [s1, s2]
    for licitacio in licitacions:
        print(licitacio)
