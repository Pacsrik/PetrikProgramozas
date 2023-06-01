from datetime import datetime
class EU:
    def __init__(self,orszag,csatlakozas):
            self.orszag= orszag
            self.csatlakozas = csatlakozas            

    def __str__(self):
          return f"{self.orszag}, {self.csatlakozas}"
    
euLista = []

def beolvasas():

    with open("./eu/eu3.txt", "r", encoding="utf-8") as f:
          
        for sor in f:        
        
            adatok = sor.strip().split(';')       

            # példányosítás
            peldany = EU(adatok[0], datetime.strptime(adatok[1],'%Y.%m.%d').date())
            euLista.append(peldany)
    
        for elem in euLista:
            print(elem)

def f3():
    print("3. feladat: EU tagállamainak száma:",len(euLista)," db")

def f4():
     szamlalo=0
     for elem in euLista:
          if elem.csatlakozas.year == 2007:
               szamlalo += 1

     print(f"4. feladat: 2007-ben {szamlalo} ország csatlakozott.")

def f5():
     for elem in euLista:
          if elem.orszag=="Magyarország":
               print(f"5. feladat: Magyarország csatlakozási dátuma: {elem.csatlakozas}")

def f6():
     vanE = False # van-e májusi csatlakozás?
     for elem in euLista:
          if elem.csatlakozas.month == 5:
               vanE = True

     if vanE:
        print("6. feladat: Májusban volt csatlakozás!")
     else:
        print("6. feladat: Májusban nem volt csatlakozás!")

def f7():
     max = datetime.strptime("1900.01.01", '%Y.%m.%d').date()
     index = -1

     for i in range(len(euLista)):
          if euLista[i].csatlakozas>max:
               max = euLista[i].csatlakozas
               index = i 

     print(f"7. feladat: Legutoljára csatlakozott ország: {euLista[index].orszag}")

def csatlakozasDb(ev):
     szamlalo = 0
     for elem in euLista:
        if elem.csatlakozas.year == ev:
             szamlalo += 1
     return szamlalo
     
def f8():
    evek =[]
    for elem in euLista:
          if elem.csatlakozas.year not in evek:
               evek.append(elem.csatlakozas.year)

    for elem in evek:
         print(f"\t{elem} - {csatlakozasDb(elem)} ország")

def main():
     beolvasas()
     f3() 
     f4()  
     f5() 
     f6()
     f7()
     f8()

main()