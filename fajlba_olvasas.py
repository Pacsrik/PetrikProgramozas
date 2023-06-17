novenyek = []

with open("novenyek.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        noveny = sor.strip()
        novenyek.append(noveny)

print(novenyek)
