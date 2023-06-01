class Ember:
    def __init__(self, nev, szulEv, magassag):
        self.nev = nev
        self.szulEv = szulEv
        self.magassag = magassag
    def __str__(self):
        return f"{self.nev} {self.szulEv} {self.magassag} cm"

obj = Ember("Jancsi", 1810, 150)
print(obj.nev)
print(obj.szulEv)
print(obj.magassag)

obj2 = Ember("Juliska", 1812, 146)
print(obj2.nev)
print(obj.nev, obj2.nev)

print(obj)
print(obj2)

