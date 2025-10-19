from abc import ABC, abstractmethod

class Account:
    def __init__(self, number, balance, pin):
        self.__balance = balance
        self.__number = number
        self.__pin = pin
        
    def __check_pin(self, pin):
        if pin != self.__pin:
            raise PermissionError("Неверный PIN")
        
    def deposit(self, amount, pin):
        self.__check_pin(pin)
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть положительной :)')
        self.__balance += amount
        return self.__balance
    
    
        
    def withdraw(self, amount, pin):
        self.__check_pin(pin)
        if amount <= 0:
            raise ValueError('Сумма снятия должна быть положительной')
        if amount > self.__balance:
            raise ValueError('Недостаточно средств')
        self.__balance -= amount
        return self.__balance
    
    def get_balance(self, pin):
        self.__check_pin(pin)
        return self.__balance


    if __name__ == "__main__":
        acc = Account("12345", 87999, 2566)
        
        print("\nВыберите действие: ")
        print("1 - Пополнить счёт")
        print("2 - Снять деньги")
        print("3 - Проверить баланс")
        print("q - Выйти")
            
        choice = input("Введите команду: ")
            
            
    pin = int(input("Введите PIN: "))
        
    try:
            if choice == "1":
                amount = float(input("Сумма для пополнения: "))
                print(f"Новый баланс: {acc.deposit(amount, pin)}")
            elif choice == "2":
                amount = float(input("Сумма для снятия: "))
                print(f"Новый баланс: {acc.withdraw(amount, pin)}")
            elif choice == "3":
                print(f"Текущий баланс: {acc.get_balance(pin)}")
            else:
                print("Неверная команда, попробуйте снова.")
                
    except Exception as e:
            print("Ошибка:", e)


    class Product:
        def __init__(self, price):
            self.price = price
            self.__discount_percent = 0
    
        def set_discount(self, percent):
            if percent < 0:
                raise ValueError('Скидка не может быть отрицательным')
            if percent == 100:
                self.__discount_percent = percent
                
        def final_price(self):
            return self.__price * (1 - self.__discount_percent / 100)
        
        # Course
        
class SmartWatch:
    def __init__(self, battery=100):
        self.__battery = battery

    def use(self, minutes):
        decrease = minutes / 10  # 1% за каждые 10 минут
        self.__battery = max(0, self.__battery - decrease)
        print(f"Использовано {minutes} минут, заряд теперь {self.get_battery()}%")

    def charge(self, percent):
        if percent < 0:
            raise ValueError("Нельзя отрицательно заряжать")
        self.__battery = min(100, self.__battery + percent)
        print(f"Зарядка на {percent}%, заряд теперь {self.get_battery()}%")

    def get_battery(self):
        return round(self.__battery, 2)


    if __name__ == "__main__":
        watch = SmartWatch(50)

        while True:
            print("\nВыберите действие: ")
            print("1 - Использовать часы")
            print("2 - Зарядить часы")
            print("3 - Проверить заряд")
            print("q - Выйти")

            choice = input("Введите команду: ")

            if choice == "q":
                print("Выход из программы...")
                break

            try:
                if choice == "1":
                    minutes = float(input("Сколько минут использовать: "))
                    watch.use(minutes)
                elif choice == "2":
                    percent = float(input("На сколько % зарядить: "))
                    watch.charge(percent)
                elif choice == "3":
                    print(f"Текущий заряд: {watch.get_battery()}%")
                else:
                    print("Неверная команда, попробуйте снова.")
            except Exception as e:
                print("Ошибка:", e)


            
            # SmartWatch
                
                    
    
    # Transport
    
class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def travel_time(self, distance):
        if self.speed <= 0:
            raise ValueError("Скорость должна быть больше нуля")
        return distance / self.speed


    class Bus(Transport):
        pass  # стандартное travel_time


    class Train(Transport):
        pass  # стандартное travel_time


    class Airplane(Transport):
        def travel_time(self, distance):
            base_time = super().travel_time(distance)
            return base_time * 0.8  # перелёт быстрее на 20%


if __name__ == "__main__":
    bus = Bus(60, 50)
    train = Train(120, 200)
    plane = Airplane(800, 150)

    distance = float(input("Введите дистанцию в км: "))

    print(f"Время в пути автобусом: {bus.travel_time(distance):.2f} часов")
    print(f"Время в пути поездом: {train.travel_time(distance):.2f} часов")
    print(f"Время в пути самолётом: {plane.travel_time(distance):.2f} часов")

    # Order
    
    
