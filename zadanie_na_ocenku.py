#Переменные и типы данных (int, float, str, bool)
#Задание 1. Приветствие пользователя
#name = "Александр"
#print(f"Привет, ", name,"!")

#Задание 2. Возраст и год рождения
#age = 18
#birth_year = 2007
#print(f"Тебе",age, "лет. Значит ты родился в",birth_year, "году")

#Задание 3. Площадь прямоугольника
#a=2
#b=3
#S=a*b
#print(S)

#Задание 4. Конвертер температуры
#celsius = float(input("Введите температуру в градусах Цельсия: "))
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius}°C = {fahrenheit}°F")

#Задание 5. Среднее арифметическое
#num1 = float(input("Введите первое число: "))
#num2 = float(input("Введите второе число: "))
#num3 = float(input("Введите третье число: "))
#average = (num1 + num2 + num3) / 3
#print(average)

#Задание 6. Проверка чётности числа
#number = int(input("Введите целое число: "))
#if number % 2 == 0:
#    print("Число чётное")
#else:
#    print("Число нечётное")

#Задание 7. Булевы выражения
#is_student = True
#has_homework = False
#print(is_student and has_homework)
#print(is_student or has_homework)
#print(not is_student)

#Задание 8. Конкатенация строк
#first_name = "Александр"
#last_name = "Мазитов"
#print(last_name + " " + first_name)

#Задание 9. Перевод чисел в строки и обратно
#num_str = "123"
#num_int = int(num_str)
#num_added = num_int + 10
#num_str_again = str(num_added)
#print(type(num_str), type(num_int), type(num_str_again))

#Задание 10. Проверка логина и пароля
#login = "admin"
#password = "12345"
#user_login = input("Введите логин: ")
#user_password = input("Введите пароль: ")
#if user_login == login and user_password == password:
#    print("Доступ разрешён")
#else:
#    print("Неверный логин или пароль")

#Условные операторы (if, else, elif)
#Задание 1. Проверка числа на положительность
#num = float(input("Введите число: "))
#if num > 0:
#    print("Число положительное")
#elif num < 0:
#    print("Число отрицательное")
#else:
#    print("Это ноль")

#Задание 2. Возраст и доступ
#age = int(input("Введите возраст: "))
#if age < 18:
#    print("Доступ запрещён")
#else:
#    print("Доступ разрешён")

#Задание 3. Минимум из двух чисел
#a = float(input("Введите первое число: "))
#b = float(input("Введите второе число: "))
#if a < b:
#    print(f"Меньшее число: {a}")
#elif b < a:
#    print(f"Меньшее число: {b}")
#else:
#    print("Числа равны")

#Задание 4. Проверка чётности и кратности
#num = int(input("Введите число: "))
#if num % 2 == 0:
#    print("Число чётное")
#else:
#    print("Число нечётное")
#if num % 5 == 0:
#    print("Число делится на 5")
#else:
#    print("Число не делится на 5")

#Задание 5. Определение сезона по номеру месяца
#month = int(input("Введите номер месяца (1-12): "))
#if month in [12, 1, 2]:
#    print("Зима")
#elif month in [3, 4, 5]:
#    print("Весна")
#elif month in [6, 7, 8]:
#    print("Лето")
#elif month in [9, 10, 11]:
#    print("Осень")
#else:
#    print("Неверный номер месяца")

#Задание 6. Проверка логина и пароля
#login = "admin"
#password = "qwerty"
#user_login = input("Введите логин: ")
#user_password = input("Введите пароль: ")
#if user_login == login and user_password == password:
#    print("Добро пожаловать!")
#else:
#    print("Ошибка доступа")

#Задание 7. Калькулятор двух чисел
#num1 = float(input("Введите первое число: "))
#num2 = float(input("Введите второе число: "))
#operation = input("Введите операцию (+, -, *, /): ")
#if operation == "+":
#    print(f"Результат: {num1 + num2}")
#elif operation == "-":
#    print(f"Результат: {num1 - num2}")
#elif operation == "*":
#    print(f"Результат: {num1 * num2}")
#elif operation == "/":
#    if num2 != 0:
#        print(f"Результат: {num1 / num2}")
#    else:
#        print("Ошибка: деление на ноль")
#else:
#    print("Ошибка: неверная операция")

