def beolvasas():
    f = open("asd.txt", encoding="UTF-8")
    
    for sor in f:
        print(sor.strip())
    f.close()

def beolvasEgeszeket():
    lista = []
    f = open("szamok.txt")
    for sor in f:
        adat = int(sor.strip())
        lista.append(adat)
    for item in lista:
        print(item, end= " ")
    print()
    #20-nál nagyobb számok
    for item in lista:
        if item>20:
            print(item, end=" ")


def main():
    beolvasas()
    beolvasEgeszeket()

main()