class Order:
    def __init__(self, items):
        self.items = items  # список кортежей: [("Пицца", 500), ("Сок", 100)]
        self.service_fee = 0

    def calculate_total(self):
        total = sum(price for _, price in self.items)
        return total + self.service_fee


class DineInOrder(Order):
    def calculate_total(self):
        total = super().calculate_total()
        return total * 1.10  # чаевые 10%


class TakeAwayOrder(Order):
    def calculate_total(self):
        total = super().calculate_total()
        return total * 1.05  # упаковка 5%


class DeliveryOrder(Order):
    def calculate_total(self):
        total = super().calculate_total()
        return total * 1.15  # доставка +10%, упаковка +5%
    

if __name__ == "__main__":
    items = [("Пицца", 600), ("Кофе", 200)]
    
    dine_in = DineInOrder(items)
    takeaway = TakeAwayOrder(items)
    delivery = DeliveryOrder(items)
    
    print(f"Заказ в ресторане: {dine_in.calculate_total():.2f} сом")
    print(f"Навынос: {takeaway.calculate_total():.2f} сом")
    print(f"Доставка: {delivery.calculate_total():.2f} сом")



# Charecter 
    
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        raise NotImplementedError("Метод attack() должен быть реализован в подклассе")

    def __str__(self):
        return f"{self.name} — Здоровье: {self.health}, Атака: {self.attack_power}"


class Warrior(Character):
    def attack(self):
        return f"{self.name} атакует мечом с силой {self.attack_power}!"


class Mage(Character):
    def attack(self):
        return f"{self.name} использует магию и наносит {self.attack_power} урона!"


class Archer(Character):
    def attack(self):
        return f"{self.name} стреляет из лука и наносит {self.attack_power} урона!"


if __name__ == "__main__":
    characters = [
        Warrior("Артур", 100, 25),
        Mage("Мерлин", 80, 40),
        Archer("Робин", 90, 30)
    ]

    for hero in characters:
        print(hero)
        print(hero.attack())
        print("-" * 40)


# Media File
    
class MediaFile:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        raise NotImplementedError("Метод play() должен быть реализован в подклассе")


class AudioFile(MediaFile):
    def play(self):
        return f"🎵 Воспроизводится аудио: '{self.title}' ({self.duration} мин)"


class VideoFile(MediaFile):
    def play(self):
        return f"🎬 Воспроизводится видео: '{self.title}' с изображением ({self.duration} мин)"


class Podcast(MediaFile):
    def play(self):
        return f"🎙️ Воспроизводится подкаст-эпизод: '{self.title}' ({self.duration} мин)"


if __name__ == "__main__":
    playlist = [
        AudioFile("Linkin Park - Numb", 4),
        VideoFile("Inception Trailer", 3),
        Podcast("Python Talks #12", 45)
    ]

    for media in playlist:
        print(media.play())


# Payment System

from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        print(" Оплата {amount} сом через кредитную карту...")
        commission = amount * 0.02
        total = amount + commission
        print("Комиссия 2% ({commission:.2f} сом). Итог: {total:.2f} сом")
        return total


class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        print(" Оплата {amount} сом в криптовалюте...")
        discount = amount * 0.05
        total = amount - discount
        print("Скидка 5% ({discount:.2f} сом). Итог: {total:.2f} сом")
        return total


class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        print(f" Перевод {amount} сом через банковский счёт...")
        fee = 50
        total = amount + fee
        print("Фиксированная комиссия {fee} сом. Итог: {total:.2f} сом")
        return total


if __name__ == "__main__":
    print("\n=== Система оплаты ===")
    print("1 - Кредитная карта")
    print("2 - Криптовалюта")
    print("3 - Банковский перевод")
    print("q - Выйти")

    while True:
        choice = input("\nВыберите способ оплаты: ")

        if choice == "q":
            print("Выход из системы оплаты...")
            break

        try:
            amount = float(input("Введите сумму для оплаты: "))

            if choice == "1":
                payment = CreditCardPayment()
            elif choice == "2":
                payment = CryptoPayment()
            elif choice == "3":
                payment = BankTransfer()
            else:
                print("Неверная команда. Попробуйте снова.")
                continue

            total = payment.process_payment(amount)
            print(f"✅ Платёж успешно выполнен. Итоговая сумма: {total:.2f} сом")

        except Exception as e:
            print("Ошибка:", e)

# Animals

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Lion(Animal):
    def eat(self):
        return " Лев ест мясо, охотясь на добычу."
    
    def sleep(self):
        return "Лев спит днём в тени, отдыхая после охоты."


class Elephant(Animal):
    def eat(self):
        return " Слон ест траву, листья и фрукты."
    
    def sleep(self):
        return "Слон спит стоя, короткими промежутками."


