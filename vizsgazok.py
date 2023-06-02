from typing import List
import random

class Vizsga:
    def __init__(self, nev, nem, jegy):
        self.nev = nev
        self.nem = nem
        self.jegy = jegy
      
    def __str__(self):
        return f"{self.nev}, {self.nem}, {self.jegy}"


list: List[Vizsga] = []


def beolvasas():
    f = open("vizsga.txt", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split(';')
        nev = reszek[0]
        nem = reszek[1]
        jegy = int(reszek[2])

        obj = Vizsga(nev, nem, jegy)
        list.append(obj)
    f.close()

def f1():
    global pontszam
    pontszam = int(input("1.feladat: Adja meg a vizsgán elért pontszámát: "))

def f2():
    if pontszam >= 0 and pontszam <= 19:
        print(f"2.feladat: Az elért osztályzat: 1")
    elif pontszam >= 20 and pontszam <= 39:
        print(f"2.feladat: Az elért osztályzat: 2")
    elif pontszam >= 40 and pontszam <= 59:
        print(f"2.feladat: Az elért osztályzat: 3")
    elif pontszam >= 60 and pontszam <= 79:
        print(f"2.feladat: Az elért osztályzat: 4")
    elif pontszam >= 80:
        print(f"2.feladat: Az elért osztályzat: 5, a legjobb jegyet kapta")
        
    if pontszam >= 0 and pontszam < 20:
        hianyzo_pont = 20 - pontszam
    elif pontszam >= 20 and pontszam < 40:
        hianyzo_pont = 40 - pontszam
    elif pontszam >= 40 and pontszam < 60:
        hianyzo_pont = 60 - pontszam
    elif pontszam >= 60 and pontszam < 80:
        hianyzo_pont = 80 - pontszam
    else:
        hianyzo_pont = 0  
    print(f"\t Legalább {hianyzo_pont} pont kellett volna a jobb jegyhez.")

list2 = []
def f3():
    with open('jegyek.txt', 'r') as file:
        for line in file:
            list2.append(int(line.strip()))
    print(f"3.feladat: A lista elemei: {list2}")

def f4():
    randomka = random.randint(1,6)
    print(f"4.feladat: A list random generált, {randomka+1}. eleme: {list2[randomka]}")

def atlag():
    global atlag2
    hanyan = len(list2)
    ossz = 0
    for item in list2:
        ossz += item
    atlag2 = round(ossz/hanyan,2)
    
    print(f"5.feladat: A vizsgázók eredményeinek átlaga, 2 tizedesre kerekítve: {round(ossz/hanyan,2)}")

def atlag_felett():
    jegy = int(input("6.feladat: Adjon meg egy érdemjegyet: "))
    if jegy > atlag2:
        return True
    else:
        return False

def f7():
    jegy = 3
    if jegy > atlag2:
         print("7.feladat: A 3-as érdemjegy nagyobb, mint az átlag.")
    else:
        print("7.feladat: A 3-as érdemjegy nem nagyobb, mint az átlag.")
def f8():
    print("8.feladat: Vizsga nevű osztály")

def f9():
    print("9.feladat: Tárolás adatszerkezetben")

def f10():
    print(f"10.feladat: A vizsgázók száma: {len(list)} fő")

def f11():
    hany = 0
    for item in list:
        if item.nem == "lany" and item.jegy == 1:
            hany += 1

    print(f"11.feladat: A lány vizsgázók száma, akik 1-est kaptak: {hany}")

def main():
    beolvasas()
    f1()
    f2()
    f3()
    f4()
    atlag()
    atlag_felett()
    f7()
    f8()
    f9()
    f10()
    f11()


main()
