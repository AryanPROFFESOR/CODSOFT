import os

# Function to display the to-do list
def display_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

# Function to add a task to the to-do list
def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Added task: {task}")

# Function to update a task in the to-do list
def update_task(task_index, new_task):
    tasks = []
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
    
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_task + "\n"
        with open("todo.txt", "w") as file:
            file.writelines(tasks)
        print(f"Updated task {task_index}: {new_task}")
    else:
        print("Invalid task index. Task not updated.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    tasks = []
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
    
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        with open("todo.txt", "w") as file:
            file.writelines(tasks)
        print(f"Removed task {task_index}: {removed_task.strip()}")
    else:
        print("Invalid task index. Task not removed.")

# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        display_todo_list()
    elif choice == "2":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "3":
        display_todo_list()
        task_index = int(input("Enter the index of the task to update: "))
        new_task = input("Enter the new task: ")
        update_task(task_index, new_task)
    elif choice == "4":
        display_todo_list()
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
