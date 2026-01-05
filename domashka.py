#Списки (list)
#Задание 1. Создание и вывод списка
#numbers = [1,2,3,4,5,6,7,8,9]
#print(numbers)
#from operator import index

#Задание 2. Доступ к элементам
#numbers = [1, 2, 3, 4, 5]
#print(numbers[0])
#print(numbers[2])
#print(numbers[-1])

#Задание 3. Изменение элементов
#tanks=["T-14", "T-26", "T-72", "T-80", "T-90"]
#tanks[1]="T-64"
#print(tanks)

#Задание 4. Добавление элементов
#new_list = []
#new_list.append(1)
#new_list.append(2)
#new_list.append(3)
#print(new_list)

#Задание 5. Удаление элементов
#delete_list = [1,2,3,4,5]
#delete_list.pop(2)
#print(delete_list)

#Задание 6. Сумма и среднее
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#mean = sum(numbers) / len(numbers)
#print(sum(numbers))
#print(mean)

#Задание 7. Поиск элемента
#string_list=["car", "cat", "dog", "potato", "meat"]
#word = input("Enter a word: ")
#if word in string_list:
#    print(True)
#else:
#    print(False)

#Задание 8. Сортировка списка
#numbers = [7,3,10,92,1]
#numbers.sort()
#print(numbers)
#numbers.sort(reverse=True)
#print(numbers)

#Задание 9. Срезы списка
#list_numbers = [1,2,3,4,5,6,7,8,9,10]
#first_three = list_numbers[:3]
#print(first_three)
#last_three = list_numbers[-3:]
#print(last_three)
#numbers_with_even_index = list_numbers [::2]
#print(numbers_with_even_index)

#Задание 10. Объединение списков
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
#numbers.extend(words)
#print(numbers)

#Кортежи (tuple)

#Задание 1. Создание и вывод кортежа
#my_tuple = (1,2,"mankind","oh shit here we go again", True)
#print(my_tuple)

#Задание 2. Доступ к элементам
#words_tuple = ("ahahahah", "lil kek", "nigga", "allah akbar", "shahed")
#print(words_tuple[0])
#(words_tuple[1])
#print(words_tuple[-1])

#Задание 3. Индексация и отрицательные индексы
#somewords_tuple = ("я", "с рулетом", "на балконе")
#print(somewords_tuple[-2]
#      + somewords_tuple[-1])

#Задание 4. Подсчёт количества элементов
#repeat_tuple = (
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
#                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
#                )
#print(repeat_tuple.count(1))

#Задание 5. Поиск индекса элемента
#hz_tuple = (1,5,8,13,9,32,2)
#print(hz_tuple.index(8))

#Задание 6. Срезы кортежа
#num_tuple = (1,2,3,4,5,6,7,8,9)
#first_three = num_tuple[:3]
#print(first_three)
#last_three = num_tuple[-3:]
#print(last_three)
#numbers_with_step = num_tuple[::2]
#print(numbers_with_step)

#Задание 7. Объединение кортежей
#num_tuple1 = (1,3,5,7)
#num_tuple2 = (2,4,6,8)
#print(num_tuple1+num_tuple2)

#Задание 8. Повторение кортежа
#tuple_tutuple = (1,2,3,4,5)
#print(tuple_tutuple*3)

#Задание 9. Преобразование списка в кортеж и обратно
#numbers_list = [1, 2, 3, 4, 5]

#numbers_tuple = tuple(numbers_list)  # список → кортеж
#new_list = list(numbers_tuple)       # кортеж → список

#print(numbers_tuple)
#print(new_list)

#Задание 10. Итерация по кортежу
#fruits = ("яблоко", "банан", "вишня", "груша", "киви")
#
#for fruit in fruits:
#    print(fruit)

#Задание 1. Создание и вывод множества
#numbers = {1, 2, 3, 4, 5, 5, 1}
#print(numbers)

#Задание 2. Проверка элемента
#spisok_list={"car", "cat", "dog", "potato", "meat"}
#word = input("Enter a word: ")
#if word in spisok_list:
#    print(True)
#else:
#    print(False)

#Задание 3. Добавление элемента
#fruits ={"яблоко", "груша", "банан", "абрикос"}
#fruits.add("ананас")
#print(fruits)

#Задание 4. Удаление элемента
#fruits ={"яблоко", "груша", "банан", "абрикос"}
#fruits.remove("яблоко")
#print(fruits)

#Задание 5. Объединение множеств
#tuple1 = {1,3,5}
#tuple2 = {2,4,6}
#print(tuple1.union(tuple2))

#Задание 6. Пересечение множеств
#tuple1 = {1,2,3,5}
#tuple2 = {1,3,4,5}
#print(tuple1.intersection(tuple2))


#Задание 7. Разность множеств
#tuple1 = {1,2,3,4,5}
#tuple2 = {4,5,6,7,8}
#print(tuple1.difference(tuple2))

#Задание 8. Симметричная разность
#tuple1 = {1,2,3}
#tuple2 = {3,5,6}
#print(tuple1.symmetric_difference(tuple2))

#Задание 9. Проверка подмножества
#tuple1 = {1,2,3,4,5}
#tuple2 = {1,2,3,4,5,6,7}
#print(tuple1.issubset(tuple2))

#Задание 10. Итерация по множеству
#tuple1 = {1,2,3,4,5}
#for tuple1 in tuple1:
#    print(tuple1)

#Словари (dict)
#Задание 1. Создание и вывод словаря
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#print(student)

#Задание 2. Доступ к значениям
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#print(student["name"])
#(student["age"])

#Задание 3. Изменение значения
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#student["age"] = 26
#print(student)

#Задание 4. Добавление новой пары
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#student["hobbies"] = "Python"
#print(student)

#Задание 5. Удаление пары
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#del student["gender"]
#print(student)

#Задание 6. Проверка существования ключа
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#key = input("Enter key: ")
#if key in student:
#    print(True)
#
#else:
#    print(False)

#Задание 7. Перебор ключей и значений
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#for key in student.keys():
#    print(key)
#
#for value in student.values():
#    print(value)
#
#for key, value in student.items():
#    print(key, value)

#Задание 8. Объединение словарей
#student1 = {"name":"John", "age":25}
#student2 = {"town":"New York"}
#student1.update(student2)
#print(student1)

#Задание 9. Получение значения безопасно
#student = {"name":"John", "age":25, "gender":"Male", "town":"New York"}
#key = input("Enter key: ")
#if key in student:
#    print(student[key])
#
#else:
#    print("Key not found")

#Задание 10. Подсчёт элементов
#numbers = {"a":10, "b":20, "c":30, "d":40}
#print(sum(numbers.values()))
