class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, ціна: {self.price}, опис: {self.description}, габарити: {self.dimensions}"


class User:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}, телефон: {self.phone_number}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item(self, item, count):
        if item in self.products:
            self.products[item] += count
        else:
            self.products[item] = count

    def get_total(self):
        return sum(item.price * count for item, count in self.products.items())

    def __str__(self):
        items_str = "\n".join([f"{item.name}: {count} шт." for item, count in self.products.items()])
        return f"Покупець: {self.user}\nТовари:\n{items_str}\nЗагальна сума: {self.get_total()}"


# Тестування класів
lemon = Item('Лимон', 5, "жовтий", "малий")
apple = Item('Яблуко', 2, "червоний", "середній")

print(lemon)  # Лимон, ціна: 5, опис: жовтий, габарити: малий
print(apple)  # Яблуко, ціна: 2, опис: червоний, габарити: середній

buyer = User("Іван", "Іванов", "02628162")
print(buyer)  # Іван Іванов, телефон: 02628162

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)
"""
Покупець: Іван Іванов, телефон: 02628162
Товари:
Лимон: 4 шт.
Яблуко: 20 шт.
Загальна сума: 60
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Загальна сума має бути 60"
cart.add_item(apple, 10)
print(cart)
"""
Покупець: Іван Іванов, телефон: 02628162
Товари:
Лимон: 4 шт.
Яблуко: 10 шт.
Загальна сума: 40
"""

assert cart.get_total() == 40