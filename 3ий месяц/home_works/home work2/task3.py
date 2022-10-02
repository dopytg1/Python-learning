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

        
        if title == None and author == None and year == None:
            foundThisBooks = self.bookList
        elif title != None and author != None and year != None:
            for i in range(len(self.bookList)):
                book = self.bookList[i]
                if title == book.title and author == book.author and year == book.year:
                    foundThisBooks.append(book)
        elif author == None and year == None and title != None:
            title = title.replace(" ", "")
            for i in range(len(self.bookList)):
                book = self.bookList[i]
                newStr = []
                for j in range(len(title)):
                    newStr.append(book.title[j])
                newStr = "".join(newStr).replace(" ", "")
                if title.lower() == newStr.lower():
                    foundThisBooks.append(book)

        elif title == None and year == None and author != None:
            author = author.replace(" ", "")
            for i in range(len(self.bookList)):
                book = self.bookList[i]
                newStr = []
                for j in range(len(author)):
                    if book.author != None:
                        newStr.append(book.author[j])
                newStr = "".join(newStr).replace(" ", "")
                if author.lower() == newStr.lower():
                    foundThisBooks.append(book)
        elif title == None and author == None and year != None:
            for i in range(len(self.bookList)):
                book = self.bookList[i]
                if year == book.year:
                    foundThisBooks.append(book)
        elif title != None and author != None and year == None:
            for i in range(len(self.bookList)):
                book = self.bookList[i]
                if author == book.author and title == book.title:
                    foundThisBooks.append(book)
        elif title == None and author != None and year != None:
            for i in range(len(self.bookList)):
                book = self.bookList[i]
                if author == book.author and year == book.year:
                    foundThisBooks.append(book)
        elif title != None and author == None and year != None:
            for i in range(len(self.bookList)):
                book = self.bookList[i]
                if title == book.title and year == book.year:
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


book_1 = Book('Чистый код', 'Дядя Боб', 2017)
book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
book_5 = Book('Идеальный президент', 'Дядя Боб', 2018)
book_4 = Book('Рецепты татарской кухни', year=2018)

library = Library('Домашняя библиотека')
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)
library.add_book(book_5)

library.delete_book(book_1)

books = library.filter(author="Дядя Б")
print(books)
Library.as_table(books)