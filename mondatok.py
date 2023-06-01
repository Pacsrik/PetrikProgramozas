import random

def mondatok():
    hanyadik = 0
    def nevelo(fonev):
        if fonev[0] in "aeiouáéíóöőüű":
            return "Az"
        else:
            return "A"
    
    def jelzo():
        jelzok = ["piros.", "fehér.", "zöld."]
        return random.choice(jelzok)
   
    fonev1 = input("Adja meg az első főnévét: ")
    hanyadik = hanyadik + 1 
    print(hanyadik, ".főnév:", fonev1)
    print(nevelo(fonev1) + " " + fonev1 + " " + jelzo())

    fonev2 = input("Adja meg a második főnévét: ")
    hanyadik = hanyadik + 1 
    print(hanyadik, ".főnév:", fonev2)
    print(nevelo(fonev2) + " " + fonev2 + " " + jelzo())
    
    
    tovabb = input("Szeretne további főnéveket megadni? (i/n) ")
    while tovabb == "i":
        
        fonev = input("Adja meg a következő főnévét: ")
        hanyadik = hanyadik + 1 
        print(hanyadik, ".főnév:", fonev)
       
        print(nevelo(fonev) + " " + fonev + " " + jelzo())
        tovabb = input("Szeretne további főnéveket megadni? (i/n) ")
    
    
    while tovabb == "n":
        print("VÉGE!")
        break



def main():
    mondatok()



main()