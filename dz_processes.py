
import multiprocessing


class WarehouseManager(multiprocessing.Process):


    def __init__(self, data, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collector = collector
        self.requests = requests
        self.data = data

    def process_request(self, request):      # реализует запрос (действие с товаром), принимая requests-кортеж
        if request[1] == "receipt":
            if request[0] not in self.data:
                self.collector[request[0]] = request[2]
            else:
                self.collector[request[0]] += request[2]
                print(self.collector)
        else:
            if self.collector[request[0]] >= request[2]:
                self.collector[request[0]] -= request[2]
            else:
                print(
                    f'Товарной позиции {request[0]} на складе меньше, чем требуется. Её всего {self.data[request[0]]}. '
                    f'Измените объем заказа')


    def run(self):     # принимает запросы и создает для каждого свой параллельный процес
        self.requests = requests
        self.collector = multiprocessing.Queue()

        for request in self.requests:
            request.start()
        for request in self.requests:
            request.join()
        while not self.collector.empty():
            self.data = self.collector.get()





def main():
    collector = multiprocessing.Queue()

# if __name__ == '__main__':


        # start

        # join
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 100),
    ("product3", "receipt", 200),
    ("product1", "shipment", 50)
]

manager = WarehouseManager()

manager.run(requests)

print(manager.data)