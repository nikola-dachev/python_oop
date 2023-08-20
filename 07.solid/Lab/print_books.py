from abc import ABC, abstractmethod

class Book:
  def __init__(self, title, author, content):
    self.title = title
    self.author= author
    self.content = content

class BaseFormatter(ABC):
  @abstractmethod
  def format(self, book: Book):
    pass

class PaperFormatter(BaseFormatter):
  def format(self, book: Book):
    return f'{book.title}\n{book.author}'

class WebFormatter(BaseFormatter):
  def format(self, book: Book):
    return f'{book.content}'

class Printer:
  def __init__(self,formatter: BaseFormatter):
    self.formatter = formatter

  def get_book(self, book: Book):
    return self.formatter.format(book)


book = Book('Title', 'Author-a', 'some content')
p_a = Printer(WebFormatter())
p_b = Printer(PaperFormatter())

print(p_a.get_book(book))
print(p_b.get_book(book))
