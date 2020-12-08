class A:
    def show(self):
        print('ini kelas A')

class B(A):
    def show(self):
        print('ini kelas B')

class C(A):
    def show(self):
        print('ini kelas C')

class D(B,C):
    # def show(self):
    #     print('ini kelas D')

    pass


objek = D()
objek.show()
help(objek)