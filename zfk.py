from typing import List


class Jatekos:
    def __init__(self, nev, poszt, meccs_count, gol_count) -> None:
        self.nev: str = nev
        self.poszt: str = poszt
        self.meccs_count = int(meccs_count)
        self.gol_count = int(gol_count)


focistak: List[Jatekos] = []

f = open("zfk.txt", "r", encoding="utf-8")
for sor in f:
    line = sor.strip().split(";")
    if line.__len__() == 4:
        focistak.append(Jatekos(*line))

f.close()


hatved_counter = 0
for adat in focistak:
    if adat.poszt == "hátvéd":
        hatved_counter += 1
print(f"{hatved_counter} hátvéd adataid tárolja a fájl")


gol_counter = 0
for adat in focistak:
    gol_counter += adat.gol_count
print(f"{gol_counter/len(focistak)} gólt rugtak átlagosan")


marci = None
for adat in focistak:
    if adat.nev == "Marci":
        marci = adat
        break
print(
    f"Marci {marci.meccs_count} meccsen játszott, és {marci.gol_count} gólt rúgott"
)


tobb_mint_10_meccs = list(filter(lambda x: x.meccs_count >= 10, focistak))
print("Akik több mint 10 meccsen játszottak:")
if len(tobb_mint_10_meccs) == 0:
    print("\tNincs ilyen játékos")
for adat in tobb_mint_10_meccs:
    print(f"\t{adat.nev} - {adat.poszt} ({adat.meccs_count})")


legjobb_mecs_gol_arany = max(focistak, key=lambda x: x.meccs_count / x.gol_count if x.gol_count != 0 else 0)
print(
    f"{legjobb_mecs_gol_arany.nev} a legjobb meccs-gól aránnyal rendelkező játékos, aránya: {legjobb_mecs_gol_arany.meccs_count/legjobb_mecs_gol_arany.gol_count:.2f} ({legjobb_mecs_gol_arany.meccs_count}/{legjobb_mecs_gol_arany.gol_count})"
)

post_map = {}
for adat in focistak:
    if adat.poszt not in post_map:
        post_map[adat.poszt] = []
    post_map[adat.poszt].append(adat.nev)

print("Posztok:")
for poszt in post_map:
    print(f"\t{poszt.capitalize()}: {', '.join(post_map[poszt])}")
