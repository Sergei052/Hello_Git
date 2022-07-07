# Задача 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
def credit_card(num):
    return '*' * len(num[:-4]) + num[-4:]


number = input('Введите номер кредитной карты: ')
print(f'Скрытый номер кредитной карты: {credit_card(number)}')


# Задача 2. Напишите функцию, которая проверяет: является ли слово палиндромом.
def polindrom(phrase):
    return phrase == phrase[::-1]


text = input('Введите слово: ')
print(polindrom(text))


# Задача 3.
class Tomato:
    # статическое свойство states, которое содержит все стадии созревания помидора
    states = {0: "цветение", 1: "зелёный", 2: "молочный", 3: "оранжевый", 4: "спелый"}

    # метод __init__(), внутри определены два динамических protected свойства:
    # 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
    def __init__(self, index):
        self._index = index
        self._state = 0

    # метод grow(), который переводит томат на следующую стадию созревания
    def grow(self):
        self._change_state()

    # метод is_ripe(), который проверяет, что томат созрел
    def is_ripe(self):
        if self._state == 4:
            return True
        return False

    # Защищенные(protected) методы
    def _change_state(self):
        if self._state < 4:
            self._state += 1
        self._print_state()

    def _print_state(self):
        if self._state != 4:
            print(f'Помидор {self._index + 1} ещё {Tomato.states[self._state]}')
        elif self._state == 4:
            print(f'Помидор {self._index + 1} уже {Tomato.states[self._state]}')


class TomatoBush:
    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(num)]

    # метод grow_all(), который переводит все объекты из списка томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # метод all_are_ripe(), который возвращает True, если все томаты из списка стали спелыми
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # метод give_away_all(), который будет чистить список томатов после сбора урожая
    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    # метод __init__(), внутри определены два динамических свойства:
    # 1) name - передается параметром, является публичным и
    # 2) _plant - принимает объект класса Tomato, является protected
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
    def work(self):
        print(f'{self.name} ухаживает за растениями')
        self._plant.grow_all()
        print('И уход даёт свои плоды')

    # метод harvest(), который проверяет, все ли плоды созрели.
    # Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
    def harvest(self):
        print('Сбор урожая')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Рано собирать, помидоры ещё не созрели.')

    # статический метод knowledge_base(), который выводит в консоль справку по садоводству.
    @staticmethod
    def knowledge_base():
        print('''  Помидорам нужно тепло, и их нужно поливать. Собирайте помидоры когда они созреют.
Не собирайте незрелые помидоры. А ещё помидоры это ягоды, технически...''')


# Тесты
if __name__ == '__main__':
    # вызов справки по садоводству
    Gardener.knowledge_base()
    # создаём объекты классов TomatoBush и Gardener
    great_tomato_bush = TomatoBush(3)
    gardener = Gardener(name='Сергей', plant=great_tomato_bush)
    # ухаживаем за кустом и пытаемся собрать урожай
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.harvest()
