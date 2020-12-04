# encapsulasi adalah membuat semua properti dan method menjadi private
# getter mengambil value pada variable private
# setter
class Hero:

    def __init__(self,nama,health):
        # variable objek
        self.__nama = nama
        self.__health = health


    #getter
    def getNama(self):
        return self.__nama

    def getHealth(self):
        return self.__health


    # setter
    def setNama(self,namaBaru):
        self.__nama = namaBaru

    def setHealth(self,musuh):
        self.__health -= musuh


razil = Hero("razilsyah",100)
# print(razil.__nama) ini akan error

#getter
print(razil.getNama())
print(razil.getHealth())

#setter
razil.setNama("wolf")
print(razil.getNama())

razil.setHealth(75)
print(razil.getHealth())
