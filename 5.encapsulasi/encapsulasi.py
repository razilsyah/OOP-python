# encapsulasi buat semua variable private,dan untuk mengambil data yang di butuhkan kita menggunakan getter & setter
# getter mengambil variable private
# setter mensetting variable private
class Hero:

    def __init__(self,nama,health,attpower):
        # variable objek
        self.__nama = nama
        self.__health = health
        self.__attpower = attpower


    #getter
    def getNama(self):
        return self.__nama

    def getHealth(self):
        return self.__health

    def getAttack(self):
        return self.__attpower


    # setter
    def set_att_power(self,nilaibaru):
        self.__attpower = nilaibaru

    def diserang(self,musuh):
        self.__health -= musuh

# awal dari game
razil = Hero("razilsyah",100,5)
print(razil.__dict__)

# mencoba merubah var private ,alhasil malah menambah var baru
# razil.__nama = "diluc"
# print(razil.__dict__)
# print(razil.__nama)
# print(razil.__nama) ini akan error

print("==========================================")

#jadi untuk mengambil var private agar tidak error pakai getter
print(razil.getNama())
print(f'health : {razil.getHealth()}')
print('==========================================')


#setter mensetting var private
razil.diserang(90)
print(f'health : {razil.getHealth()}')

razil.set_att_power(80)
print(f'attack : {razil.getAttack()}')

