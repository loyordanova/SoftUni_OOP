import math
from typing import List


class PhotoAlbum:
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()

    def __initialize_photos(self) -> List[List[str]]:
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for index, row in enumerate(self.photos):
            if len(row) < 4:
                self.photos[index].append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(row)}"

        return "No more free slots"

    def display(self):
        result = ''
        for i in range(self.pages):
            result += '-' * 11 + '\n'
            result += ' '.join(['[]' if photo else '  ' for photo in self.photos[i]]) + '\n'
        result += '-' * 11
        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())