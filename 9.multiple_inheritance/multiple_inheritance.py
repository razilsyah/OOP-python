# multiple inheritance yaitu bisa menurunkan 2 warisan/turunan

class A:
    def method_A(self):
        print("ini menggunakan method A")


class B:
    def method_B(self):
        print("ini menggunakan method B")


class sesuatu(A,B):
    pass

objek = sesuatu()
objek.method_A()
objek.method_B()


print("\n========== contoh ============\n")

class Team:
    def setTeam(self,input):
        self.team = input

    def showTeam(self):
        print('team : ',self.team)

class Type:
    def setType(self,input):
        self.type = input

    def showType(self):
        print('type : ',self.type)


class Hero(Team,Type):
    def __init__(self,name,health):
        self.name = name
        self.health = health
        print(f'nama : {self.name} health : {self.health}')




mona = Hero('mona',100)
mona.setTeam('merah')
mona.setType('penyerang')

mona.showTeam()
mona.showType()
















