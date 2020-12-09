from abc import ABC,abstractmethod

class Button(ABC):

    def __init__(self,set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

class PushButton(Button):

    def click(self):
        print(f'GO TO : {self.link}')



objek1 = PushButton('www.kelasterbuka.id')
objek1.click()
