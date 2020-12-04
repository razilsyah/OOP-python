class Hero:
    # variable class private
    __jumlah = 0

    def __init__(self, nama):
        self.nama = nama
        Hero.__jumlah += 1

    # memakai self berlaku untuk objek saja
    def getJumlah(self):
        return Hero.__jumlah

    # tidak memakai self berlaku untuk class saja
    def getJumlah1():
        return Hero.__jumlah

    # staticMethod
    #berlaku untuk class dan objek tapi tidak mempunya argument
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # berlaku untuk class dan objek mempunya argument
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


# memakai self
razil = Hero ( "razilsyah" )
print ( razil.getJumlah () )



# print(Hero.getJumlah()) error karna method berlaku untuk objek


# tidak memakai self
gilang = Hero ( "gilang" )
print(Hero.getJumlah1())
# print(razil.getJumlah1()) ini akan error


# static method
chugong = Hero ( "chugong" )
print(razil.getJumlah2())
print(Hero.getJumlah2())


# class method
print(razil.getJumlah3())
print(Hero.getJumlah3())

