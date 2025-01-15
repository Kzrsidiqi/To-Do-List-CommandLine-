# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Edit Task")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task():
    view_tasks()  # Show tasks before removing
    task_number = int(input("Enter the task number to remove: "))
    if task_number > 0 and task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function to edit a task
def edit_task():
    view_tasks()  # Show tasks before editing
    task_number = int(input("Enter the task number to edit: "))
    if task_number > 0 and task_number <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_number - 1] = new_task
        print(f"Task updated to '{new_task}'")
    else:
        print("Invalid task number.")

# Main loop to run the program
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        edit_task()
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
