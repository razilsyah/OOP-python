class Hero:

    # variable class
    jumlah = 0
    __jumlah = 0
    def __init__(self,nama,health):
        # variable objek
        self.__nama = nama
        self.health = health

        # variable private tidak akan bisa di akses
        self.__private = "private"

#variable publik di akses dan di rubah
razil = Hero("razil",100)
print(razil.__dict__)
razil.nama = "siganteng"
print(razil.__dict__)
print(razil.nama)
print(Hero.__dict__)

#variable private
# ini akan error karna variable private hanya bisa di akses di scop class tsb
print(razil.__dict__)



