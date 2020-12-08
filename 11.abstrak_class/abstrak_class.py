# membuat class abstrak
# abc = abstrak base class
# abstrak class berfungsi agar si method yang ada pada parent di paksa agar di gunakan pada sub classnya
# method klik harus ada pada setiap subclass yang menggunakan parent Button ,karna method sudah di abstrak

from abc import ABC,abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass

class PushButton(Button):

    def click(self):
        print('ini harus di klik')


class RadioButton(Button):
    def click(self):
        print('radio button')

    def tombol(self):
        print('tombol')

button = PushButton()
button.click()

button2 = RadioButton()
button2.click()
button2.tombol()