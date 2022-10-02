class Book():
    def __init__(self, title, author = None, year = None):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        if self.author == None:
            print("%-51s %-5s" %(self.title, self.year))
        elif self.year == None:
            print("%-30s %-20s" %(self.title, self.author))
        elif self.author == None and self.year == None:
            print(self.title)
        else: 
            print ("%-30s %-20s %-5s" %(self.title, self.author, self.year))


class Library():
    def __init__(self, name, bookList = []):
        self.name = name
        self.bookList = bookList


    def list(self):
        print(self.name)
        for i in range(len(self.bookList)):
            self.bookList[i].display()
    

    def filter(self, title = None, author = None, year = None):
        foundThisBooks = []
        title = title.replace(" ", "")
        author = author.replace(" ", "")


        for i in range(len(self.bookList)):
            book = self.bookList[i]
            newStr = []
            for j in range(len(title)):
                newStr.append(book.title[j])

            newStr = "".join(newStr).replace(" ", "")
            if title.lower() == newStr.lower():
                foundThisBooks.append(book)
        
        return foundThisBooks


    def add_book(self, book):
        self.bookList.append(book)


    def delete_book(self, book):
        for i in range(len(self.bookList)):
            if book == self.bookList[i]:
                del self.bookList[i]
                break
    
    
    def as_table(books):
        for i in range(len(books)):
            books[i].display()


book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
book_4 = Book('Рецепты татарской кухни', year=2018)
book_5 = Book('Идеальный президент', 'Дядя Боб', 2018)

library = Library('Домашняя библиотека')
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)
library.add_book(book_5)

books = library.filter("Идеальн", 'Дядя Боб', 2017)
# Library.as_table(books)