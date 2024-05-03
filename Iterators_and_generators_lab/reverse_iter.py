class reversed_iter:
    def __init__(self, collection):
        self.collection = collection
        self.start_index = len(self.collection) - 1
        self.end_index = 0
        self.current_index = self.start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.end_index:
            raise StopIteration

        temp_index = self.current_index
        self.current_index -= 1

        return self.collection[temp_index]


reversed_list = reversed_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
