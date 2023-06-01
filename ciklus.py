import math
#1.feladat 

for i in range(0,51):
    print(i)
"""
""" 
for i in range(182,213):
    print(i) 
"""
""" 
for i in range(100,201,2):
    print(i) 
"""
""" 
for i in range(89,56,-2):
    print(i) 
"""
""" 
for i in range(1,21):
    print(i,i*i)
"""
""" 
for i in range(99,0,-3):
    print(i)
"""
""" 
for i in range(100,49,-5):
    print(i*2) 
"""

""" 
for i in range(1,1000):
    print(i,end=",")
print(int(1000),".") 
"""
""" 
for i in range(1000,0,-3):
    print(i) 
"""

#2.feladat
""" 
for i in range(100):
    print("*") 
"""
"""
darabszam = int(input("Adjon meg egy számot:"))
karakter = input("Adjon meg egy karaktert:")

for i in range(darabszam):
    print(karakter)
"""
""" 
szoveg = input("Adjon meg egy tetszőleges szöveget:")

for i in range(len(szoveg)+2):
    print("*",end="")
print()
print("*",szoveg,"*",sep="")

for i in range(len(szoveg)+2):
    print("*",end="") 
"""
""" 
for i in range(2):
    print("* * ",end="")
print()

for i in range(2):  
    print(" * *",end="")
print()

for i in range(2):
    print("* * ",end="")
print()

for i in range(2):  
    print(" * *",end="")
print()

for i in range(2):
    print("* * ",end="")
print()

for i in range(2):  
    print(" * *",end="")
print()

for i in range(2):
    print("* * ",end="")
print()

for i in range(2):  
    print(" * *",end="")
print() 
"""
""" 
#3.feladat
szam1 = int(input("Adjon meg egy egész számot:"))
szam2 = int(input("Adjon meg egy másik egész számot:"))
lepeskoz = int(input("Adja meg a lépésközt:"))


if szam1<szam2:
    for i in range(szam1,szam2+1,lepeskoz):
        print(i)
else:
    for i in range (szam2+1,szam1,lepeskoz):
        print(i)
"""

""" 
#4.feladat

szam = int(input("Adjon meg egy n számot:"))

for  i in range(szam):
    print(i*i, end=";")
"""
""" 
#5.feladat
szam = int(input("Adjon meg egy n számot:"))

for  i in range(szam):
    print(i*i*i)
"""

""" 
#6.feladat
a = int(input("Adjon meg egy a számot:"))
b = int(input("Adjon meg egy b számot:"))

for i in range(a,b+1):
    print(round(math.sqrt(i),2))
"""
""" 
#7.feladat

szam= int(input("Adjon meg egy számot:"))

print(math.factorial(szam)) 
"""
""" 
#8.feladat
szam = int(input("Adjon meg egy n számot:"))

for  i in range(szam):
    print(i*i)
"""
""" 
#9.feladat
szam= int(input("Adjon meg egy számot:"))
osszeg= 0

for i in range(1, szam, 2):
    osszeg+=i
print(osszeg) 
