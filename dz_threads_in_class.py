from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, skill, warriors, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.warriors = warriors

    def run(self):
        print(f'{self.name}, на нас напали!', flush=True)
        for i in range(1, (int(self.warriors/self.skill)+1)):
            self.warriors -= self.skill
            print(f'{self.name} сражается {i} дня(дней).... Осталось {self.warriors} воинов', flush=True)
            sleep(5)
            if self.warriors == 0:
                print(f'{self.name} одержал победу спустя {i} дней!')



knight1 = Knight(name='Sir Lancelot', skill=10, warriors=100)
knight2 = Knight(name='Sir Galahad', skill=20, warriors=100)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print('.' * 20, 'Все битвы закончились!')