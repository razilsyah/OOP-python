"""
buat sebuah game sederhana mempunya attribut nama, health, attack, dan armor.
setiap menyerang ke musuh menambahkan experience(exp) untuk menaikan level hero,
dan setiap level naik akan semakin bertambah nilai attribut health, attack, dan armor
"""

class Hero:

    # variable private class
    __jumlah = 0

    def __init__(self,name,health,attack,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attStandar = attack
        self.__armorStandar = armor
        self.__level = 1
        self.exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attMax = self.__attStandar * self.__level
        self.__armorMax = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1


    @property
    def info(self):
        return f"{self.__name} : \n\thealth : {self.__health}/{self.__healthMax} \n\tattack : {self.__attMax}" \
               f"\n\tarmor : {self.__armorMax}"



rozer = Hero("razor",100,10,5)
print(rozer.info)
