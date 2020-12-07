class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def info(self,tipe):
        print("show info superClass Hero")
        print( f"{self.name} tipe : {tipe} \n\thealth : {self.health}")


# subClass
class Hero_intel(Hero):
    def __init__(self,name):
        super().__init__(name,100)


    #override
    def info(self):
        print ( f"{self.name} tipe : intelligent \n\thealth : {self.health}" )

class Hero_attack(Hero):
    def __init__(self,name):
        super().__init__(name,200)



diluc = Hero_intel("diluc")
diluc.info()

print("\n")

razor = Hero_attack("razor")
razor.info("attack")
















