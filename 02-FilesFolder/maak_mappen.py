import io, os
bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline()

while tekst_regel:
    mapnaam = tekst_regel
    lengte_mapnaam = len(mapnaam)
    tekst_regel = tekst_regel.strip()
    print(tekst_regel)
    tekst_regel = bestand.readline()

    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)

    
