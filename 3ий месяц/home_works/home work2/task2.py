class book():
    def __init__(self, title, author = None, year = None):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        if self.author == None:
            print("%-50s %-5s" %(self.title, self.year))
        elif self.year == None:
            print("%-30s %-20s" %(self.title, self.author))
        else: 
            print ("%-30s %-20s %-5s" %(self.title, self.author, self.year))


harryPotter = book("Title","Author", year = 2020)
    
harryPotter.display()