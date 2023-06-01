class Autok:
    def __init__(self, marka, szin, ferohely):
        self.marka = marka
        self.szin = szin
        self.ferohely = ferohely
    def __str__(self):
        return f"{self.marka} {self.szin} {self.ferohely}"

obj = Autok("BMW", "fekete színű", "5 férőhelyes" )
print(obj)
obj2 = Autok("Ferrari", "piros színű", "2 férőhelyes")
print(obj2)
obj3 = Autok("Mercedes AMG", "ezüst színű", "2 férőhelyes")
print(obj3)