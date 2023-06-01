import random
""" 
def elso():
    print("Hello")

def main():
    elso()

main()
"""
""" 
#1.feladat

def f1():
    a = int(input("A háromszög oldala:"))
    b = int(input("A háromszög magassága:"))
    terulet = a*b/2
    print("A háromszög területe:",terulet)

def main():
    f1()

main()
"""
""" 
#2.feladat 

def f2():
    a = int(input("A háromszög egyik oldala: "))
    b = int(input("A háromszög másik oldala: "))
    c = int(input("A háromszög harmadik oldala: "))
    if a<b+c and b<c+a and c<b+a:
        print("Ez lehet egy háromszög.")
    else:
        print("Ez nem lehet háromszög.")

def main():
    f2()

main()
"""
""" 
#3.feladat

def f3():
    a = int(input("A háromszög egyik oldala: "))
    b = int(input("A háromszög másik oldala: "))
    c = int(input("A háromszög harmadik oldala: "))
    if c == b:
        print("Ez a háromszög egyenlő szárú.")
    else:
        print("Ez a háromszög nem egyenlő szárú.")

def main():
    f3()

main() 
"""
""" 
#4.feladat

def f4():
    fizetes = int(input("Adja meg a fizetését: "))
    beosztas = input("Adja meg a beosztását: ")
    
    if beosztas == "vezető":
        print("Az új fizetésed:",int(fizetes*1.25))
    else: 
        print("Az új fizetésed:",int(fizetes*1.15))

def main():
    f4()

main() 
"""
""" 
#6.feladat 

def f6():
    a = int(input("Adjon meg egy számot: "))
    for i in range(a,-1,-1):
        print(i)

def main():
    f6()

main()
"""
""" 
#7.feladat

def f7():
    a = int(input("Adjon meg egy számot: "))
    if a>0:
        for i in range(a,-1,-1):
            print(i)
    else:
        print("A számod negatív!")
    

def main():
    f7()

main() 
"""
""" 
#8.feladat

def f8():
    a = int(input("Adjon meg egy számot: "))
    while a < 0:
        a = int(input("Adjon meg egy számot: "))
    else: 
        for i in range(a,-1,-1):
            print(i)

def main():
    f8()

main() 
"""
""" 
#9.feladat

def f9():
    a = int(input("Adjon meg egy számot: "))
    b = int(input("Adjon meg egy másik számot:"))

    if a > b:
        for i in range(a,b):
            print(i)
    else:
        for i in range(b,a):
            print(i)
        
def main():
    f9()

main() 
"""
""" 
#11.feladat

def f11():
    hanyszor = int(input("Hányszor?"))
    
    egy = 0
    ketto = 0
    harom = 0
    for i in range(hanyszor):
        dobas= random.randint(1,3)
        
        if dobas==1:
            egy+=1
        elif dobas==2:
            ketto+=1
        elif dobas==3:
            harom+=1
        print(egy)
        print(ketto)
        print(harom)

def main():
    f11()

main()
"""
