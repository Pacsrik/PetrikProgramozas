

def f1():
    with open("szamok.txt", "w") as f:
        for i in range (10, 101, 10):
            f.write(str(i)+"\n")

def f2():
    with open("szamok.txt", "a") as f:
        f.write(str(110)+"\n")

szamok = []
def f3():
    
    with open("szamok.txt") as f:
        for line in f:
            szamok.append(int(line))
    print(szamok)

def f4():
    sum = 0
    for item in szamok:
        if item%20 == 0:
            sum += item
            
    print(sum)

def f5():
    lista = []
    hanyszor = int(input("Hány számot szerente hozzáadni?"))
    for i in range(hanyszor):
        lista.append(input("Adja meg a hozzáadni kívánt számot: "))
        
    
    with open("szamok2.txt", 'w') as fp:
        for item in lista:
            fp.write("%s\n" % item) 

lista2 = []
def f6():
    
    with open('szamok2.txt', 'r') as f:
        lista2 = [line.strip() for line in f]
    print(lista2)
    #7.feladat
    print("A legkisebb elem a listában: ",lista2[0])
    index = lista2.index("1")
    print("Ezen a pozíción áll: ",index)
    #8.feladat
    maxpont = max(lista2) 
    print("A legnagyobb elem a listában: ",maxpont)
    index2 = lista2.index(maxpont)
    print("Ezen a pozíción áll: ",index2)
    #10.feladat
    with open ("szamok2.txt", "a") as f:
        f.write(sum(lista2)+"\n")
    
    
    
def main():
    
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    
    
main()