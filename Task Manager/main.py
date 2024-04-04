from Tasks import Tasks
import os

def change_status():
    os.system("clear")
    change = input("Enter the line number to change status : ")
    which_change = input("""
Update to which status :
1. Not Assigned
2. In Progress
3. Finished
""")
    return change, which_change
def edit_task():
    id = input("Enter the line number to edit : ")
    position = input("Which characteristic do you wish to modify ? (Name / Description) ")
    while position.lower() != "name" or position.lower() != "description":
        position = input("Which characteristic do you wish to modify ? (Name / Description) ")
        print("Not a valid position!")

    text = input("Text to modify : ")
    return id, text, position

def show_tasks():
    choose_show = input("""
        1. Show newly created tasks
        2. Show your tasks in progress
        3. Show your finished tasks
        4. Show all tasks
""")
    match choose_show:
        case "1":
            filter = "New"
            os.system("clear")

        case "2":
            filter = "In Progress"
            os.system("clear")

        case "3":
            filter = "Finished"
            os.system("clear")

        case "4":
            filter = "All"
            os.system("clear")
        case _:
            print("Invalid Entry")
    
    return filter

def create_task():
    name = input("Enter a name for the task : ")
    while len(name) < 3:  # or name in csv
        name = input("""Invalid Name\nEnter a valid name : """)

    short_description = input(
        "Enter a short description for the task : ")
    return name, short_description


def start_cmd():
    task = Tasks()
    while True:
        os.system("clear")
        first_input = input("""
        Hello, what do you want to do today
        
        1. Create a new task
        2. Show your tasks
        3. Change task status
        4. Delete task
        5. Quit
    """)
        match first_input:
            case "1":
                os.system("clear")
                name, short_description = create_task()
                task.create_task(name, short_description)
                print("Successfuly created a new task")
            case "2":
                os.system("clear")
                filter = ""
                while filter == "":
                    filter = show_tasks()
                task.show_tasks(filter)
                if input("Do you want to edit a task on the list ? ").lower() == "yes":
                    id, position, text = edit_task()
                    task.edit_task(id, position, text)
                    print("Successfuly edited task")
                continue 
            case "3":
                os.system("clear")
                task.show_tasks("All")
                change, which_change = change_status()
                task.edit_task(change, "Status", which_change)
            case "4":
                os.system("clear")
                task.show_tasks("All")
                to_del = input("Select task to delete : ")
                task.delete_task(to_del)
            case "5":
                os.system("clear")
                break
            case _:
                "Invalid Entry"
                continue


if __name__ == "__main__":
    start_cmd()
