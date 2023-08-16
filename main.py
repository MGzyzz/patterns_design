import random
from abc import ABC, abstractmethod


class AgeStrategy(ABC):
    @abstractmethod
    def apply_increase(self, value):
        pass

    @abstractmethod
    def apply_decrease(self, value):
        pass


class YoungAgeStrategy(AgeStrategy):
    def apply_increase(self, value):
        return value + 10

    def apply_decrease(self, value):
        return value - 2


class MiddleAgeStrategy(AgeStrategy):
    def apply_increase(self, value):
        return value + 5

    def apply_decrease(self, value):
        return value - 5


class OldAgeStrategy(AgeStrategy):
    def apply_increase(self, value):
        return value + 2

    def apply_decrease(self, value):
        return value - 10

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0
        self.mood = 0
        self.health = 0

        if age <= 5:
            self.age_strategy = YoungAgeStrategy()
        elif age <= 10:
            self.age_strategy = MiddleAgeStrategy()
        else:
            self.age_strategy = OldAgeStrategy()


    def __str__(self):
        return f'Имя: {self.name}, Возвраст {self.age}, Характеристики: Сытость: {self.hunger}, Настроение: {self.mood}, Здоровье: {self.health}'


    def random_numbers(self):
        numbers = random.randint(1, 100)
        if numbers <= 10:
            return True
        else:
            return False


    def feed(self):
        print(f'Вы покормили с {self.name}')
        if self.random_numbers():
            print(f'Внезапное событие. ВАШ {self.name} ОТРАВИЛСЯ!')
            self.mood = self.age_strategy.apply_decrease(self.mood)
            self.health = self.age_strategy.apply_decrease(self.health)
        else:
            self.hunger = self.age_strategy.apply_increase(self.hunger)
            self.mood = self.age_strategy.apply_increase(self.mood)
            self.health = self.age_strategy.apply_increase(self.health)
        self.info()

    def play(self):
        print(f'Вы играете с {self.name}')
        if self.random_numbers():
            print(f'Внезапное событие. ВАШ {self.name} ТРАВМИРОВАЛСЯ!')
            self.hunger = self.age_strategy.apply_decrease(self.hunger)
            self.mood = self.age_strategy.apply_decrease(self.mood)
            self.health = self.age_strategy.apply_decrease(self.health)
        else:
            self.hunger = self.age_strategy.apply_decrease(self.hunger)
            self.mood = self.age_strategy.apply_increase(self.mood)
            self.health = self.age_strategy.apply_increase(self.health)
        self.info()

    def heal(self):
        self.mood = self.age_strategy.apply_increase(self.mood)
        self.health = self.age_strategy.apply_increase(self.health)
        self.info()


    def info(self):
        return print(f'{"="*40}\nХарактеристики:\nГолод:{self.hunger}\nНастроение:{self.mood}\nЗдоровье: {self.health}\n{"="*40}')

    @staticmethod
    def check_statistics(animal):
        if animal.hunger < 0  or animal.health < 0 or animal.mood < 0:
            print('Животное погибло')
            Main.animals.remove(animal)


class Main:
    animals = []

    def run(self):
        while True:
            if not self.animals:
                print('Прежде чем начать играть, пожалуйста, создайте животное\n')
                self.add_animals()
            else:
                for idx, animal in enumerate(self.animals, start=1):
                    print(f'{"=" * 40}\n[{idx}] Имя: {animal.name}, Возраст {animal.age}\n{"=" * 40}')

                choose_animal = self.get_valid_animal_choice()

                valid_actions = ['1', '2', '3', '4']
                choose = self.get_valid_choice(
                    f'Какое действие вы хотите сделать?\n{"=" * 40}\n[1] Покормить животное\n[2] Поиграть с животным\n[3] Лечить животное\n[4] Добавить животное\n{"=" * 40}\n',
                    valid_actions
                )

                id_animal = self.animals[choose_animal]
                match choose:
                    case '1':
                        id_animal.feed()
                    case '2':
                        id_animal.play()
                    case '3':
                        id_animal.heal()
                    case '4':
                        self.add_animals()
                Animal.check_statistics(id_animal)

    def get_valid_choice(self, message, valid_choices):
        while True:
            user_input = input(message)
            if user_input in valid_choices:
                return user_input
            else:
                print('Неверный ввод. Пожалуйста, выберите корректное действие.')

    def get_valid_animal_choice(self):
        while True:
            try:
                choose_animal = int(input('\nВыберите животное из списка (введите номер): ')) - 1
                if 0 <= choose_animal < len(self.animals):
                    return choose_animal
                else:
                    print('Неверный номер. Пожалуйста, введите корректный номер.')
            except ValueError:
                print('Неверный ввод. Пожалуйста, введите номер животного.')

    def add_animals(self):
        name = input('Введите имя: ')
        age = input('Введите возвраст: ')

        if not age.isdigit():
            print('Введены неккоректные данные')
            return self.add_animals()

        animals = Animal(name, int(age))
        self.animals.append(animals)
        print('Ваше животное добавлено:')
        return self.run()


if __name__ == '__main__':
    print('Добро пожаловать в приложение.')
    Main().run()