import math


"""
valos= float(input("Kérek egy valós számot: "))

print("A szám egészre kerekítve:", round(valos))
print("A szám 2 tizedesjegyre kerekítve:", round(valos, 2))

print("A szám abszolútértéke:", abs(valos))

a= int(input("a= "))
b= int(input("b= "))

print(f"A nagyobb szám {a} és {b} közül: {max(a,b)}")
print(f"A kisebb szám {a} és {b} közül: {min(a,b)}")
"""


""" 
#1.feladat 

ar= float(input("Mennyibe kerül egy kiló krupmli?"))
kilo= float(input("Akkor ennyi kilót kérnék:"))

print("Ennyibe fog kerülni:", int(ar*kilo), "Ft")
"""

""" 
#2.feladat

fizetes= float(input("Mennyi a mostani fizetése?"))
emeles= float(input("Hány százalékos a fizetésemelése?")) 

print("Az új fizetése:", int(fizetes*(1+(emeles/100))),"Ft")
"""


""" 
#3.feladat

laptopar = float(input("Mennyibe kerül a laptop?"))
sporolas = float(input("Mennyit pénzt tudsz félrerakni a laptopra egy hónapban?"))

print ((math.ceil(laptopar/sporolas)), "hónapig kell gyűjtened rá a pénzt!" ) 
"""

""" 
#4.feladat

kolcson = float(input("Mennyi kölcsönt vett fel?"))
futamido = float(input("Mennyi a futamidő években?"))

print("Az Ön havi törlesztőrészlete:", round(kolcson/futamido/12), "Ft") 
"""

""" 
#5.feladat

szelesseg = float(input("A szoba szélessége méterben:"))
magassag = float(input("A szoba magassága méterben:"))

csempe_magas = 0.2
csempe_szeles = 0.2
csempe_terulet = (csempe_szeles*csempe_magas)
csempezendo_terulet = (szelesseg*magassag*1.1)
csempe_darab = (csempezendo_terulet/csempe_terulet)
csempe_db = math.ceil(csempezendo_terulet/csempe_terulet)

print(f"{csempe_db} db csempére lesz szükségünk.") 
"""


#6.feladat

ora = float(input("Óra:"))
perc = float(input("Perc:"))
masodperc = float(input("Másodperc:"))