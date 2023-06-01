from typing import List


class Csapatok:
    def __init__(self, csapat, helyezes, valtozas, pontszam):
        self.csapat = csapat
        self.helyezes = helyezes
        self.valtozas = valtozas
        self.pontszam = pontszam

    def __str__(self):
        return f"{self.csapat}, {self.helyezes}, {self.valtozas}, {self.pontszam}"

lista: List[Csapatok] = []

def beolvasas():
    f = open("fifa.txt", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split(';')
        csapat = reszek[0]
        helyezes = reszek[1]
        valtozas = reszek[2]
        pontszam = int(reszek[3])
        

        obj = Csapatok(csapat, helyezes, valtozas, pontszam)
        lista.append(obj)
    f.close()
    

    

def f3():
    print("3.feladat: A világranglistán", len(lista), "csapat szerepel")

def f4():

    pontok = 0
    csapatok = len(lista)

    for item in lista:
        if item.pontszam >0:
            pontok += item.pontszam

    print("4.feladat: A csapatok átlagos pontszáma: ",pontok/csapatok ,"pont")

def f5():
    maximum = lista[0]
    for item in lista:
        if item.valtozas >maximum.valtozas:
            maximum = item

    print("5.feladat: A legtöbbet javító csapat")
    print("\t Helyezés:", maximum.helyezes)
    print("\t Csapat:", maximum.csapat)
    print("\t Pontszám:", maximum.pontszam)

def f6():
    for item in lista:
        if item.csapat == "Magyarország":
            print("6.feladat: A csapatok között van Magyarország")
            break
        else:
            print("6.feladat: A csapatok között nincs Magyarország")         
            break 

def f7():

    print("7.feladat: Statiszika")
    csapatok = {}

    for item in lista:
        kulcs = item.valtozas
        if kulcs not in csapatok:
            csapatok[kulcs] = 0
        csapatok[kulcs] += 1
        
    for item in csapatok:
        if csapatok[item] > 1:
            print(f"\t {item} helyet változott: {csapatok[item]} csapat")


def main():
    beolvasas()
    f3()
    f4()
    f5()
    f6()
    f7()

main()
