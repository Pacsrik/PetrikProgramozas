""" 
def f1():
    szoveg = input("Adjon meg egy szöveget: ")
    szoveg2 = (("Princz ") + szoveg)
    ujszoveg = szoveg2
    print(ujszoveg)
    
    szoszam = len(ujszoveg.split())
    print(szoszam)

    keresztnev = "Patrik"
    betuk = len(keresztnev)
    print(betuk)
    


def main():
    f1()

main()
"""

""" 
def f2():
    vezeteknev = "Princz"
    keresztnev = "Patrik"
    elso = [word[0] for word in vezeteknev.split()]
    print(elso)
    utolso = [word[-1] for word in keresztnev.split()]
    print(utolso)
    if elso == utolso:
        print("A két betű megegyezik!")
    else: 
        print("A két betű nem egyezik meg!")

f2()

def main():
    f2()

main() 
"""

""" 
def f3():
    vezeteknev = "Princz"
    keresztnev = "Patrik"
    teljes = vezeteknev + keresztnev
   

    elso = teljes.count("P")
    masodik = teljes.count("r")
    print("A vezetékneved első betűje ennyiszer fordul elő a teljes nevedben:", elso)
    print("A vezetékneved második betűje ennyiszer fordul elő a teljes nevedben:", masodik)

def main():
    f3()

main() 
"""




""" 
def f4():
   keresztnev = "Patrik"
   vezeteknev = "Princz"
   teljes = vezeteknev + keresztnev

   print(teljes.swapcase())

def main():
    f4()

main()
"""

""" 
def f5():
    keresztnev = "Patrik"
    masodik = keresztnev[1]
    torles = keresztnev.replace(masodik,"")
    print(torles)

def main():
    f5()

main()
"""
""" 
def f6():
    vezeteknev = "Princz"
    maganhangzok = ['a', 'á', 'e', 'é', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű', 'i', 'í']
    for maganhangzo in maganhangzok:
        vezeteknev = vezeteknev.replace(maganhangzo, 'é')
    print(vezeteknev)

def main():
    f6()

main()
"""
""" 
def f7():
    keresztnev = "Patrik"

    if "am" in keresztnev:
        print("Szerepel az 'am' szócska a nevedben!")
    else:
        print("Nem szerepel az 'am' szócska a nevedben!")

def main():
    f7()

main()
"""
