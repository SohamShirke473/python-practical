
tasks = ['Go to the office', 'Pay Bills', 'Visit doctor', 'Cook the food', 'Arrange wardrobe', 'Swimming class']

def show_tasks():
    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\nTask Manager:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_tasks()

    elif choice == '2':
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added.")

    elif choice == '3':
        show_tasks()
        task_no = int(input("Enter task number to update: "))
        updated_task = input("Enter the updated task: ")
        tasks[task_no - 1] = updated_task
        print("Task updated.")

    elif choice == '4':
        show_tasks()
        task_no = int(input("Enter task number to remove: "))
        tasks.pop(task_no - 1)
        print("Task removed.")

    elif choice == '5':
        print("Exiting Task Manager.")
        break

    else:
        print("Invalid choice. Please try again.")
