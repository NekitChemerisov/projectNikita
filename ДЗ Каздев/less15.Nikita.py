#Класс представляющий продукт в интернет магазине
class InternetShop():
    def __init__(self, name, price, description):
        self.product = {}
        self.name = name
        self.price = price
        self.description = description
    
    def add_desc(self):
        self.product['описание'] = self.description
        print ('Описание добавлено')

    def add_price(self):
        self.product['цена'] = self.price
        print ('Цена добавлена')


internetShop = InternetShop('Хлеб', 500, 'Вкусный')
internetShop.add_desc()
internetShop.add_price()

class Book():
    def __init__(self, title, author, publicashion_year, is_available):
        self.title = title
        self.author = author
        self.publicashion_year = publicashion_year
        self.is_available = is_available

    def checkout(self):
        self.is_available = False
        print('Книга у клиента')

    def checkin(self):
        self.is_available = True
        print('Книга в наличии')

book = Book('Война и Мир', 'Толстой', '1880', True)
book.checkout()
book.checkin()

