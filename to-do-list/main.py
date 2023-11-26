import task_manager
from storage import Storage

storage = Storage("bd.txt")

def main():
    while True:
        print("\nДоступные операции с to-do-list:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Показать все задачи")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            task_name = input("Введите название задачи: ")
            date = input("Введите дату задачи: ")
            description = input("Введите описание задачи: ")
            status = input("Введите статус задачи: ")
            task = task_manager.Task(task_name, date, description, status)
            storage.add_task(task)
        elif choice == '2':
            task_name = input("Введите название задачи для удаления: ")
            storage.delete_task(task_name)
        elif choice == '3':
            for task in storage.get_all_tasks():
                print(task)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
