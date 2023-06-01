from ctypes.wintypes import SIZEL
import math
from tkinter import N



""" 
#3.feladat

szam = int(input("Adjon egy megy egész számot: "))
osztas = szam%10

print(osztas)

if osztas == 0:
    print("A szám osztható tízzel.") 
"""

""" 
#4.feladat
szam1 = int(input("Adj meg egy egész számot: "))
szam2 = int(input("Adj meg egy másik egész számot: "))

print(szam1,"/",szam2)

if szam2 == 0: 
    print("Hiba! Hülye vagy ,mint Levi.") 
"""

""" 
#8.feladat

a = int(input("Egyik oldal: "))
b = int(input("Másik oldal: "))

if a == b:
    print("Ez egy négyzet!")
else:
    print("Ez egy téglalap.")
"""

""" 
#11.feladat 

szam = int(input("Adj meg egy számot: "))

if szam>=1 and szam<=9:
    print("Benne van az {1,9} intervallumban.")
else:
    print("Nincs benne az {1,9} intervallumban.")
"""

""" 
#12.feladat

szam = int(input("Adjon meg egy számot: "))

if szam % 2 == 1 and szam<0:
    print("Igen")
else:
    print("Nem") 
"""

""" 
#17.feladat 

szam = int(input("Adjon meg egy számot: "))

if szam<0:
    print("-")
elif szam>0:
    print("+")
elif szam == 0: 
    print("A számod nulla.")
"""

""" 
#21.feladat 

szam = int(input("Adja meg az elért pontszámát: "))

if szam>=0 and szam<=42:
    print("Elégtelen")
elif szam>=43 and szam<=57:
    print("Elégséges")
elif szam>=58 and szam<=72:
    print("Közepes")
elif szam>=73 and szam<=87:
    print("Jó")
elif szam>=88 and szam<=100:
    print("Jeles")   
""" 

""" 
#22.feladat 

szam = int(input("Adja meg az életkorát: "))

if szam>=0 and szam<=13:
    print("Gyerek")
elif szam>=14 and szam<=17:
    print("Fiatalkorú")
elif szam>=18 and szam<=23:
    print("Ifjú")
elif szam>=24 and szam<=59:
    print("Felnőtt")
elif szam>=60:
    print("Idős")       
""" 

""" 
#28.feladat

szel = int(input("Adja meg a telek szélességét: "))
hossz = int(input("Adja meg a telek hosszúságát: "))
ado = int(input("Adja meg a helyi telek adót: "))

if szel<=15 and hossz<=25:
    print(int(ado*0.8))
else:
    print("Neked nem jár a kedvezmény!")
"""

""" 
#31.feladat

szam = int(input("Adjon meg egy számot 1 és 7 között: "))

if szam == 1:
    print("Hétfő")
elif szam ==2:
    print("Kedd")
elif szam ==3:
    print("Szerda")
elif szam ==4:
    print("Csütörtök")
elif szam ==5:
    print("Péntek")
elif szam ==6:
    print("Szombat")
elif szam ==7:
    print("Vasárnap")
"""

""" 
#32.feladat

ev = int(input("Adjon meg egy évszámot: "))
honap = int(input("Adjon meg egy hónapot számmal: "))
nap = int(input("Adjon meg egy napot számmal: "))

if honap == 1:
    print(ev,".január.",nap)
elif honap == 2:
    print(ev,".február.",nap)
elif honap == 3:
    print(ev,".március.",nap)
elif honap == 4:
    print(ev,".április.",nap)
elif honap == 5:
    print(ev,".május.",nap)
elif honap == 6:
    print(ev,".június.",nap)
elif honap == 7:
    print(ev,".július.",nap)
elif honap == 8:
    print(ev,".augusztus.",nap)
elif honap == 9:
    print(ev,".szeptember.",nap)
elif honap == 10:
    print(ev,".október.",nap)
elif honap == 11:
    print(ev,".november.",nap)
elif honap == 12:
    print(ev,".december.",nap)
"""

""" #35.feladat

lab = int(input("Adjon meg egy hosszúságot lábban: "))
huvelyk = int(input("Adjon meg egy hosszúságot hüvelykben: "))

print(lab*30.48+huvelyk*2.54)
"""

""" 
#41.feladat

szam1 = int(input("Adj meg az egyik befogót: "))
szam2 = int(input("Adj meg a másik befogót: "))

atfogo = ((szam1*szam1)+(szam2*szam2))

print(math.sqrt(atfogo))
"""

""" 
#44.feladat 

szam = int(input("Adjon meg egy számot: "))

if szam<0:
    print("-")
elif szam>0:
    print("+")
elif szam == 0: 
    print("+") 
"""

"""
#48.feladat

honap = int(input("Adjon meg egy hónapot: "))

if honap ==  1:
    print("január-tél")
elif honap == 2:
    print("február-tél")
elif honap == 3:
    print,("március-tavasz")
elif honap == 4:
    print("április-tavasz")
elif honap == 5:
    print("május-tavasz")
elif honap == 6:
    print("június-nyár")
elif honap == 7:
    print("július-nyár")
elif honap == 8:
    print("augusztus-nyár")
elif honap == 9:
    print("szeptember-ősz")
elif honap == 10:
    print("október-ősz")
elif honap == 11:
    print("november-ősz")
elif honap == 12:
    print("december-tél") 
"""