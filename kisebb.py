def beker_1():
    global szam1    
    proba_szamlalo = 0
    while True:
        if proba_szamlalo == 0:
            szam1 = int(input("Kérem adja meg a/az első negatív számot:\n"))
        else:
            szam1 = int(input("Ez nem negatív szám! Kérem adja meg még egyszer a/az első negatív számot:\n"))

        proba_szamlalo += 1
        if szam1<0:
            if proba_szamlalo > 1:
                print(f"{proba_szamlalo}. beírt szám lett a jó!")
            break;

def beker_2():
    global szam2
    proba_szamlalo = 0
    while True:
        if proba_szamlalo == 0:
            szam2 = int(input("Kérem adja meg a/az második negatív számot:\n"))
        else:
            szam2 = int(input("Ez nem negatív szám! Kérem, adja meg még egyszer a/az második negatív számot:\n"))

        proba_szamlalo += 1
        if szam2<0:
            if proba_szamlalo > 1:
                print(f"{proba_szamlalo}. beírt szám lett a jó!")
            break;

def melyik_kisebb():
    if szam1<szam2:
        print(f"A kisebb szám: {szam1}")
    elif szam2<szam1:
        print(f"A kisebb szám: {szam2}")
    else:
        print(f"A két szám egyenlő.")  


def main():
    beker_1()
    beker_2()
    melyik_kisebb()

main()



