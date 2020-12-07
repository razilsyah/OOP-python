# inheritance adalah pewarisan ,berfungsi mencegah mengulang ulang property dan method yang sudah ada
# superClass akan mewariskan smeua yang ada di dalamnnya kepada subClass

# super class
class Hero:
    def __init__(self,nama,health):
        self.nama = nama
        self.health = health

# sub class
class Hero_intel(Hero):
    pass


class Hero_strength(Hero):
    pass

diluc = Hero("diluc",10)
print(diluc.nama)

razor = Hero_intel("razor",20)
print(razor.nama)

fishl = Hero_strength("fishl",30)
print(fishl.nama)











