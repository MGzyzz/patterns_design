class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0
        self.mood = 0
        self.health = 0

    def __str__(self):
        return f'Имя: {self.name}, Возвраст {self.age}, Характеристики: Сытость: {self.hunger}, Настроение: {self.mood}, Здоровье: {self.health}'



class Main:
    while True:
        name = input('Введите имя: ')
        age = input('Введите возвраст')
        check = Animal(name, age)
        print(check)

if __name__ == '__main__':
    Main()