""" 
#1.feladat 

def f1():
    szoveg = input("Adja meg a szöveget: ")
    szoveg2 = szoveg.split()
    print(szoveg2)

def main():
    f1()

main() 
"""
""" 
#2.feladat

def f2():
    
    vezetek = input("Adja meg a vezetéknevét: ")
    kereszt = input("Adja meg a keresztnevét: ")

    

    if vezetek == " ":
        print("Nem két neved van.")
    elif kereszt == " ":
        print("Nem két neved van.")
    else:
        print(vezetek, kereszt)
        

def main():
    f2()

main()
"""
""" 
#3.feladat

def f3():
    s1 = input("Adjon meg karaktereket: ")
    s2 = input("Adjon meg karaktereket: ")
    s3 = s1+s2
    print(s3)

def main():
    f3()

main()
"""
""" 
#4.feladat

def f4():
    a ="       CFXUJHuhjz7g"      
    print(a.strip())

def main():
    f4()

main() 
"""
""" 
#5.feladat

def f5():
    a = input("Adj meg egy szöveget: ")
    b = input("Melyik karaktert töröljem ki belőle? ")

    print(a.replace(b,""))

def main():
    f5()

main() 
"""
""" 
#6.feladat

def f6():
    szoveg = input("Adjon meg egy szöveget: ")
    forditott = szoveg[::-1] and szoveg.strip()
    
    if forditott == szoveg:
        print("A szöveg ugyanazt jelenti fordítva!")
        
    else:  
        print("A szöveg nem ugyanazt jelenti fordítva!")

def main():
    f6()

main() 
"""
""" 
#8.feladat

def f8():
    a = input("Adjon meg egy szöveget: ")
    print(a.count(a))

f8()
"""