import random

def gyakorlas2():
    elemszam = int(input("Hány eleme legyen a listának? "))
    lista = []
    
    for i in range (elemszam):
        lista.append(random.randint(1,500))
    print(lista)

    valtozo = 0
    for i in lista:
        if i < 350 and i > 15 and i & 1 == 0:
            valtozo += 1

    print(f"{valtozo} páros szám van 15 és 350 között!")



    valtozo2 = 0
    for i in lista:
        if i % 3 == 0:
            valtozo2 += i
    print(f"A hárommal osztható számok összege: {valtozo2}")



def main():
    gyakorlas2()

main()