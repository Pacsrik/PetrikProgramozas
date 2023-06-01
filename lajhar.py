from typing import List


class Lajhar:
    def __init__(self, nev, kor, tomeg, nem, utodok_db):
        self.nev = nev
        self.kor = kor
        self.tomeg = tomeg
        self.nem = nem
        self.utodok_db = utodok_db
    
    def __str__(self):
        return f"{self.nev}, {self.kor}, {self.tomeg}, {self.nem}, {self.utodok_db}"

lajharok:List[Lajhar] = []
with open("lajhar.txt", "r", encoding="utf-8") as f: 
    
    elso_sor = True
    for sor in f: 

        adatok = sor.strip().split(';') 
        
        if elso_sor == True :
             elso_sor = False
             continue

        peldany = Lajhar(adatok[0], int(adatok[1]), float(adatok[2]), adatok[3], int(adatok[4])) 
        lajharok.append(peldany) 

    for elem in lajharok: 
        print(elem)


def f1():
    nostenyek = 0
    for item in lajharok:
        if item.nem == "nosteny":
            nostenyek += 1
    print(nostenyek, "darab nőstény van!")

def f2():
    nebulok = 0
    for item in lajharok:
        if item.nem == "him":
            nebulok += item.utodok_db
    print(nebulok,"darab gyerekük van a hímeknek!")

def f3():
    for item in lajharok:
        if item.utodok_db > 0:
            print(item.nev)

def f4():
    nosteny = 0
    him = 0
    for item in lajharok:
        if item.nem == "him":
            him += 1
        elif item.nem =="nosteny":
            nosteny += 1
    if nosteny == him:
        print("Minden hímnek jut nöstény!")
    else: 
        print("Nem jut minden hímnek nőstény!")

def f5():
    him = 0
    nosteny = 0
    him_db = 0
    nosteny_db = 0
    for item in lajharok:
        if item.nem == "him":
            him += item.tomeg
        elif item.nem == "nosteny":
            nosteny += item.tomeg
    for item in lajharok:
        if item.nem == "him":
            him_db += 1
        elif item.nem =="nosteny":
            nosteny_db += 1

    him_atlag = him/him_db
    nosteny_atlag = nosteny/nosteny_db

    print(round(him_atlag), " kg a hímek átlagos testtömege!")
    print(round(nosteny_atlag), " kg a nőstények átlagos testtömege!")

def f6():
    him = 0
    nosteny = 0
    him_db = 0
    nosteny_db = 0
    for item in lajharok:
        if item.nem == "him":
            him += item.tomeg
        elif item.nem == "nosteny":
            nosteny += item.tomeg
    for item in lajharok:
        if item.nem == "him":
            him_db += 1
        elif item.nem =="nosteny":
            nosteny_db += 1
    
    him_atlag = him/him_db
    nosteny_atlag = nosteny/nosteny_db

    if him_atlag > nosteny_atlag:
        print("A hímek súlyosabbak!")
    else:
        print("A nőstények súlyosabbak!")

            
def main():
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
main()