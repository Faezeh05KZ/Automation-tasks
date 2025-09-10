def get_tasks_from_console():
    tasks = []
    print("Enter your tasks one by one. Type 'done' when you are finished.")
    while True:
        task = input("> ")
        if task.lower() == 'done':
            break
        if task:
            tasks.append(task)
    return tasks

def get_tasks_from_file(filename="tasks.txt"):

    try:
        with open(filename, 'r') as f:
            tasks = [line.strip() 
                     for line in f if line.strip()]
        print(f"Successfully loaded tasks from {filename}.")
        return tasks
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please create it or choose another option.")
        
        return None

def sort_and_display_tasks(tasks):
    if not tasks:
        print("\nNo tasks to sort.")
        return

    sorted_tasks = sorted(tasks, key=str.lower)
    
    print("\nYour Sorted To-Do List ")
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. {task}")
    print("----------------------------")

def main():
    print("Daily Task Sorter")
    print("How would you like to input your tasks?")
    print("1: Enter tasks manually in the console")
    print("2: Read tasks from a 'tasks.txt' file")

    choice = input("Enter your choice (1/2): ")

    tasks_list = []
    if choice == '1':
        tasks_list = get_tasks_from_console()
    elif choice == '2':
        tasks_list = get_tasks_from_file()
    else:
        print("Invalid choice!!! Please run the script again and enter 1 or 2.")
        return

    if tasks_list is not None:
        sort_and_display_tasks(tasks_list)

if __name__ == "main":
    main()