#Задание 8. Определение оценки по баллам
#score = int(input("Введите количество баллов (0-100): "))
#if 90 <= score <= 100:
#    print("Отлично")
#elif 75 <= score <= 89:
#    print("Хорошо")
#elif 50 <= score <= 74:
#    print("Удовлетворительно")
#elif 0 <= score < 50:
#    print("Неудовлетворительно")
#else:
#    print("Некорректные баллы")

#Задание 9. Проверка високосного года
#year = int(input("Введите год: "))
#if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#    print("Год високосный")
#else:
#    print("Год не високосный")

#Задание 10. Определение типа треугольника
#a = float(input("Введите сторону 1: "))
#b = float(input("Введите сторону 2: "))
#c = float(input("Введите сторону 3: "))
#if a == b == c:
#    print("Равносторонний")
#elif a == b or b == c or a == c:
#    print("Равнобедренный")
#else:
#    print("Разносторонний")

#Циклы (for, while)
#Задание 1. Счёт от 1 до 10
#for i in range(1, 11):
#    print(i)

#Задание 2. Сумма чисел от 1 до N
#N = int(input("Введите число N: "))
#total = 0
#for i in range(1, N+1):
#    total += i
#print(f"Сумма чисел от 1 до {N} равна {total}")

#Задание 3. Таблица умножения
#num = int(input("Введите число для таблицы умножения: "))
#for i in range(1, 11):
#    print(f"{num} × {i} = {num * i}")

#Задание 4. Обратный отсчёт
#count = 10
#while count > 0:
#    print(count)
#    count -= 1
#print("Старт!")

#Задание 5. Подсчёт чётных чисел
#start = int(input("Введите начало диапазона: "))
#end = int(input("Введите конец диапазона: "))
#count_even = 0
#for i in range(start, end + 1):
#    if i % 2 == 0:
#        count_even += 1
#print(f"Чётных чисел в диапазоне: {count_even}")

#Задание 6. Угадай число
#import random
#secret = random.randint(1, 10)
#guess = None
#while guess != secret:
#    guess = int(input("Угадайте число от 1 до 10: "))
#    if guess == secret:
#        print("Поздравляем! Вы угадали.")
#    else:
#        print("Неверно, попробуйте снова.")

#Задание 7. Факториал числа
#n = int(input("Введите число для факториала: "))
#factorial = 1
#for i in range(1, n+1):
#    factorial *= i
#print(f"{n}! = {factorial}")

#Задание 8. Сумма цифр числа
#number = input("Введите целое число: ")
#digit_sum = 0
#for digit in number:
#    digit_sum += int(digit)
#print(f"Сумма цифр числа: {digit_sum}")

#Задание 9. Рисуем треугольник из звёздочек
#n = int(input("Введите высоту треугольника: "))
#for i in range(1, n+1):
#    print("*" * i)

#Задание 10. Математическая викторина
#import random
#correct = 0
#for _ in range(5):
#    a = random.randint(1, 10)
#    b = random.randint(1, 10)
#    answer = int(input(f"Сколько будет {a} + {b}? "))
#    if answer == a + b:
#        print("Верно!")
#        correct += 1
#    else:
#        print("Ошибка!")
#print(f"Вы ответили правильно на {correct} из 5 вопросов.")

#Функции (def, return, параметры, аргументы)
#Задание 1. Приветствие пользователя
#def greet():
#    name = input("введите ваше имя")
#    print(f"Привет, {name}!")

#Задание 2. Сумма двух чисел
#def add(a, b):
#    return a + b

#print(add(5, 7))

#Задание 3. Возведение числа в степень
#def power(base, exponent):
#    return base ** exponent

#print(power(2, 3))

#Задание 4. Проверка чётности
#def is_even(num):
#    return num % 2 == 0

#print(is_even(4))

#Задание 5. Максимум из трёх чисел
#def max_of_three(a, b, c):
#    max_num = a
#    if b > max_num:
#        max_num = b
#    if c > max_num:
#        max_num = c
#    return max_num

#Задание 6. Преобразование температуры
#def c_to_f(c):
#    return (c * 9/5) + 32

