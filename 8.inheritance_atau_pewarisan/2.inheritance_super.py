
# superClass
class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def info(self):
       print( f"{self.name} health : {self.health}")


# subClass
class Hero_intel(Hero):
    def __init__(self,name):
        super().__init__(name,100)
        super().info()


class Hero_attack(Hero):
    def __init__(self,name):
        super().__init__(name,200)
        super().info()



diluc = Hero_intel("diluc")
fishl = Hero_attack('fishl')













