class library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
        
        
    def add_books(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
        
    def show_books(self):
        for i in self.books:
            print(f"The name of the book is '{i}'.")
        print(f"The Library has {self.noBooks} books")
    

l1 = library()
l1.add_books("Harry Potter1")
l1.add_books("Harry Potter2")
l1.add_books("Harry Potter3")
l1.add_books("Harry Potter4")
l1.show_books()
       
        
        