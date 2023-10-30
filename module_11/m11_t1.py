#Module 11, task 1

class Publication:

    def __init__(self, name):
        self.name = name

    def info(self, name):
        print(name)

class Book(Publication):

    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def info(self):
        print(f"Name: {self.name}, Author: {self.author}, Page count: {self.page_count}")


class Magazine(Publication):

    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def info(self):
        print(f"Name: {self.name}, Chief editor: {self.chief_editor}")


magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine1.info()
book1.info()

