# Simple To-Do List Application

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_list():
    if not todo_list:
        print("\n✅ Your to-do list is empty!")
    else:
        print("\n📌 Your To-Do List:")
        for i, (task, status) in enumerate(todo_list, start=1):
            print(f"{i}. {task} {'✔️' if status else '❌'}")

def add_task():
    task = input("\nEnter a new task: ")
    todo_list.append([task, False])
    print(f"✅ '{task}' added to your list!")

def remove_task():
    view_list()
    try:
        task_no = int(input("\nEnter task number to remove: "))
        removed = todo_list.pop(task_no - 1)
        print(f"🗑️ '{removed[0]}' removed from your list!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number!")

def mark_done():
    view_list()
    try:
        task_no = int(input("\nEnter task number to mark as done: "))
        todo_list[task_no - 1][1] = True
        print(f"✔️ '{todo_list[task_no - 1][0]}' marked as done!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        view_list()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        print("\n👋 Exiting To-Do List. Have a productive day!")
        break
    else:
        print("⚠️ Invalid choice! Please try again.")