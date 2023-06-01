from typing import List


class Hegyek:
    def __init__(self, neve, hegyseg, magassag):
        self.neve = neve
        self.hegyseg = hegyseg
        self.magassag = magassag
        

    def __str__(self):
        return f"{self.neve}, {self.hegyseg}, {self.magassag}"
    
    def lab(self):
        return self.magassag*3.280839895

lista: List[Hegyek] = []

def beolvasas():
    f = open("hegyekMo.txt", "r", encoding="UTF-8")
    
    f.readline()
    for sor in f:
        global reszek
        reszek = sor.strip().split(';')
        neve = reszek[0]
        hegyseg = reszek[1]
        magassag = int(reszek[2])
        
        obj = Hegyek(neve, hegyseg, magassag)
        lista.append(obj)
    f.close()

def f3():
    a = 0
    for item in lista:
        if item.magassag >= 0:
            a += 1

    print("3.feladat: Hegycsúcsok száma:",a,"db")

def f4():
    magassag = 0
    hegyek = 0
    for item in lista:
        if item.magassag >= 0:
            magassag += item.magassag
        if item.magassag >= 0:
            hegyek += 1

    atlag = magassag/hegyek
    print("4.feladat: Hegycsúcsok átlagos magassága:", atlag, "m")


def f5():
    maximum = lista[0]
    for item in lista:
        if item.magassag >maximum.magassag:
            maximum = item

    print("5.feladat: A legmagasabb hegycsúcs adatai:")
    print("\t Név:", maximum.neve)
    print("\t Hegység:", maximum.hegyseg)
    print("\t Magasság:", maximum.magassag,"m")

def f6():
    bekert = int(input("6.feladat: Kérek egy magasságot:"))
    for item in lista:
        if item.magassag >= bekert:
            print("Van",bekert,"m-nél magasabb hegycsúcs a Börzsönyben!")
            break
        else:
            print("Nincs",bekert,"m-nél magasabb hegycsúcs a Börzsönyben!")
            break

def f7():
    magassag = 0
    for item in lista:
        if item.magassag*3.280839895 > 3000:
            magassag += 1

    print("7.feladat: 3000 lábnál magasabb hegycsúcsok száma:",magassag)

def f8():
    print("8.feladat: Hegység statiszika")
    hegyek = {}

    for item in lista:
        kulcs = item.hegyseg
        if kulcs not in hegyek:
            hegyek[kulcs] = 0
        hegyek[kulcs] += 1
        
    for item in hegyek:
        if hegyek[item] > 1:
            print(f"\t {item} - {hegyek[item]} db")

def f9():
    print("9.feladat: bukk-videk.txt")
    
    f=open("bukk-videk.txt","w",encoding="UTF-8")
    f.write(f"Hegycsúcs neve;Magasság láb\n")
    for item in lista:
        if item.hegyseg == "Bükk-vidék":
            f.write(f"{item.neve};{round(item.lab(),1)}\n")


def main():
    beolvasas()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    f9()

main()