class Snake(Animal):
    def eat(self):
        return " Змея заглатывает добычу целиком."
    
    def sleep(self):
        return "Змея спит, свернувшись кольцом."


if __name__ == "__main__":
    animals = {
        "1": Lion(),
        "2": Elephant(),
        "3": Snake()
    }

    print("\n=== Мир животных ===")
    print("1 - Лев")
    print("2 - Слон")
    print("3 - Змея")
    print("q - Выйти")

    while True:
        choice = input("\nВыберите животное: ")

        if choice == "q":
            print("Выход из программы...")
            break

        if choice not in animals:
            print("Неверный выбор, попробуйте снова.")
            continue

        animal = animals[choice]
        print(animal.eat())
        print(animal.sleep())



#  Documents

from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def save(self):
        pass


class WordDocument(Document):
    def open(self):
        return "Word-документ открыт."
    
    def edit(self):
        return "Вы редактируете текст в Word-документе..."
    
    def save(self):
        return "Word-документ сохранён успешно."


class PdfDocument(Document):
    def open(self):
        return " PDF-документ открыт в режиме чтения."
    
    def edit(self):
        return "PDF нельзя редактировать напрямую (только через специальные программы)."
    
    def save(self):
        return "PDF-документ сохранён без изменений."


class SpreadsheetDocument(Document):
    def open(self):
        return "Таблица открыта."
    
    def edit(self):
        return "Вы изменяете формулы и данные в ячейках..."
    
    def save(self):
        return "Таблица сохранена успешно."


if __name__ == "__main__":
    docs = {
        "1": WordDocument(),
        "2": PdfDocument(),
        "3": SpreadsheetDocument()
    }

    print("\n=== Работа с документами ===")
    print("1 - Word-документ")
    print("2 - PDF-документ")
    print("3 - Таблица (Spreadsheet)")
    print("q - Выйти")

    while True:
        choice = input("\nВыберите тип документа: ")

        if choice == "q":
            print("Выход из программы...")
            break

        if choice not in docs:
            print("Неверный выбор, попробуйте снова.")
            continue

        doc = docs[choice]
        print(doc.open())
        print(doc.edit())
        print(doc.save())


# Quizz
 
from abc import ABC, abstractmethod

class Lesson(ABC):
    @abstractmethod
    def start(self):
        pass


class VideoLesson(Lesson):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def start(self):
        return f" Урок '{self.title}' начинается! Длительность: {self.duration} мин. Воспроизводится видео."


class QuizLesson(Lesson):
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def start(self):
        return f" Урок '{self.title}' начинается! Вопросов: {len(self.questions)}. Готовьтесь отвечать."


class TextLesson(Lesson):
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def start(self):
        return f" Урок '{self.title}' начинается! Страниц для чтения: {self.pages}."


if __name__ == "__main__":
    lessons = [
        VideoLesson("Python Основы", 15),
        QuizLesson("Тест по Python", ["Вопрос 1", "Вопрос 2"]),
        TextLesson("Теория Python", 10)
    ]

    print("\n=== Старт уроков ===")
    for lesson in lessons:
        print(lesson.start())

# sms

class Notification:
    def send(self, message):
        raise NotImplementedError("Метод send() должен быть реализован в подклассе")


class EmailNotification(Notification):
    def send(self, message):
        print(f" Отправка Email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f" Отправка SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f" Push-уведомление: {message}")


if __name__ == "__main__":
    notifications = [EmailNotification(),SMSNotification(),PushNotification()]

    message = input("Введите сообщение для отправки: ")

    print("\n=== Отправка уведомлений ===")
    for notif in notifications:
        notif.send(message)

# Shapes 

import math

class Shape:
    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть реализован в подклассе")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    shapes = [
        Square(5),
        Circle(3),
        Triangle(3, 4, 5)
    ]

    print("\n=== Периметры фигур ===")
    for shape in shapes:
        print(f"{shape.__class__.__name__}: {shape.perimeter():.2f}")


# Developers

class Employee:
    def work(self):
        raise NotImplementedError("Метод work() должен быть реализован в подклассе")


class Manager(Employee):
    def work(self):
        return "Менеджер планирует задачи и контролирует команду."


class Developer(Employee):
    def work(self):
        return "Разработчик пишет код и решает технические задачи."


class Designer(Employee):
    def work(self):
        return "Дизайнер создаёт макеты и визуальные решения."


if __name__ == "__main__":
    employees = [
        Manager(),
        Developer(),
        Designer()
    ]

    print("\n=== Рабочий день сотрудников ===")
    for emp in employees:
        print(f"{emp.__class__.__name__}: {emp.work()}")
