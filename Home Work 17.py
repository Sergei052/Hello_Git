# Задача 1. Написать функцию, которая заполняет массив длинной 10 элементов,
# случайными числами в диапазоне, указанном пользователем с клавиатуры.
# Функция должна принимать два аргумента – начало диапазона и его конец, при этом ничего не возвращать.
import random


def array(a, b):
    initial = [random.randint(a, b) for _ in range(10)]
    print(initial)


a_1 = int(input('Введите нижнюю границу диапазона - '))
b_1 = int(input('Введите верхнюю границу диапазона - '))
array(a_1, b_1)


# Задача 2. Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def second(sec):
    day = sec // 86400
    sec %= 86400
    hour = sec // 3600
    sec %= 3600
    minute = sec // 60
    sec %= 60
    return "Дни: %2d Часы: %2d Минуты: %2d Секунды: %2d" % (day, hour, minute, sec)


seconds = int(input('Введите количество секунд: '))
print(second(seconds))


# Задача 3. Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить с клавиатуры.
def counting_vowels_consonants(t):
    vowels = 0  # гласные
    consonants = 0  # согласные
    for i in t:
        if type(i) is str:
            if i in "aeoiuyауоеияюёэы":
                vowels += 1
            else:
                consonants += 1
    return "Гласных - %2d, Согласных - %2d" % (vowels, consonants)


text = input('Введите строку: ')
print(counting_vowels_consonants(text))


# Задача 4. Функцию которая при заданном целом числе n посчитает n + nn + nnn.
def semi_progression(n):
    nu = n + n
    num = nu + n
    return int(n) + int(nu) + int(num)


number = input('Введите число: ')
print(semi_progression(number))


# Задача 5. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
def func(a):
    if type(a) is tuple:
        c = ','.join(a)
        return len(c)

    elif type(a) is list:
        total = 0
        for i in a:
            if type(i) is str:
                if i.isalpha():
                    for _ in i:
                        total += 1
                elif i.isdigit():
                    for _ in i:
                        total += 1
            elif type(i) is int:
                total += 1
        return total

    elif type(a) is int:
        odd = 0
        while a > 0:
            if a % 2 != 0:
                odd += 1
            a = a // 10
        return odd

    elif type(a) is str:
        count = 0
        for i in a:
            if i.isalpha():
                count += 1
        return count


while True:
    request = input('Что передать в функцию: 1 - кортеж; 2 - список; 3 - число; 4 - строку; 0 - выход - ')
    if request == '1':
        data = ('one', 'two', 'hello', 'world')
        print(func(data))
    elif request == '2':
        data = [15, 48, 'hello', 6, 19, 'world']
        print(func(data))
    elif request == '3':
        data = 135298
        print(func(data))
    elif request == '4':
        data = 'g3hg7hytf1'
        print(func(data))
    elif request == '0':
        break

