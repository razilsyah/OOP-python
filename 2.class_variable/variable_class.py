class Hero():

    # class variable
    jumlah = 0

    def __init__(self,inputName,inputAttack,inputArmor):
        # yang ini dinamakan objek variable
        self.name = inputName
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.jumlah += 1
        print(f"hero dengan nama :{inputName}")




hero1 = Hero(inputName="rozer",inputAttack=200,inputArmor=1000)
print(Hero.jumlah)
hero2 = Hero(inputName="diluc",inputAttack=300,inputArmor=500)
print(Hero.jumlah)

print(hero1.__dict__)
print(hero1.name)
print(hero2.__dict__)
print(hero2.attack)