class Hero:

    # variable class
    jumlah = 0

    def __init__(self,nama,health):
        # variable objek
        self.nama = nama
        self.health = health

        # variable private tidak akan bisa di akses di luar
        self.__private = "private"

#variable publik di akses dan di rubah
razil = Hero("razil",100)
print(razil.__dict__)
razil.nama = "siganteng"
print(razil.nama)

#variable private
# ini akan error karna variable private hanya bisa di akses di scop class tsb
print(razil.__dict__)



