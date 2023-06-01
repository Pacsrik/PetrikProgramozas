import math
import random
from tkinter.tix import Tree


#FONTOS
"""
osszeg = 0

while True:
    szam = int(input("Kérem adjon meg egy számot! Kilépés 0-val!"))
    osszeg += szam
    if szam == 0:
        break
print("A számok összege:",osszeg)
"""
#FONTOS




""" 
#1.feladat 

szam = random.randint(0,10)
print(szam)
szam2 = random.randint(0,100)
print(szam)
szam3 = random.randint(10,15)
print(szam)
szam4 = random.randint(-100,100)
print(szam) 
for i in range(10):
    szam5 = random.randint(0,10)
    print(szam5) 
for i in range(4):
    szam5 = random.randint(10,30)
    print(szam5) 
"""
""" 
#2.feladat 

tovabb = True
while tovabb:
    tipp = int(input("Fej vagy írás? fej=0, írás=1:"))
    random = random.randint(0,1)
    print("Ezt sorsolta a gép:", random)
    if random == tipp:
        print("Gratulálok, eltaláltad!")
        tovabb = False
    else: 
        print("Sajnos most nem találtad el, de tovább tudsz próbálkozni! :D ") 
"""
"""
#6.feladat

db = int(input("db:"))
karakter = input("karakter:")

i=0
while i < db:
    print(karakter, end="")
    i+=1
"""

""" 
#22.feladat

a = True
while a:
    szam = int(input("Adjon meg egy számot 1 és 7 között:"))
    if szam == 1:
        print("Hétfő")
        a = False
    elif szam == 2:
        print("Kedd")
        a = False
    elif szam == 3:
        print("Szerda")
        a = False
    elif szam == 4:
        print("Csütörtök")
        a = False
    elif szam == 5:
        print("Péntek")
        a = False
    elif szam == 6:
        print("Szombat")
        a = False
    elif szam == 7:
        print("Vasárnap") 
        a = False
while a:        
    if szam < 1:
         print("A szám nem jó, adjon meg egy újat!") 
    elif szam > 7:
        print("A szám nem jó, adjon meg egy újat!")
        a=False
"""