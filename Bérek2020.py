from typing import List
import math


class Berek:
    def __init__(self, nev, neme, reszleg, belepes, ber):
        self.nev = nev
        self.neme = neme
        self.reszleg = reszleg
        self.belepes = belepes
        self.ber = ber

    def __str__(self):
        return f"{self.nev}, {self.neme}, {self.reszleg}, {self.belepes}, {self.ber}"


lista: List[Berek] = []


def beolvasas():
    f = open("berek2020.txt", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split(';')
        nev = reszek[0]
        neme = reszek[1]
        reszleg = reszek[2]
        belepes = int(reszek[3])
        ber = int(reszek[4])

        obj = Berek(nev, neme, reszleg, belepes, ber)
        lista.append(obj)
    f.close()


def f3():
    global osszeg
    osszeg = 0

    for item in lista:
        if item.ber >= 0:
            osszeg += 1

    print("3.feladat: Dolgozók száma:", osszeg, "fő")


def f4():
    ossz = 0
    for item in lista:
        if item.ber >= 0:
            ossz += item.ber

    a = round(ossz/osszeg/1000, 1)
    print("4.feladat: Bérek átlaga", a, "eFt")


def f5():
    global beker
    beker = input("Kérem egy részleg nevét: ")


def f6():

    legmagasabb = 0
    dolgozo = None

    for item in lista:

        fizetes = item.ber
        reszleg = item.reszleg

        if reszleg == beker and fizetes > legmagasabb:
            legmagasabb = fizetes
            dolgozo = item

    if dolgozo:
        print("6.feladat: A legtöbbet kereső dolgozó a megadott részlegen")
        print(f'Neve: {dolgozo.nev}')
        print(f'Neme: {dolgozo.neme}')
        print(f'Belépés: {dolgozo.belepes}')
        print(f'Bér: {dolgozo.ber} Forint')
    else:
        print("6.feladat: A megadott részleg nem létezik a cégnél!")


def f7():
    print("7.feladat: Statisztika")

    beszerzes = 0
    penzugy = 0
    asztalosmuhely = 0
    ertekesites = 0
    lakatosmuhely = 0
    karbantartas = 0
    szerelomuhely = 0
    szemelyzeti = 0

    for item in lista:
        if item.reszleg == "beszerzés":
            beszerzes += 1
        elif item.reszleg == "pénzügy":
            penzugy += 1
        elif item.reszleg == "asztalosműhely":
            asztalosmuhely += 1
        elif item.reszleg == "értékesítés":
            ertekesites += 1
        elif item.reszleg == "lakatosműhely":
            lakatosmuhely += 1
        elif item.reszleg == "karbantartás":
            karbantartas += 1
        elif item.reszleg == "szerelőműhely":
            szerelomuhely += 1
        elif item.reszleg == "személyzeti":
            szemelyzeti += 1

    print("beszerzés -", beszerzes, "fő")
    print("pénzügy -", penzugy, "fő")
    print("asztalosműhely -", asztalosmuhely, "fő")
    print("értékesítés -", ertekesites, "fő")
    print("lakatosműhely -", lakatosmuhely, "fő")
    print("karbantartás -", karbantartas, "fő")
    print("szerelőműhely -", szerelomuhely, "fő")
    print("személyzeti -", szemelyzeti, "fő")


def main():
    beolvasas()
    f3()
    f4()
    f5()
    f6()
    f7()


main()
