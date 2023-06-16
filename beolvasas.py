from typing import List
import math


class Class_neve:
    def __init__(self, adat1, adat2, adat3, adat4):
        self.adat1 = adat1
        self.adat2 = adat2
        self.adat3 = adat3
        self.adat4 = adat4

    def __str__(self):
        return f"{self.adat1}, {self.adat2}, {self.adat3}, {self.adat4}"


lista: List[Class_neve] = []


def beolvasas():
    f = open("beolvasando fájl.txt/.csv stb.", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split('amivel el vannak választva az adatok, pl.: ;')
        adat1 = reszek[0]
        adat2 = reszek[1]  #Ha az adat szám, akkor int()-be kell írni!
        adat3 = reszek[2]
        adat4 = reszek[3]


        obj = Class_neve(adat1, adat2, adat3, adat4)
        lista.append(obj)
    f.close()
    #Ellenőrzés: for item in list:
                    #print(item)


def main():
    beolvasas()

main()