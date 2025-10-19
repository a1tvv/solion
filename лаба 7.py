# Суперклас
class Animal:
    def __init__(self, name, habitat, food):
        self.name = name
        self.habitat = habitat
        self.food = food

    def make_sound(self):
        return f"{self.name} издает звук."

    def __str__(self):
        return f"Животное: {self.name}\nСреда обитания: {self.habitat}\nПитание: {self.food}"



class Mammal(Animal):
    def __init__(self, name, habitat, food, has_fur):
        super().__init__(name, habitat, food)
        self.has_fur = has_fur

    def feed_babies(self):
        return f"{self.name} кормит своих детенышей молоком."

    def __str__(self):
        fur_status = "есть шерсть" if self.has_fur else "шерсти нет"
        return super().__str__() + f"\nОсобенность: {fur_status}"


class Reptile(Animal):
    def __init__(self, name, habitat, food, is_venomous):
        super().__init__(name, habitat, food)
        self.is_venomous = is_venomous

    def bask_in_sun(self):
        return f"{self.name} любит греться на солнце."

    def __str__(self):
        venom_status = "ядовитое" if self.is_venomous else "не ядовитое"
        return super().__str__() + f"\nОсобенность: {venom_status}"


#  Объекты животных 
lion = Mammal(name="Лев", habitat="Саванна", food="Мясо", has_fur=True)
snake = Reptile(name="Кобра", habitat="Джунгли", food="Грызуны", is_venomous=True)

print(lion)
print(lion.feed_babies())
print()
print(snake)
print(snake.bask_in_sun())
print()


#  Класс зу шоу
class Zoo_show:
    def __init__(self):
        self.shows = {
            1: {"name": "Шоу львов", "price": 500, "description": "Мощные львы показывают охотничьи навыки."},
            2: {"name": "Шоу рептилий", "price": 400, "description": "Редкие змеи и ящерицы демонстрируют трюки."},
            3: {"name": "Ночное сафари", "price": 700, "description": "Ночное шоу с хищниками и световыми эффектами."}
        }

    def show_info(self):
        print("Добро пожаловать в Зоопарк!\nДоступные шоу:\n")
        for key, show in self.shows.items():
            print(f"{key}. {show['name']}\n   {show['description']}\n   Цена билета: {show['price']} сом\n")

    def choose_ticket(self):
        while True:
            try:
                choice = int(input("Введите номер шоу, которое хотите посетить: "))
                if choice in self.shows:
                    selected = self.shows[choice]
                    print(f"\nВы выбрали: {selected['name']}")
                    print(f"Описание: {selected['description']}")
                    print(f"Стоимость билета: {selected['price']} сом")
                    break 
                else:
                    print("Такого шоу нет. Попробуйте снова.\n")
            except ValueError:
                print("Ошибка! Введите, пожалуйста, число.\n")


# Пример работы 
zoo = Zoo_show()
zoo.show_info()
zoo.choose_ticket()
