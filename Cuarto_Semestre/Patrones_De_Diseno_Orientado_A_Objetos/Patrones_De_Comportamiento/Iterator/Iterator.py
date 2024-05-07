class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)