#def f_to_c(f):
#    return (f - 32) * 5/9

#print(c_to_f(0))
#print(f_to_c(32))

#Задание 7. Подсчёт гласных в слове
#def count_vowels(word):
#    vowels = 'аеёиоуыэюя'
#    count = 0
#    for char in word.lower():
#        if char in vowels:
#            count += 1
#    return count

#Задание 8. Таблица умножения
#def multiplication_table(n):
#    for i in range(1, 11):
#        print(f"{n} × {i} = {n * i}")

#Задание 9. Факториал (через функцию)
#def factorial(n):
#    result = 1
#    for i in range(1, n + 1):
#        result *= i
#    return result

#print(factorial(5))

#Задание 10. Калькулятор
#def calculator(a, b, op):
#    if op == '+':
#        return a + b
#    elif op == '-':
#        return a - b
#    elif op == '*':
#        return a * b
#    elif op == '/':
#        if b != 0:
#            return a / b
#        else:
#            return "Ошибка: деление на ноль"
#    else:
#        return "Ошибка: неверная операция"
#
#print(calculator(10, 2, '/'))

#Работа со строками
#Задание 1. Длина строки
#string = input("Введите строку: ")
#print(len(string))

#Задание 2. Преобразование регистра
#string = input("Введите строку: ")
#print("Верхний регистр:", string.upper())
#print("Нижний регистр:", string.lower())

#Задание 3. Конкатенация строк
#first_name = input("Введите имя: ")
#last_name = input("Введите фамилию: ")
#full_name = first_name + " " + last_name
#print(full_name)

#Задание 4. Индексация
#string = input("Введите строку: ")
#middle_index = len(string) // 2
#print(string[0])
#print(string[-1])
#print(string[middle_index])

#Задание 5. Срезы
#string = input("Введите строку: ")
#print(string[:3])
#print(string[-3:])
#print(string[1:-1])

#Задание 6. Поиск подстроки
#string = input("Введите строку: ")
#substring = input("Введите подстроку: ")
#print(substring in string)

#Задание 7. Замена символов
#string = input("Введите строку: ")
#print(string.replace(" ", "_"))

#Задание 8. Разделение и объединение строк
#sentence = input("Введите предложение: ")
#words = sentence.split()
#print(",".join(words))

#Задание 9. Подсчёт символов
#string = input("Введите строку: ")
#char = input("Введите символ для подсчёта: ")
#print(f"Символ '{char}' встречается {string.count(char)} раз(а)")

#Задание 10. Обработка чисел в строке
#numbers_str = input("Введите числа через пробел: ")
#numbers = numbers_str.split()
#total = 0
#for num in numbers:
#    total += int(num)
#print(total)

#Ввод/вывод (input, print)
#Задание 1. Приветствие пользователя
#name = input("[translate:Введите ваше имя:] ")
#print(f"Привет, {name}!")

#Задание 2. Возраст и год рождения
#age = int(input("[translate:Введите ваш возраст:] "))
#birth_year = 2025 - age
#print(f"Вы родились примерно в {birth_year} году.")

#Задание 3. Сумма двух чисел
#num1 = int(input("[translate:Введите первое число:] "))
#num2 = int(input("[translate:Введите второе число:] "))
#print(f"{num1} + {num2} = {num1 + num2}")

#Задание 4. Средний балл
#grades_str = input(#"Введите три оценки через запятую: ")
#grades = [int(x.strip()) for x in grades_str.split(",")]
#average = sum(grades) / len(grades)
#print(f"Средний балл: {average}")

#Задание 5. Преобразование строки
#s = input("Введите строку: ")
#print(f"Длина: {len(s)}")
#print(f"В верхнем регистре: {s.upper()}")
#print(f"В нижнем регистре: {s.lower()}")

#Задание 6. Конвертер валют
#euros = float(input("Введите сумму в евро: "))
#rubles = euros * 100
#print(f"{euros} евро = {int(rubles)} рублей")

#Задание 7. Форматированный вывод
#name = input("Введите имя: ")
#age = input("Введите возраст: ")
#city = input("Введите город: ")
#print(f"Меня зовут {name}, мне {age} года, я из города {city}.")

