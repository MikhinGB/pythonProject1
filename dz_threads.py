from threading import Thread
from  time import sleep


def counter():
    for i in range(1, 11):
        print(i)
        sleep(1)


def alfabet():
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
        print(i)
        sleep(1)

th1 = Thread(target=counter)
th1.start()

th2 = Thread(target=alfabet)
th2.start()

th1.join()
th2.join()