from typing import List


class Versenyzo:
    def __init__(self, nev, rajtszam, kategoria, versenyido, tavszazalek):
        self.nev = nev
        self.rajtszam = rajtszam
        self.kategoria = kategoria
        self.versenyido = versenyido
        self.tavszazalek = tavszazalek

    def __str__(self):
        return f"{self.nev}, {self.rajtszam}, {self.kategoria}, {self.versenyido}, {self.tavszazalek}"


list: List[Versenyzo] = []


def beolvasas():
    f = open("ub2017egyeni.txt", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split(';')
        nev = reszek[0]
        rajtszam = int(reszek[1])
        kategoria = reszek[2]
        versenyido = reszek[3]
        tavszazalek = int(reszek[4])

        obj = Versenyzo(nev, rajtszam, kategoria, versenyido, tavszazalek)
        list.append(obj)
    f.close()


def f3():
    indulok = len(list)
    print(f"3.feladat: Egyéni indulók: {indulok} fő")


def f4():
    nok = 0
    for item in list:
        if item.kategoria == "Noi" and item.tavszazalek == 100:
            nok += 1

    print(f"4.feladat: Célba érkező női sportolók: {nok} fő")


def f5():
    sportolo = input("5.feladat: Kérem a sportoló nevét: ")
    vanE = "Nem"
    teljesitetteE = "Nem"

    for item in list:
        if item.nev == sportolo:
            vanE = "Igen"
            if item.tavszazalek == 100:
                teljesitetteE = "Igen"
            break

    print(f"\tIndult egyéniben a sportoló? {vanE}")
    if vanE == "Igen":
        print(f"\tTeljesítette a teljes távot? {teljesitetteE}")


def IdőÓrában(versenyido):
    adatok = versenyido.strip().split(':')
    ora = int(adatok[0])
    perc = int(adatok[1])
    mp = int(adatok[2])
    return ora + (perc/60) + (mp/3600)


def f7():
    osszes = 0
    db = 0

    for item in list:
        if item.kategoria == "Ferfi" and item.tavszazalek == 100:
            osszes += IdőÓrában(item.versenyido)
            db += 1

    atlag = osszes/db
    print(f"7.feladat: Átlagos idő: {atlag} óra")


def f8():
    minimum = 1111
    nev = " "
    rsz = 0
    ido = " "

    for item in list:
        if item.kategoria == "Noi" and item.tavszazalek == 100 and IdőÓrában(item.versenyido) < minimum:
            minimum = IdőÓrában(item.versenyido)
            nev = item.nev
            rsz = item.rajtszam
            ido = item.versenyido

    nev2 = " "
    rsz2 = 0
    ido2 = " "

    for item in list:
        if item.kategoria == "Ferfi" and item.tavszazalek == 100 and IdőÓrában(item.versenyido) < minimum:
            minimum = IdőÓrában(item.versenyido)
            nev2 = item.nev
            rsz2 = item.rajtszam
            ido2 = item.versenyido

    print(f"8.feladat: Verseny győztesei")
    print(f"\tNők: {nev} ({rsz}.) - {ido}")
    print(f"\tFérfiak: {nev2} ({rsz2}.) - {ido2}")

def main():
    beolvasas()
    f3()
    f4()
    f5()
    f7()
    f8()


main()
