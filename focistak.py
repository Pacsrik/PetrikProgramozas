from typing import List
import math


class Focista:
    def __init__(self, nev, poszt, jatszott_meccsek, rugott_golok) -> None:
        self.nev = nev
        self.poszt = poszt
        self.jatszott_meccsek = jatszott_meccsek
        self.rugott_golok = rugott_golok

    def __str__(self):
        return f"{self.nev}, {self.poszt}, {self.jatszott_meccsek}, {self.rugott_golok}"


focistak: List[Focista] = []


def beolvasas():
    f = open("zfk.txt", "r", encoding="UTF-8")
    for sor in f:
        reszek = sor.strip().split(';')
        if len(reszek) == 4:  
            nev = reszek[0]
            poszt = str(reszek[1])
            jatszott_meccsek = int(reszek[2])
            rugott_golok = int(reszek[3])

            obj = Focista(nev, poszt, jatszott_meccsek, rugott_golok)
            focistak.append(obj)
    f.close()
    for item in focistak:
        print(item)

def f1():
    hatved = 0
    for item in focistak:
        if item.poszt == "hátvéd":
            hatved += 1

    print(f"1.feladat: Összesen {hatved} db hátvéd adatait tárolja a fájl.")

def f2():
    golok = 0
    db = 0
    for item in focistak:
        if item.rugott_golok >= 0:
            golok += item.rugott_golok
            db += 1

    print(f"2.feladat: Átlagosan {golok/db} gólt rúgtak a focisták.")

def f3():
    meccs = 0
    gol = 0
    
    for item in focistak:
        if item.nev == "Marci":
            meccs += item.jatszott_meccsek
            gol += item.rugott_golok

    print(f"3.feladat: Marci {meccs} meccsen {gol} gólt rúgott.")

def f4():
    nevek = []
    db = 0
    for item in focistak:
        if item.jatszott_meccsek >= 10:
            db += 1
            nevek.append(item.nev)

    if db > 0:
        print(f"4.feladat: Van olyan aki legalább 10 mecccsen játszott")
    else:
        print(f"4.feladat: Nincs olyan aki legalább 10 mecccsen játszott")
    print(f"\tAkik legalább tíz meccsen játszottak: {nevek}")

def f6():
    csatar = 0
    kozeppalyas = 0
    hatved = 0
    kapus = 0

    for item in focistak:
        if item.poszt == "csatár":
            csatar += item.rugott_golok
        elif item.poszt == "középpályás":
            kozeppalyas += item.rugott_golok
        elif item.poszt == "hátvéd":
            hatved += item.rugott_golok
        elif item.poszt == "kapus":
            kapus += item.rugott_golok

    print("6.feladat: Gólok posztonként")
    print(f"\tCsatár gólok: {csatar} gól")
    print(f"\tKözéppályás gólok: {kozeppalyas} gól")
    print(f"\tHátvéd gólok: {hatved} gól")
    print(f"\tKapus gólok: {kapus} gól")

def f7():
    csatar = []
    kozeppalyas = []
    hatved = []
    kapus = []

    for item in focistak:
        if item.poszt == "csatár":
            csatar.append(item.nev)
        elif item.poszt == "középpályás":
            kozeppalyas.append(item.nev)
        elif item.poszt == "hátvéd":
            hatved.append(item.nev)
        elif item.poszt == "kapus":
            kapus.append(item.nev)

    print("7.feladat: Posztok")
    print(f"\tKapus: {kapus}")
    print(f"\tHátvéd: {hatved}")
    print(f"\tKözéppályás: {kozeppalyas}")
    print(f"\tCsatár: {csatar}")

def main():
    beolvasas()
    f1()
    f2()
    f3()
    f4()

    f6()
    f7()
main()