from threading import Lock, Thread

from time import sleep
class BankAccount:

    def __init__(self, *args):
        self.balance = 1000.0
        self.lock = Lock()


    def debit(self, transfer):
        self.lock.acquire()

        current_balance = self.balance
        current_balance += transfer

        sleep(0.1)

        self.balance = current_balance
        print(f'Deposited {transfer}, new balance is {self.balance}')

        self.lock.release()


    def credit(self, transfer):
        if self.balance >= transfer:
            self.balance -= transfer
        else:
            print('на счете недостаточно средств')

        self.lock.acquire()

        current_balance = self.balance
        current_balance -= transfer

        sleep(0.1)

        self.balance = current_balance
        print(f'Withdrew {transfer}, new balance is {self.balance}')

        self.lock.release()

account = BankAccount()

def debit_task(account, transfer):
    for _ in range(5):
        account.debit(transfer)

def credit_task(account, transfer):
    for _ in range(5):
        account.credit(transfer)


# создаём потоки

debit_thread = Thread(target=debit_task, args=(account, 100))
credit_thread = Thread(target=credit_task, args=(account, 150))


# запускаем потоки

debit_thread.start()
credit_thread.start()


# ждём завершения потоков

debit_thread.join()
credit_thread.join()





#
#     def increase(self, by):
#         self.lock.acquire()
#
#         current_value = self.value
#         current_value += by
#
#         sleep(0.1)
#
#         self.value = current_value
#         print(f'Значение counter: {self.value}')
#
#         self.lock.release()
#
#
bank_account = BankAccount()
#
# # создаем потоки
# t1 = Thread(target=bank_account.increase, args=(10, ))
# t2 = Thread(target=bank_account.increase, args=(20, ))
#
# # запускаем потоки
# t1.start()
# t2.start()
#
# # ждём завершения потоков
# t1.join()
# t2.join()
#
#
# print(f'Значение counter в итоге: {bank_account.value}')







