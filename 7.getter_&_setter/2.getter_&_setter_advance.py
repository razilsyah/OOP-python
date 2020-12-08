# decorator @property untuk merubah method menjadi seperti variable
# jika pake decorator @properti akan dinamic jika isi variable di ubah
class Hero:

    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = f'nama :{self.name} \n\thealth : {self.__health}'


    @property
    def info(self):
        return f'nama :{self.name} \n\thealth : {self.__health}'

    @property       # untuk menggetter dan setter variable private armor harus di ubah dulu sebagai property
    def armor(self):
       pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor += input

    @armor.deleter
    def armor(self):
        print("ini di delete")
        self.__armor = None

print("======= merubah info =======")
diluc = Hero("diluc",100,5)
print(diluc.info)
diluc.name = "razil"
print(diluc.__dict__)
print(diluc.info)


print("====== getter dan setter __armor =======")
print(diluc.__dict__)
print(diluc.armor)
diluc.armor = 75
print(diluc.__dict__)
print(diluc.armor)

# delete armor
del diluc.armor
print(diluc.armor)