class EvenNumbers:
    def __init__(self, start=0.0, end=1.0):
        self.start = start
        self.end = end

    def __iter__(self):
        self.value = self.start - 1
        return self

    def __next__(self):
        self.value += 1
        if self.value % 2 != 0:
            self.value += 1
        if self.value > self.end:
            raise StopIteration
        return self.value


en = EvenNumbers(10, 25)
for x in en:
    print (x)


