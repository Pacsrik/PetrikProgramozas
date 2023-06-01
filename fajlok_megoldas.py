# 1. Írjuk ki a számokat 10-től 100-ig tízesével egy szamok.txt fájlba, minden számot új sorba! Használj kontext managert!
def f1():
    with open("szamok.txt", "w") as f:
        for i in range (10, 101, 10):
            f.write(str(i)+"\n")

# 2. Fűzzünk hozzá a szamok.txt tartalmához, a végére, a 110 számot.

def f2():
    with open("szamok.txt", "a") as f:
        f.write(str(110)+"\n")

# 3. Olvassuk be a szamok.txt tartalmát egy szamok nevű, egész számokat tartalmazó listába! Használjunk kontext managert!
# Majd írassuk ki a lista tartalmát a konzolra!

szamok = []
def f3():
    
    with open("szamok.txt") as f:
        for line in f:
            szamok.append(int(line))
    print(szamok)

# 4. Adjuk össze a lista elemei közül a 20-al maradék nélkül oszthatókat, és az eredményt írjuk a konzolra
def f4():
    osszeg = 0
    for elem in szamok:
        if elem%20 == 0:
            osszeg += elem
    print("A 20-al maradék nélkül oszthatók összege:", osszeg)        


# 5. Kérjünk be a felhasználótól n számot, és írassuk ki egy szamok2.txt fájlba a bekért egész számokat.
def f5():
    with open("szamok2.txt", "w") as f:
        n= int(input("Elemszám: "))
        for i in range(n):
            szam = int(input("Kérem a következő egész számot: "))
            f.write(str(szam)+"\n")

# 6. Olvassuk be a szamok2.txt tartalmát egy egész típusú listába.
lista = []

def f6():
    with open("szamok2.txt", "r") as f:
        for line in f:
            lista.append(int(line))
        print(lista)

# 7. Melyik a legkisebb elem a listában, és hányadik index pozíción található?
def f7():
    min = lista[0]
    idx = 0
    for i in range(0, len(lista)):
        if lista[i]<min:
            min=lista[i]
            idx = i
    print(f"Legkisebb elem: {min}, indexe: {idx}")

# 8. Melyik a legnagyobb elem a listában, és hányadik index pozíción található?
def f8():
    max = lista[0]
    idx = 0
    for i in range(0, len(lista)):
        if lista[i]>max:
            max=lista[i]
            idx = i
    print(f"Legnagyobb elem: {max}, indexe: {idx}")

# 9. Monoton növekvő sorrendben vannak-e az elemek a listában? 
# (Monoton növekvő a lista, ha minden elemre igaz, hogy az őt követő elem nem kisebb nála.)

def f9():
    novekvo = True
    for i in range(0,len(lista)-1):
        if lista[i]>lista[i+1]:
            novekvo = False
    if novekvo == True:
        print("A lista monoton növekvő.") 
    else:
        print("A lista nem monoton növekvő.")  

# 10. Fűzd hozzá a szamok2.txt végére, új sorba, a listában lévő számok összegét!
def f10():
    with open("szamok2.txt", "a") as f:
        osszeg = 0
        for elem in lista:
            osszeg += elem
        f.write(str(osszeg)+"\n")

# 11. A listában lévő számok közül a páros vagy a páratlan számok vannak többen? Egész mondatban válaszolj, válaszod írasd ki a konzolra!
def f11():
    parosDb=0
    paratlanDb=0
    for elem in lista:
        if elem%2==0:
            parosDb += 1
        else:
            paratlanDb += 1

    if parosDb > paratlanDb:
        print("A párosak vannak többen.")
    elif parosDb < paratlanDb:
        print("A páratlanok vannak többen.")
    else:
        print("A párosak és a páratlanok egyenlő számban vannak.")

# 12. Kérj be egy kétjegyű számot, és a számot szöveggel írasd ki egy szoveg.txt nevű fájlba! 
# Pl. ha a bekért szám 23, akkor szövegesen: huszonhárom.

def f12():
    szam = int(input("kérek egy kétjegyű számot: "))
    szamstr = str(szam)
    print(f"első számjegy: {szamstr[0]}, második: {szamstr[1]}")
    szoveg1 = ""
    szoveg2 = ""
    if szamstr[0] == "1":
        szoveg1 = "tizen"
    elif szamstr[0] == "2":
        szoveg1 = "huszon"
    elif szamstr[0] == "3":
        szoveg1 = "harminc"
    elif szamstr[0] == "4":
        szoveg1 = "negyven"
    elif szamstr[0] == "5":
        szoveg1 = "ötven"
    elif szamstr[0] == "6":
        szoveg1 = "hatvan"
    elif szamstr[0] == "7":
        szoveg1 = "hetven"
    elif szamstr[0] == "8":
        szoveg1 = "nyolcvan"
    elif szamstr[0] == "9":
        szoveg1 = "kilencven"
    
    if szamstr[0] == "1" and szamstr[1] == "0":
        szoveg1 = "tíz"

    if szamstr[0] == "2" and szamstr[1] == "0":
        szoveg1 = "húsz"

    if szamstr[1] == "1":
        szoveg1 += "egy"
    elif szamstr[1] == "2":
        szoveg1 += "kettő"
    elif szamstr[1] == "3":
        szoveg1 += "három"
    elif szamstr[1] == "4":
        szoveg1 += "négy"
    elif szamstr[1] == "5":
        szoveg1 += "öt"
    elif szamstr[1] == "6":
        szoveg1 += "hat"
    elif szamstr[1] == "7":
        szoveg1 += "hét"
    elif szamstr[1] == "8":
        szoveg1 += "nyolc"
    elif szamstr[1] == "9":
        szoveg1 += "kilenc"

    with open("szoveg.txt", "w", encoding="utf-8") as f:
        f.write(szoveg1)

# 13. Egy héten minden nap leolvassuk a hőmérséklet értéket, és ezeket rögzítjük egy homero.txt nevű fájlba. 
# A szövegfájlból olvasd be egy listába a hét hőmérséklet adatot, és számítsd ki az átlagukat,
# és írasd ki ezt az átlagot a konzolra 2 tizedesjegy pontossággal.

def f13():
    with open("homero.txt","w") as f:
        for i in range(7):
            homerseklet = int(input("kérem a következő hőmérséklet értéket:")) 
            f.write(str(homerseklet)+"\n")
    
    homero = []
    with open("homero.txt", "r") as f:
        for line in f:
            homero.append(int(line))

    osszeg = 0
    for elem in homero:
        osszeg += elem
    atlag = round(osszeg/len(homero),2)

    print("A hőmérsékletek átlaga:", atlag )

def main():
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    f9()
    f10()
    f11()
    f12()
    f13()

main()    