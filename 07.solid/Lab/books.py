
from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
  def __init__(self):
    self.books: List[Book] = []

  def add_book(self, book: Book):
    self.books.append(book)
    return f'{book.title} has been added'

  def find_book(self, title):
    try:
      book = next(filter(lambda x: x.title == title, self.books))
      return book

    except StopIteration:
      return 'The book does not exist'


b1 = Book('Title1', 'Author 1')
b2 = Book('Title2', 'Author 2')
b3 = Book('Title3', 'Author 3')

library = Library()
print(library.add_book(b1))
library.add_book(b2)
library.add_book(b3)
print([b.title for b in library.books])
print(library.find_book('Title1'))
