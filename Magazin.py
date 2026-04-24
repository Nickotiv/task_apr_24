class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def get_info(self):
        return f"Товар: {self.name}, цена: {self.price} руб."


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product_id):
        for product in self.items:
            if product.product_id == product_id:
                self.items.remove(product)
                break

    def total_price(self):
        total = 0

        for product in self.items:
            total += product.price

        return total

    def clear(self):
        self.items = []


class Order:
    def __init__(self, order_id, cart, customer_name):
        self.order_id = order_id
        self.cart = cart
        self.customer_name = customer_name
        self.is_paid = False

    def get_total(self):
        return self.cart.total_price()

    def pay(self):
        self.is_paid = True
        return f"Заказ №{self.order_id} оплачен на сумму {self.get_total()} руб."

    def receipt(self):
        text = f"Заказ №{self.order_id}\n"
        text += f"Покупатель: {self.customer_name}\n"
        text += "---\n"

        number = 1

        for product in self.cart.items:
            text += f"{number}. {product.name} - {product.price} руб.\n"
            number += 1

        text += "---\n"
        text += f"Итого: {self.get_total()} руб.\n"

        if self.is_paid:
            text += "Оплачен: Да"
        else:
            text += "Оплачен: Нет"

        return text

# Создаём товары
apple = Product("Яблоки", 50, 1)
milk = Product("Молоко", 80, 2)

# Создаём корзину
cart = Cart()
cart.add_product(apple)
cart.add_product(milk)
cart.add_product(apple)   # можно добавить ещё раз

# Создаём заказ из этой корзины
order = Order(1, cart, "Анна")
print(order.get_total())  # 180

# Оплачиваем
print(order.pay())        # "Заказ №1 оплачен на сумму 180 руб."

# Получаем чек
print(order.receipt())  

# Тест 1: товар и корзина
p1 = Product("Ручка", 30, 1)
p2 = Product("Тетрадь", 50, 2)
cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
assert cart.total_price() == 80
cart.add_product(p1)
assert cart.total_price() == 110
print("Тест 1 пройден")

# Тест 2: удаление товара из корзины
cart.remove_product(1)  # удаляет одну ручку
assert cart.total_price() == 80
cart.remove_product(99)  # нет такого — ничего не меняется
assert cart.total_price() == 80
print("Тест 2 пройден")

# Тест 3: очистка корзины
cart.clear()
assert cart.total_price() == 0
assert len(cart.items) == 0
print("Тест 3 пройден")

# Тест 4: заказ и оплата
cart = Cart()
cart.add_product(Product("Хлеб", 40, 3))
order = Order(10, cart, "Петр")
assert order.get_total() == 40
assert order.is_paid == False
order.pay()
assert order.is_paid == True
assert "оплачен" in order.receipt().lower()
print("Тест 4 пройден")
