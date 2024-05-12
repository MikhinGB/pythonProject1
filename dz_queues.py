import time
from threading import Thread

from time import sleep
import random as rnd

import queue


class Table(Thread):
    def __init__(self, number,  is_busy=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_busy = False
        self.number = number



class Cafe:

    def __init__(self, tables, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tables = tables
        self.turn = queue.Queue(maxsize=20)
        self.customers_thread = []

    def customer_arrival(self):               # поток-производитель. Моделирует приход посетителя(каждую секунду)
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл')
            self.serve_customer(i)
            sec = rnd.uniform(0.6, 2)  # интервал прибытия клиентов - случайная величина из диапазона
            time.sleep(sec)                       # от 0,6 до 2 сек




    def serve_customer(self, customer):          # поток-потребитель. Моделирует обслуживание посетителя.
        free_table = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer} сел за стол {table.number}.')
                customer_thr = Customer(customer, self, self.turn, table)
                customer_thr.start()
                self.customers_thread.append(customer_thr)
                free_table = True
                return
        if not free_table:
            print(f'Посетитель номер {customer} ждёт стол.')
            self.turn.put(customer)



class Customer(Thread):

    def __init__(self, number, cafe, turn, table, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.number = number
        self.cafe = cafe
        self.turn = turn
        self.table = table

    def run(self):
        # Какой такой павлин-мавлин? Не видишь - мы кушаем!
        sec = rnd.uniform(4, 7)  # время обслуживания клиентов - случайная величина из диапазона
        time.sleep(sec)                     # от 4 до 7 сек
        print(f'Посетитель номер {self.number} покушал и ушёл')
        self.table.is_busy = False
        if not self.turn.empty():
            next_customer = self.turn.get()
            self.cafe.serve_customer(next_customer)








# Создаем столики в кафе
tables = []
for i in range(1, 4):
    tables.append(Table(i))

print(tables)

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

for i in cafe.customers_thread:
    i.join()
