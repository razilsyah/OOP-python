
# ini cara getter dan setter sederhana
class Hero:

    def __init__(self,name,health,armor):
        self.__name = name
        self.__health = health
        self.__armor = armor

    # getter
    def getHealth(self):
        return self.__health

diluc = Hero("diluc",100,5)
print(diluc.getHealth())