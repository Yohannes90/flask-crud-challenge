from uuid import uuid4


class Book:
    def __init__(self, title, author, price, category, publication_year):
        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.price = price
        self.category = category
        self.publication_year = publication_year
