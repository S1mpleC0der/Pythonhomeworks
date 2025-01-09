class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExceededException(Exception):
    pass
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def __str__(self):
        return f'{self.title} written by {self.author}'

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.max_books = 3
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.max_books:
            raise MemberLimitExceededException(f'Member limit exceeded')
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f'Book already borrowed')
        self.borrowed_books.append(book)
        book.is_borrowed = True
    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        
    def __str__(self):
        return f'{self.name} with borrowed books: {"| ".join(str(book) for book in self.borrowed_books)}'
    
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        
    def add_book(self,title,author):
        book = Book(title,author)
        self.books.append(book)
    def add_member(self,name):
        member = Member(name)
        self.members.append(member)
    def find_book(self,title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book not found")
    def find_member(self,name):
        for member in self.members:
            if member.name == name:
                return member
    def borrowing(self,name,book):
        member = self.find_member(name)
        book = self.find_book(book)
        member.borrow_book(book)
    def returning(self,name,book):
        member = self.find_member(name)
        book = self.find_book(book)
        member.return_book(book)
    def __str__(self):
        lib_books = ' | '.join([str(book) for book in self.books])
        lib_members = '\n'.join([str(member) for member in self.members])
        return f'Books: {lib_books}\nMembers: {lib_members}'
    
library = Library()
library.add_book('Harry Potter','J.K.Rowling')
library.add_book('Jumanji','Anonym writer')
library.add_book('O`tkan Kunlar','Qodiriy')
library.add_book('Hellados','Dumbadze')


library.add_member('Houston Bridge')
library.add_member('Cristina')


library.borrowing('Houston Bridge','Harry Potter')
library.borrowing('Houston Bridge', 'Jumanji')
#library.borrowing('Houston Bridge', 'O`tkan Kunlar')   <-- Raises exception
library.borrowing('Houston Bridge', 'Hellados')
#library.borrowing('Cristina','Jumanji')  <-- Raises exception
#library.borrowing('Cristina','Allambalo') <-- Raises exception


library.returning('Houston Bridge','Harry Potter')
print(library.__str__())
    
        
    
        