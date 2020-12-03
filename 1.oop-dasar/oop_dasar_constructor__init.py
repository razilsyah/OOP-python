# class adalah template yang bisa di gunakan oleh objek
# __init__ pada saat class di panggil __init__ ini akan terpanggil juga
class hero():
    def __init__(self,inputName,inputAttack,inputArmor):
        self.name = inputName
        self.attack = inputAttack
        self.armor = inputArmor



# hero1 adalah objek
hero1 = hero(inputName="rozer",inputAttack=200,inputArmor=1000)
hero2 = hero(inputName="diluc",inputAttack=300,inputArmor=500)

print(hero1.__dict__) # mencoba menampilkan attribut apa saja yang ada pada objek hero1
print(hero1.name) # menampilkan attribut yang dipilih atau di select
print(hero2.__dict__)
print(hero2.attack)