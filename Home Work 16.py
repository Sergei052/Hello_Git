# # Задача № 1. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# # и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
# # Номер месяца вводить с клавиатуры.
def season(mon):
    if 3 <= mon <= 5:
        print('Весна')
    elif 6 <= mon <= 8:
        print('Лето')
    elif 9 <= mon <= 11:
        print('Осень')
    elif mon == 12 or 1 <= mon <= 2:
        print('Зима')
    elif mon > 12:
        print('Неправильный номер месяца.')


month = int(input('Введите месяц: '))

season(month)


# Задача 2. Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
import random


def is_prime(n):
    print(n)
    if n < 2:
        return False
    if n == 2:
        return True
    limit = n ** 0.5
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


print(is_prime(random.randint(0, 1000)))


# Задача 3. Функция, вычисляющая среднее арифметическое элементов массива.
# Массив должен состоять из случайных чисел, длинной 10 элементов.
import random


initial = [random.randint(0, 100) for _ in range(10)]


def summa_func():
    suma = 0
    for i in initial:
        suma += i
    print(initial)
    print('Среднее арифметическое массива =', suma / len(initial))


summa_func()


# Задача 4. Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


def calculator(f, s):
    operation = input('Введите операцию(+, -, /, *): ')
    if operation == '+':
        print(f + s)
    if operation == '-':
        print(f - s)
    if operation == '*':
        print(f * s)
    try:
        if operation == '/':
            print(f / s)
    except ZeroDivisionError:
        print('На ноль делить нельзя')


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))


calculator(first, second)
