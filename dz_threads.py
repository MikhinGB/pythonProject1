from threading import Thread
from  time import sleep



def func():
    for i in range(1, 11):
        print(i)
        sleep(1)

th = Thread(target=func)
th.start()

for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
    sleep(0.99)
    print(i)

th.join()