def exemplo_1(x, y, z=0):
    return x + y

class Trap:
    def intro(self):
        print("There are many types of traps.")
    
    def personality(self):
        print("Most traps are dere but some are not only dere.")

class Kizuna(Trap):
    def personality(self):
        print("Kisuna is a dere.")

class Rimuru(Trap):
    def personality(self):
        print("Rimuru is a kuldere.")

class Tsubaki(Trap):
    def personality(self):
        print("Tsubaki is a tsundere.")


Kizuna_Aikawa = Kizuna()
Rimuru_Tempest = Rimuru()
Tsubaki_Yaezaki = Tsubaki()

for trap in (Kizuna_Aikawa, Rimuru_Tempest, Tsubaki_Yaezaki):
    trap.intro()
    trap.personality()


class what_I_am():
    def what_I_do(self):
        print("I can demonstrate duck-typying.")