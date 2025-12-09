import json
import os


FILENAME = "tasks.json"


def load_tasks():

    if not os.path.exists(FILENAME):
        return []

    try:

        with open(FILENAME, "r") as f:
            tasks = json.load(f)
            return tasks
    except:

        return []


def save_tasks(tasks):

    with open(FILENAME, "w") as f:

        json.dump(tasks, f, ensure_ascii=False, indent=4)


def view_tasks(tasks):

    if len(tasks) == 0:
        print("Список задач пуст.")
        return

    print("\nВаши задачи:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} — [{task['priority']}]")


def add_task(tasks):

    title = input("Введите название задачи: ")

    priority = input("Введите приоритет (Низкий/Средний/Высокий): ")

    new_task = {"title": title, "priority": priority}

    tasks.append(new_task)

    save_tasks(tasks)

    print("Задача добавлена!")


def delete_task(tasks):

    if len(tasks) == 0:
        print("Нет задач для удаления.")
        return


    view_tasks(tasks)


    num_text = input("\nВведите номер задачи для удаления: ")

    try:

        num = int(num_text)


        if num < 1 or num > len(tasks):
            print("Некорректный номер задачи!")
            return


        deleted_task = tasks.pop(num - 1)


        save_tasks(tasks)

        print(f"Задача '{deleted_task['title']}' удалена!")

    except ValueError:
        print("Ошибка: нужно ввести число!")


def main():

    print("Добро пожаловать в менеджер задач!")


    tasks = load_tasks()


    while True:
        print("\n=== МЕНЮ ===")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("0. Выйти")


        choice = input("Ваш выбор: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Попробуйте еще раз.")



if __name__ == "__main__":
    main()