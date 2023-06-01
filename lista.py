from audioop import reverse
import random
""" 
lista = []
lista.append(12)
lista.append(13)
lista.append(14)

print(lista)

print(f"A lista első eleme: {lista[0]}")
print(f"A lista hossza: {len(lista)}")
print(f"A lista utolsó eleme: {lista[len(lista)-1]}")

lista.insert(2,"Maci Laci")
print(*lista, sep=", ")

lista.remove("Maci Laci")
print("Törlés után:", end= " ")
print(*lista, sep= ", ")

lista.pop(2)
print(*lista, sep= ", ")
"""

""" 
#1.feladat

def f1():
    lista = []
    for i in range (5):
        lista.append(int(input("Adjon meg egy számot: ")))
    print(*lista, sep= ", ")
    
def main():
    f1()

main() 
"""

""" 
#2.feladat

def f2():
    lista = []
    
    for i in range(7):
        lista.append(random.randint(0,1))
        if lista[i] == 0:
            print("Hamis")
        else:
            print("Igaz")
        
def main():
    f2()

main() 
"""

""" 
#3.feladat

def f3():
    lista = []
    for i in range(10):
        lista.append(random.randint(5,25))
    print(lista)
    print(lista[::-1])
    print(lista[::2])
    index = int(input("1-10 közötti szám:"))
    while index > 10 or index < 0:
        index = int(input("1-10 közötti szám:"))
    print(lista[index])

def main():
    f3()

main() 
"""

""" 
#4.feladat

def f4():
    lista1= [1,2,3,4,5,6]
    lista2= [7,8,9,10,11,12]
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i]+lista2[i])
    print(*lista3, sep=", ")

def main():
    f4()

main()
"""
""" 
#5.feladat

def f5():
    lista = ["1", "2", "3", "4", "5"]
    print(lista)
    irany = 0

    while True:
        irany2 = input("jobbra vagy balra vigyük az elemeket: ")
        if irany2 == "jobbra":
            irany = lista[-1]
            lista.pop(-1)
            lista.insert(0, irany)
            print(lista)
        elif irany2 == "balra":
            irany = lista[0]
            lista.pop(0)
            lista.append(irany)
            print(lista)

def main():
    f5()

main() 
"""

""" 
#6.feladat

def f6():
    szam = int(input("Adjon meg N számot: "))
    lista = []

    for i in range(szam,0,-1):
        lista.append(i)
    print(lista)
    
def main():
    f6()

main() 
"""

"""
 #7.feladat

def f7():
    szam = int(input("Adjon meg egy N számot: "))
    list = []
    for i in range(szam):
        bekert = int(input("Add meg a lista következő elemét: "))
        list.append(bekert)
    Sum = sum(list)
    print(Sum)

def main():
    f7()

main() 
"""