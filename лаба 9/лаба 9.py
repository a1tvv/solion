# from abc import ABC, abstractmethod
#
#
# # -----------------------------
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#
#     @abstractmethod
#     def refund(self, amount):
#         pass
#
#
# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         print(f"[Кредитная карта] Оплата на сумму {amount}₽ успешно проведена.")
#
#     def refund(self, amount):
#         print(f"[Кредитная карта] Возврат на сумму {amount}₽ выполнен.")
#
#
# class CryptoPayment(Payment):
#     def pay(self, amount):
#         print(f"[Криптовалюта] Перевод {amount}$ в блокчейн выполнен.")
#
#     def refund(self, amount):
#         print(f"[Криптовалюта] Возврат {amount}$ обратно в кошелёк произведён.")
#
#
# payments = [CreditCardPayment(), CryptoPayment()]
# for p in payments:
#     p.pay(1000)
#     p.refund(200)
#
#
# from abc import ABC, abstractmethod
#
# class Course(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def get_materials(self):
#         pass
#     @abstractmethod
#     def end(self):
#         pass
#
# class PythonCourse(Course):
#     def start(self):
#         print("Стартовал Python курс")
#
#     def get_materials(self):
#         return ["Основы синтаксиса", "ООП", "Модули", "Файлы"]
#
#     def end(self):
#         print("Курс Python завершён.")
#
# class MathCourse(Course):
#     def start(self):
#         print("Курс Математики начался! ➕")
#
#     def get_materials(self):
#         return ["Алгебра", "Геометрия", "Тригонометрия"]
#
#     def end(self):
#         print("Курс Математики завершён.")
#
#
# courses = [PythonCourse(), MathCourse()]
# for c in courses:
#     c.start()
#     print("Материалы:", c.get_materials())
#     c.end()
#
#
# # ---------------------------------------
# from abc import ABC, abstractmethod
#
# class Delivery(ABC):
#     @abstractmethod
#     def calculate_cost(self, distance):
#         pass
#
#     @abstractmethod
#     def deliver(self):
#         pass
#
# class AirDelivery(Delivery):
#     def calculate_cost(self, distance):
#         return distance * 10
#
#     def deliver(self):
#         print("Доставка по воздуху началась ")
#
# class GroundDelivery(Delivery):
#     def calculate_cost(self, distance):
#         return distance * 5
#
#     def deliver(self):
#         print("Наземная доставка началась ")
#
# class SeaDelivery(Delivery):
#     def calculate_cost(self, distance):
#         return distance * 3
#
#     def deliver(self):
#         print("Морская доставка началась ")
#
# deliveries = [AirDelivery(), GroundDelivery(), SeaDelivery()]
# for d in deliveries:
#     print(f"{d.__class__.__name__}: Стоимость {d.calculate_cost(100)}₽")
#     d.deliver()
#
# from abc import ABC, abstractmethod
#
# class BankAccount(ABC):
#     def __init__(self, owner, balance, pin):
#         self.__owner = owner
#         self.__pin = pin
#         self.__balance = balance
#     @abstractmethod
#     def deposit(self, amount, pin):
#         if pin == self.__pin and amount > 0:
#             self.__balance += amount
#             print(f"Пополнено {amount}₽. Баланс: {self.__balance}₽")
#         else:
#             print("Ошибка: неправильный PIN или сумма.")
#
#     def withdraw(self, amount, pin):
#         if pin == self.__pin and 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Снято {amount}₽. Баланс: {self.__balance}₽")
#         else:
#             print("Ошибка: недостаточно средств или неверный PIN.")
#
#     def change_pin(self, old_pin, new_pin):
#         if old_pin == self.__pin:
#             self.__pin = new_pin
#             print("PIN успешно изменён.")
#         else:
#             print("Ошибка: старый PIN неверен.")
#
#
# acc = BankAccount("Эльзар", 10000, 1234)
# acc.deposit(2000, 1234)
# acc.withdraw(3000, 1234)
# acc.change_pin(1234, 4321)
#
#
# # -----------------------------
# class UserProfile:
#     def __init__(self, email, password):
#         self.__email = email
#         self.__password = password
#         self._status = "free"
#
#     def login(self, email, password):
#         if email == self.__email and password == self.__password:
#             print("Успешный вход.")
#             return True
#         else:
#             print("Ошибка: неверный логин или пароль.")
#             return False
#
#     def upgrade_to_premium(self):
#         self._status = "premium"
#         print("Аккаунт обновлён до PREMIUM!")
#
#     def get_info(self):
#         return {"email": self.__email, "status": self._status}
#
#
# user = UserProfile("user@mail.com", "1234")
# if user.login("user@mail.com", "1234"):
#     user.upgrade_to_premium()
# print(user.get_info())
#
#
# # -----------------------------
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.__discount = 0
#
#     def get_price(self):
#         return self.price * (1 - self.__discount)
#
#     def set_discount(self, discount, is_admin=False):
#         if is_admin:
#             self.__discount = discount
#             print(f"Скидка {discount * 100}% установлена на {self.name}.")
#         else:
#             print("Ошибка: доступ запрещён.")
#
#
# p = Product("Наушники", 5000)
# p.set_discount(0.2, is_admin=True)
# print("Цена со скидкой:", p.get_price())
#
# # -----------------------------
# class TextFile:
#     def open(self):
#         print("Открыт текстовый файл (.txt)")
#
#
# class ImageFile:
#     def open(self):
#         print("Открыто изображение (.png)")
#
#
# class AudioFile:
#     def open(self):
#         print("Открыт аудиофайл (.mp3)")
#
#
# def open_all(files):
#     for f in files:
#         f.open()
#
#
# files = [TextFile(), ImageFile(), AudioFile()]
# open_all(files)
#
# # -----------------------------
# class Car:
#     def move(self, distance):
#         speed = 80
#         print(f"Машина проедет {distance} км за {distance/speed:.2f} ч.")
#
#
# class Truck:
#     def move(self, distance):
#         speed = 60
#         print(f"Грузовик проедет {distance} км за {distance/speed:.2f} ч.")
#
#
# class Bicycle:
#     def move(self, distance):
#         speed = 20
#         print(f"Велосипед проедет {distance} км за {distance/speed:.2f} ч.")
#
#
# def simulate_transport(transport_list, distance):
#     for t in transport_list:
#         t.move(distance)
#
#
# simulate_transport([Car(), Truck(), Bicycle()], 120)
#
#
# # -----------------------------
# class Student:
#     def access_portal(self):
#         print("Студент: может видеть расписание и оценки.")
#
#
# class Teacher:
#     def access_portal(self):
#         print("Преподаватель: может выставлять оценки.")
#
#
# class Administrator:
#     def access_portal(self):
#         print("Администратор: управляет пользователями и курсами.")
#
#
# users = [Student(), Teacher(), Administrator()]
# for u in users:
#     u.access_portal()
