class Mangga:

    # magic method
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah
        print(f'nama : {self.nama} berjumlah : {self.jumlah}')


    def __repr__(self):
        return  f'nama : {self.nama} berjumlah : {self.jumlah}'


objek = Mangga('harum manis',10)
print(objek)
