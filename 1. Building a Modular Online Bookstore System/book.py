# Task 1: Designing the Book Module

class Book:
    def __init__(self, title, author, serial_num, price, stock, sale = 1):
        self.title = title
        self.author = author
        self.serial_num = serial_num
        self.price = price
        self.stock = stock
        self.sale = sale

class BookEditer:
    def __init__(self, book):
        self.book_edit = book

    def edit_book_info(self, book, new_title, new_author, new_serial_num):
        self.book_edit = book
        self.book_edit.title = new_title
        self.book_edit.author = new_author
        self.book_edit.serial_num = new_serial_num
        return self.book_edit
    
class BookPricer:
    def __init__(self, book):
        self.book_pricer = book

    def price_book(self, book, new_price):
        self.book_pricer = book
        self.book_edit.price = new_price
        return self.book_edit

    def sale_for_book(self, book, sale_fraction):
        if sale_fraction < 0 or sale_fraction > 1:
            print('Must choose a decimal between 0 and 1')
            return self.book_edit
        self.book_pricer = book
        self.book_pricer.sale = sale_fraction
        return self.book_edit
    
class BookStocker:
    def __init__(self, book):
        self.book_stock = book

    def add_stock(self, book, amount):
        self.book_stock = book
        self.book_stock.stock += amount
        return self.book_stock

    def remove_stock(self, book, amount):
        self.book_stock = book
        self.book_stock.stock -= amount
        return self.book_stock
    
class BookDispalyer:
    def __init__(self, book):
        self.book_display = book

    def display_price(self, book):
        self.book_display = book
        print(f"{self.book_display.title} costs {self.book_display.price * self.book_display.sale}")

    def display_all_info(self, book):
        self.book_display = book
        print(self.book_display.title)
        print(self.book_display.author)
        print(self.book_display.serial_num)
        print(self.book_display.price)
        print(self.book_display.stock)
        print(self.book_display.sale)