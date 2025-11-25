import sqlite3

DATABASE = "tasks.db"


def init_database():

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            print("База данных инициализирована успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка при инициализации базы данных: {e}")


def load_tasks():

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, priority FROM tasks ORDER BY created_at DESC")
            tasks = cursor.fetchall()
            return tasks
    except sqlite3.Error as e:
        print(f"Ошибка при загрузке задач: {e}")
        return []


def view_tasks():

    tasks = load_tasks()

    if not tasks:
        print("Список задач пуст.")
        return

    print("\nСписок задач:")
    print("-" * 40)
    for task in tasks:
        print(f"{task[0]}. {task[1]} — [{task[2]}]")
    print("-" * 40)


def add_task():

    title = input("Введите название задачи: ").strip()
    if not title:
        print("Ошибка: название задачи не может быть пустым!")
        return

    priority = input("Введите приоритет (Низкий/Средний/Высокий): ").strip()
    valid_priorities = ["Низкий", "Средний", "Высокий"]
    if priority not in valid_priorities:
        print("Ошибка: приоритет должен быть одним из: Низкий, Средний, Высокий")
        return

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", (title, priority))
            conn.commit()
            print("Задача добавлена успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении задачи: {e}")


def delete_task():

    view_tasks()

    try:
        task_id = int(input("Введите ID задачи для удаления: "))
    except ValueError:
        print("Ошибка: введите корректный числовой ID!")
        return

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()

            if cursor.rowcount == 0:
                print("Задача с таким ID не найдена.")
            else:
                print("Задача удалена успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении задачи: {e}")


def update_task():

    view_tasks()

    try:
        task_id = int(input("Введите ID задачи для обновления: "))
    except ValueError:
        print("Ошибка: введите корректный числовой ID!")
        return

    tasks = load_tasks()
    task_ids = [task[0] for task in tasks]
    if task_id not in task_ids:
        print("Задача с таким ID не найдена.")
        return

    new_title = input("Введите новое название задачи (оставьте пустым, чтобы не менять): ").strip()
    new_priority = input(
        "Введите новый приоритет (Низкий/Средний/Высокий) (оставьте пустым, чтобы не менять): ").strip()

    if not new_title and not new_priority:
        print("Не указано ни одного поля для обновления.")
        return

    if new_priority:
        valid_priorities = ["Низкий", "Средний", "Высокий"]
        if new_priority not in valid_priorities:
            print("Ошибка: приоритет должен быть одним из: Низкий, Средний, Высокий")
            return

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()

            if new_title and new_priority:

                cursor.execute("UPDATE tasks SET title = ?, priority = ? WHERE id = ?",
                               (new_title, new_priority, task_id))
            elif new_title:

                cursor.execute("UPDATE tasks SET title = ? WHERE id = ?",
                               (new_title, task_id))
            elif new_priority:

                cursor.execute("UPDATE tasks SET priority = ? WHERE id = ?",
                               (new_priority, task_id))

            conn.commit()

            if cursor.rowcount == 0:
                print("Задача с таким ID не найдена.")
            else:
                print("Задача обновлена успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении задачи: {e}")


def main():

    print("Добро пожаловать в менеджер задач с БД!")
    init_database()

    while True:
        print("\nМеню:")
        print("1 — Просмотреть задачи")
        print("2 — Добавить задачу")
        print("3 — Удалить задачу")
        print("4 — Обновить задачу")
        print("0 — Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            update_task()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: такого пункта меню нет. Попробуйте снова.")


if __name__ == "__main__":
    main()