class Hero:
    def __init__(self,name,health,attack,defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def serang(self,lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self,self.attack)

    def diserang(self,lawan,attackPower_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attack_diterima = attackPower_lawan / self.defense
        print(f"serangan terasa : {attack_diterima}")
        self.health -= attack_diterima
        print(f"darah {self.name} tersisa : {self.health}")


razor = Hero(name="razor",health=100,attack=50,defense=10)
diluc = Hero(name="diluc",health=100,attack=70,defense=5)

razor.serang(diluc)
print("\n")
diluc.serang(razor)