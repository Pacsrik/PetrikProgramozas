class Vizilo:

    def __init__(self, név, szülév, nem, tömeg):
        self.név = név

        self.szülév = szülév

        self.nem = nem

        self.tömeg = tömeg

   

    def __str__(self):

        return f"{self.név}, {self.szülév}, {self.nem}, {self.tömeg}"



vizilovak = []

with open ("vizilo.txt", "r", encoding="utf-8") as f:

    elso_sor = True

    for sor in f:

        adatok = sor.strip().split(";")

        if elso_sor == True:

            elso_sor = False

            continue

        peldany = Vizilo(adatok[0], int(adatok[1]), adatok[2], int(adatok[3]))

        vizilovak.append(peldany)

    for elem in vizilovak:

        print(elem)