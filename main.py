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
            print('work')
        elif age <= 10:
            self.age_strategy = MiddleAgeStrategy()
            print('work two')


        else:
            self.age_strategy = OldAgeStrategy()
            print('work three')


    def __str__(self):
        return f'Имя: {self.name}, Возвраст {self.age}, Характеристики: Сытость: {self.hunger}, Настроение: {self.mood}, Здоровье: {self.health}'


    def feed(self):
        print(f'Вы покормили с {self.name}')
        self.hunger = self.age_strategy.apply_increase(self.hunger)
        self.mood = self.age_strategy.apply_increase(self.mood)
        self.health = self.age_strategy.apply_increase(self.health)
        self.info()

    def play(self):
        self.hunger = self.age_strategy.apply_decrease(self.hunger)
        self.mood = self.age_strategy.apply_increase(self.mood)
        self.health = self.age_strategy.apply_increase(self.health)
        self.info()

    def heal(self):
        self.mood = self.age_strategy.apply_increase(self.mood)
        self.health = self.age_strategy.apply_increase(self.health)
        self.info()


    def info(self):
        return print(f'\nХарактеристики: {self.hunger}, {self.mood}, {self.health}')
class Main:
    animals = []

    def run(self):
        while True:
            print('Добро пожаловать в приложение. Пожалуйста создайте животное.')
            self.add_animals()

            for animal in self.animals:
                print(f'[1] Имя: {animal.name}, Возвраст {animal.age}')
            choose_animal = int(input('Ваше животное добавлено:\nВыберите животное из списка: ')) - 1

            if 0 <= choose_animal < len(self.animals):
                choose = input('Какое действие вы хотите сделать?\n[1]Покормить животное\n[2]Поиграть с животным\n[3]Лечить животное')
                id_animal = self.animals[choose_animal]
                match choose:
                    case '1':
                        id_animal.feed()
                    case '2':
                        id_animal.play()
                    case '3':
                        id_animal.heal()
                    case '4':
                        break
            else:
                print('Неккоректный ввод данных, попробуйте еще раз')
                return



    def add_animals(self):
        name = input('Введите имя: ')
        age = input('Введите возвраст: ')

        if not age.isdigit():
            print('Введены неккоректные данные')
            return self.add_animals()

        animals = Animal(name, int(age))
        self.animals.append(animals)


if __name__ == '__main__':
    Main().run()