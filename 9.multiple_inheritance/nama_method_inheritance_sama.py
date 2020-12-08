# method resolusion order
# jika ada nama method yang sama ,yang akan di eksekusi melihat dari resolusion order
class A:
    def show(self):
        print('ini method A')

class B:
    def show(self):
        print('ini method B')

class C(A,B):
    def show_c(self):
        print('ini method C')

    def show(self):
        print('method C ,method dari inheritance akan di timpa')


objek = C()
objek.show_c()
objek.show()
help(objek)