#Задание8. Калькулятор возраста
#current_year = int(input("Введите текущий год: "))
#birth_year = int(input("Введите год рождения: "))
#age = current_year - birth_year
#print(f"Вам {age} года.")

#Задание9. Площадь прямоугольника
#length = float(input("Введите длину: "))
#width = float(input("Введите ширину: "))
#area = length * width
#print(f"Площадь прямоугольника: {area}")

#Задание10. Интерактивная анкета
#print("=== АНКЕТА ===")
#first_name = input("Введите имя: ")
#last_name = input("Введите фамилию: ")
#age = input("Введите возраст: ")
#profession = input("Введите профессию: ")
#print(f"Имя: {first_name}")
#print(f"Фамилия: {last_name}")
#print(f"Возраст: {age}")
#print(f"Профессия: {profession}")

#Ошибки и исключения (try/except)
#Задание 1. Деление чисел
#try:
#    a = float(input("Введите первое число: "))
#    b = float(input("Введите второе число: "))
#    result = a / b
#    print(f"Результат деления: {result}")
#except ZeroDivisionError:
#    print("Ошибка: деление на ноль невозможно.")

#Задание 2. Преобразование строки в число
#try:
#    num = int(input("Введите число: "))
#    print(f"Вы ввели число: {num}")
#except ValueError:
#    print("Ошибка: введено не число.")

#Задание 3. Чтение файла
#try:
#    with open("data.txt", "r") as file:
#        content = file.read()
#        print(content)
#except FileNotFoundError:
#    print("Файл не найден.")

#Задание 4. Индекс списка
#lst = [10, 20, 30, 40, 50]
#try:
#    index = int(input("Введите индекс (0-4): "))
#    print(f"Элемент списка: {lst[index]}")
#except IndexError:
#    print("Ошибка: индекс вне диапазона.")
#except ValueError:
#    print("Ошибка: введён не целочисленный индекс.")

#Задание 5. Математические операции
#try:
#    a = float(input("Введите первое число: "))
#    b = float(input("Введите второе число: "))
#    op = input("Введите операцию (+, -, *, /): ")
#    if op == '+':
#        print(f"Результат: {a + b}")
#    elif op == '-':
#        print(f"Результат: {a - b}")
#    elif op == '*':
#        print(f"Результат: {a * b}")
#    elif op == '/':
#        if b == 0:
#            print("Ошибка: деление на ноль невозможно.")
#        else:
#            print(f"Результат: {a / b}")
#    else:
#        print("Ошибка: неизвестная операция.")
#except ValueError:
#    print("Ошибка: введено не число.")

#Задание 6. Конвертация в float с повтором
#while True:
#    s = input("Введите число с плавающей запятой: ")
#    try:
#        val = float(s)
#        print(f"Вы ввели число: {val}")
#        break
#    except ValueError:
#        print("Ошибка: введено не число с плавающей запятой. Попробуйте ещё раз.")

#Задание 7. Словарь и ключ
#d = {"a": 1, "b": 2, "c": 3}
#key = input("Введите ключ (a, b, c): ")
#try:
#    print(f"Значение: {d[key]}")
#except KeyError:
#    print("Ошибка: такого ключа нет в словаре.")

#Задание 8. Деление внутри функции
#def safe_divide(a, b):
#    try:
#        return a / b
#    except ZeroDivisionError:
#        return "Ошибка: деление на ноль."
#    except TypeError:
#        return "Ошибка: неверные типы данных."

#print(safe_divide(10, 2))
#print(safe_divide(10, 0))
#print(safe_divide(10, "2"))

#Задание 9. Работа с файлом и числом
#filename = input("Введите имя файла: ")
#try:
#    with open(filename, "r") as f:
#        content = f.read().strip()
#        num = int(content)
#        print(f"Число из файла: {num}")
#except FileNotFoundError:
#    print("Ошибка: файл не найден.")
#except ValueError:
#    print("Ошибка: содержимое файла не является числом.")

#Задание 10. Обработка нескольких исключений
#try:
#    user_input = input("Введите число: ")
#    num = float(user_input)
#    result = 100 / num
#    print(int(result))
#except ZeroDivisionError:
#    print("Ошибка: деление на ноль невозможно.")
#except ValueError:
#    print("Ошибка: введено не число.")