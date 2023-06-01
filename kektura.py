from typing import List


class Szakasz:
    def __init__(self, kiindulo_nev, vegpont_nev, hossz, emelkedes, lejtes, pecsetelo):
        self.kiindulo_nev = kiindulo_nev
        self.vegpont_nev = vegpont_nev
        self.hossz = hossz
        self.emelkedes = emelkedes
        self.lejtes = lejtes
        self.pecsetelo = pecsetelo

    def __str__(self):
        return f"{self.kiindulo_nev}, {self.vegpont_nev}, {self.hossz}, {self.emelkedes}, {self.lejtes}, {self.pecsetelo}"


list: List[Szakasz] = []


def beolvasas():
    with open("kektura.csv", "r", encoding="utf-8") as f:
        elsosor = f.readline()
        adatok0 = elsosor.strip().split(';')
        global kezdomagassag
        kezdomagassag = int(adatok0[0])

        for sor in f:
            adatok = sor.strip().split(';')
            peldany = Szakasz(adatok[0], adatok[1], float(
                adatok[2]), int(adatok[3]), int(adatok[4]), adatok[5])
            list.append(peldany)

        for item in list:
            print(item)


def f3():
    szakaszok = len(list)
    print(f"3.feladat: Szakaszok száma: {szakaszok} db")


def f4():
    teljes = 0
    for item in list:
        if item.hossz > 0:
            teljes += item.hossz

    print(f"4.feladat: A túre teljes hossza {round(teljes,3)} km")


def f5():
    minimum = list[0].hossz
    kezdet = list[0].kiindulo_nev
    veg = list[0].vegpont_nev

    for item in list:
        if item.hossz < minimum:
            minimum == item.hossz
            kezdet == item.kiindulo_nev
            veg = item.vegpont_nev

    print(f"5.feladat: A legrövidebb szakasz adatai:")
    print(f"\tKezdete: {kezdet}")
    print(f"\tVége: {veg}")
    print(f"\tTávolság: {minimum} km")


def HianyosNev(vegpont):
    for item in list:
        if item.vegpont_nev == vegpont:
            if "pecsetelohely" not in item.vegpont_nev and item.pecsetelo == "i":
                return True

    return False


def f7():
    print("7.feladat: Hiányos állmásnevek:")
    hianyosNevVan = False
    for item in list:
        if HianyosNev(item.vegpont_nev) == True:
            print(f"\t{item.vegpont_nev}")
            hianyosNevVan = True

    if hianyosNevVan == False:
        print("Nincs hiányos állomásnév!")


def f8():
    maximum = kezdomagassag + list[0].emelkedes - list[0].lejtes
    veg = list[0].vegpont_nev
    print(f"8.feladat: A túra legmagasabban fekvő végpontja:")
    aktmagassag = kezdomagassag
    for item in list:
        aktmagassag += item.emelkedes - item.lejtes
        if aktmagassag > maximum:
            maximum = aktmagassag
            veg = item.vegpont_nev

    print(f"\tA végpont neve: {veg}")
    print(f"\tA végpont tengerszint feletti magassága: {maximum} m")


def f9():
    with open("kektura2.csv", "w", encoding="utf-8") as f:
        for item in list:
            if HianyosNev(item.vegpont_nev) == False:
                f.write(
                    f"{item.kiindulo_nev}; {item.vegpont_nev}; {item.hossz}; {item.emelkedes}; {item.lejtes}; {item.pecsetelo}\n")
            else:
                f.write(
                    f"{item.kiindulo_nev}; {item.vegpont_nev} pecsetelohely; {item.hossz}; {item.emelkedes}; {item.lejtes}; {item.pecsetelo}\n")


def f10():
    ossz = 0
    for item in list:
        if item.lejtes > item.emelkedes:
            ossz += 1

    print(
        f"10.feladat: Szakaszok száma, ahol lefelé többet kell menni, mint felfelé: {ossz} db")
    if ossz == 0:
        print("Nincs olyan szakasz, ahol összességében többet kell lefelé menni, mint felfelé.")


def f11():
    ossz = 0
    for item in list:
        if item.pecsetelo == "i":
            ossz += 1

    if ossz > 0:
        print(f"11.feladat: Pecsételőhelyek száma: {ossz} db")
    else:
        print("Nincs pecsételőhely!")


def main():
    beolvasas()
    f3()
    f4()
    f5()
    f7()
    f8()
    f9()
    f10()
    f11()


main()
