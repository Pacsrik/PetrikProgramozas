from typing import List
import os

class Verado:
    def __init__(self, nev, cim, csoport) -> None:
        self.nev: str = nev
        self.cim: str = cim
        self.csoport: str = csoport


adatok: List[Verado] = []

f = open("veradok.txt", "r", encoding="utf-8")
for sor in f:
    line = sor.strip().split(";")
    adatok.append(Verado(*line))
f.close()

print(f"{len(adatok)} véradó adatait tudjuk")
# --------------------------------------------


# --------------------------------------------
fekete_peti = list(filter(lambda x: x.nev == "Fekete Péter", adatok))
if fekete_peti.__len__() == 0:
    print("Nincs Fekete Péter")
else:
    print("Van Fekete Péter")
# --------------------------------------------

# --------------------------------------------
haromtag = False
for adat in adatok:
    if adat.nev.count(" ") > 1 or\
            adat.nev.count(" ") >= 1 and adat.nev.count("-") >= 1:
        print(f"Van háromtagú név ({adat.nev})")
        haromtag = True
        break
if not haromtag:
    print("Nincs háromtagú név")
# --------------------------------------------


# --------------------------------------------
budapesti_rh = list(
    filter(
        lambda x: x.cim.startswith("Budapest") and "Rh pozitív" in x.csoport,
        adatok
    )
)
print(f"{len(budapesti_rh)} budapesti Rh pozitív véradó van")
# --------------------------------------------


# --------------------------------------------
budapesti_rh_neg = False
for adat in adatok:
    if adat.cim.startswith("Budapest") and adat.csoport == "A Rh negatív":
        print(f"Van budapesti Rh negatív véradó ({adat.nev})")
        budapesti_rh_neg = True
        break
if not budapesti_rh_neg:
    print("Nincs budapesti Rh negatív véradó")
# --------------------------------------------


# --------------------------------------------
nev = input("Adjon meg egy nevet: ")
nev_match = list(filter(lambda x: x.nev.split(" ")[0].split("-")[0] == nev, adatok))
if nev_match.__len__() == 0:
    print("\tNincs ilyen vezetéknév")
else:
    for adat in nev_match:
        print(f"\t{adat.nev}")
# --------------------------------------------


# --------------------------------------------
ver666szam = list(
    filter(
        lambda x: "666" in x.cim,
        adatok
    )
)
print(f"{len(ver666szam)}db 666-os cím alat lakó van")
# --------------------------------------------


# --------------------------------------------
budapestiek = list(
    filter(
        lambda x: "Budapest" in x.cim,
        adatok
    )
)

if not os.path.exists("./output"):
    os.makedirs("./output")

f = open("./output/budapestiek.txt", "w", encoding="utf-8")
for adat in budapestiek:
    f.write(f"{adat.nev};{adat.cim};{adat.csoport}\n")
f.close()
# --------------------------------------------


# --------------------------------------------
vercsoportok = {}
for adat in adatok:
    if adat.csoport not in vercsoportok:
        vercsoportok[adat.csoport] = []
    vercsoportok[adat.csoport].append(adat)

for csoport in vercsoportok:
    f = open(f"./output/vercsoport{csoport.replace(' ', '_')}.txt", "w", encoding="utf-8")
    for adat in vercsoportok[csoport]:
        f.write(f"{adat.nev};{adat.cim};{adat.csoport}\n")
    f.close()