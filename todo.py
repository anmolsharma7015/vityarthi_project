tasks = []

def menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. List Tasks")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")

def edit_task():
    if tasks:
        list_tasks()
        try:
            task_index = int(input("Enter task index to edit: ")) - 1
            if 0 <= task_index < len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_index] = new_task
                print("Task edited successfully.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to edit.")

def delete_task():
    if tasks:
        list_tasks()
        task_index = int(input("Enter task index to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")
    else:
        print("No tasks to delete.")

def list_tasks():
    if tasks:
        print("\nYour Tasks")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
    else:
        print("No tasks in the list.")

while True:
    menu()
    choice = input("Select an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        edit_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        list_tasks()
    elif choice == '5':
        print("Exiting To-Do app.")
        break
    else:
        print("Invalid choice. Please try again.")