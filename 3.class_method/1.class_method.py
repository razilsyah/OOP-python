class Hero:

    # class variable
    jumlah = 0

    def __init__(self,inputName,inputAttack,inputArmor):
        # yang ini dinamakan objek variable
        self.name = inputName
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.jumlah += 1

    # method tanpa argument
    def nama(self):
        print(f"nama saya adalah {self.name}")

    # method dengan argument
    def upAttack(self,up):
        self.attack += up

    # method dengan return
    def getAttack(self):
        return self.attack

hero1 = Hero(inputName="razor",inputAttack=100,inputArmor=50)
hero2 = Hero(inputName="fishl",inputAttack=70,inputArmor=80)

hero1.nama()
hero1.upAttack(20)
print(hero1.attack)
print(hero1.getAttack())
