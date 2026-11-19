#day-2 assignment
tasks=[] 


def showtmenu(): # I have refactored the code to display a menu for user interaction
    print("\n--------Task Manager--------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")  


def add_task():
    task = input("Enter the task name: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():       # I have refactored the code to display tasks with their corresponding numbers for better user experience
    if len(tasks)==0:
        print("No tasks available.")
    else:
        print("\n--------Task List--------")
        for i in range(len(tasks)):
            print(i+1, ". ", tasks[i])


def delete_task():    # I have refactered the code to delete a task by its number instead of name for better user experience
    view_tasks()

    if tasks:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")


while True:   #i have refactored the code to use a while loop for continuous user interaction until they choose to exit
    showtmenu() 
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":    
        print("Thank you for using Task Manager!")
        break

  
        
