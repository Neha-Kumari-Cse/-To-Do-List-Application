

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.\n")
    else:
        print("Empty task not added.\n")

def remove_task(tasks):
    """Remove a task by number."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Task '{removed}' removed.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.\n")

if __name__ == "__main__":
    main()
