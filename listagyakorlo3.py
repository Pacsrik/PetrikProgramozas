import random
from collections import Counter
""" 
def f1():
    lista = []
    for i in range(10):
        lista.append(random.randint(0,20))
    print(lista)


def main():
    f1()

main()
"""
""" 
def f2():
    lista = []
    for i in range(5):
        szam = random.randint(1,90)
        if szam not in lista:
            lista.append(szam)
        else: 
            lista.append(random.randint(1,90))
        

    print(lista)

def main():
    f2()

main() 
"""
""" 
def f3():
    lista = []
    for i in range(20):
        lista.append(random.randint(0,5))
    print(lista)
    counter = Counter(lista)

    most_common = counter.most_common(1)[0][0]
    print("Ez a szám szerepel legtöbbször: ", most_common)
    

def main():
    f3()

main() 
"""

""" 
def f4():
    lista = []
    for i in range(10):
        b = random.randint(-100,100)
        lista.append(b)

    a = str(lista)
    a = (a.replace(',', ' '))
    print(a)
    

def main():
    f4()


main() 
"""