
import multiprocessing
import random

class WarehouseManager:


    def __init__(self):
        self.data = multiprocessing.Manager().dict()

# реализует запрос (действие с товаром), принимая request-кортеж
    def process_request(self, request, *args, **kwargs):
        if request[0] not in self.data:
            self.data[request[0]] = 0
        if request[1] == "receipt":
            self.data[request[0]] += request[2]
        else:
            if self.data[request[0]] >= request[2]:
                self.data[request[0]] -= request[2]

# принимает запросы и создает для каждого свой параллельный процесc
    def run(self, requestes):
        self.requestes = requestes
        processes = []
        for request in self.requestes:
            multiprocessing.Process(target=self.process_request, args=request).start()
        for request in self.requestes:
            multiprocessing.Process(target=self.process_request, args=request).join()





if __name__ == '__main__':

    manager = WarehouseManager()

    requestes = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 100),
        ("product3", "receipt", 200),
        ("product1", "shipment", 50)
    ]

    manager.run(requestes)

    print(manager.data)