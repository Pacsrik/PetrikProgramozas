#1.a

def gyakorlas():
    
    szam = int(input("Hány eleme legyen a listának?"))
    lista = []
    for i in range(szam):
        bekert = int(input("Adja meg a lista egyik elemét: "))
        lista.append(bekert)
    print(lista)
    print("A lista legkisebb eleme:", min(lista))
    print("A lista legkisebb eleme:", max(lista))
    print("A lista második legkisebb eleme:",lista[1])

    
    while True:
        szam2 = int(input("Adjon meg egy számot 1 és N között: "))
        if szam2>=1 and szam2<=szam:
            print("Jó számot adtál meg!") 
            break
        
 
    print(f"A {szam}. elem = {lista[szam-1]} ")

def main():
    gyakorlas()

main()




    




