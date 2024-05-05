from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        ...


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.author}\n{book.content[:4]}"


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


book = Book('Book1', 'qwerty', 'some_content')
pa = Printer(PaperFormatter())
pb = Printer(WebFormatter())
print(pa.get_book(book))
