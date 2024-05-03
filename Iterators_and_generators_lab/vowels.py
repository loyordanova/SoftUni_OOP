class vowels:
    def __init__(self, text: str):
        self.text = text
        self.all_vowels = ['a', 'i', 'e', 'u', 'o', 'y']
        self.vowels = [char for char in self.text if char.lower() in self.all_vowels]
        self.current_index = -1
        self.end_index = len(self.vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1

        if self.current_index > self.end_index:
            raise StopIteration

        return self.vowels[self.current_index]


# class vowels:
#     def __init__(self, text: str):
#         self.text = text
#         self.all_vowels = ['a', 'i', 'e', 'u', 'o', 'y']
#         self.current_index = -1
#         self.end_index = len(text) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_index += 1
#
#         if self.current_index > self.end_index:
#             raise StopIteration
#
#         current_element = self.text[self.current_index]
#         if current_element.lower() in self.all_vowels:
#
#             return current_element
#
#         return self.__next__()
