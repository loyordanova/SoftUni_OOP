from typing import Dict


class dictionary_iter:
    def __init__(self, dict_obj: Dict):
        self.items = list(dict_obj.items())
        self.index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1

        return self.items[self.index]

# from typing import Dict
#
#
# class dictionary_iter:
#     def __init__(self, dict_obj: Dict):
#         self.dict_obj = dict_obj
#         self.keys = list(self.dict_obj.keys())
#         self.iteration = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.iteration == len(self.dict_obj):
#             raise StopIteration
#         key = self.keys[self.iteration]
#         value = self.dict_obj[key]
#         self.iteration += 1
#
#         return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)