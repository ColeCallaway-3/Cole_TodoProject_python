import time
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

print( "Welcome to the To-Do List App!")
user = input( "What is your name user? \n")

def add_task(tasks):
    try:
        title = input( f"Enter the task title {user}: ")
        if any(task["title"].lower() == title.lower() for task in tasks):
            raise ValueError( f'Task "{title}" already exists.')
                
        # Get the due date
        due_date = input( "Enter the due date (MM-DD-YYYY): ")
        datetime.strptime(due_date, "%m-%d-%Y")  # Validate date format  

        task = {
            "title": title, 
            "status": "Incomplete", 
            "due_date": due_date
        }
        tasks.append(task)
    except ValueError as e:
        print(e)
    finally:
        print( "Returning to menu...\n")

def view_tasks(tasks):
    if not tasks:
        print( f"No tasks available, {user}.\n")
    else:
        print( "\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status_color = Fore.GREEN if task["status"] == "Complete" else Fore.RED 
            
            print( f'{idx}. {task["title"]} - {task["status"]} -  Due: {task["due_date"]}')
        print()

def mark_task_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input( f"Enter the task number to mark as complete, {user}: "))
            if not (1 <= task_num <= len(tasks)):
                raise IndexError(Fore.RED + f"Invalid task number, {user}.")
        except ValueError:
            print( f"Please enter a valid number, {user}.\n")
        except IndexError as e:
            print(e)
        else:
            tasks[task_num - 1]["status"] = "Complete"
            print( f'Task "{tasks[task_num - 1]["title"]}" was marked as complete, {user}.\n')
        finally:
            print( "Returning to menu...\n")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input( f"Enter the task number to delete, {user}: "))
            if not (1 <= task_num <= len(tasks)):
                raise IndexError( f"Invalid task number, {user}.")
        except ValueError:
            print( f"Please enter a valid number, {user}.\n")
        except IndexError as e:
            print(e)
        else:
            deleted_task = tasks.pop(task_num - 1)
            print( f'Task "{deleted_task["title"]}" was deleted, {user}.\n')
        finally:
            print( "Returning to menu...\n")

def show_menu(tasks):
    while True:
        time.sleep(2)
        print( "\nMenu:")
        print( "1. Add a task")
        print( "2. View tasks")
        print( "3. Mark a task as complete")
        print( "4. Delete a task")
        print( "5. Quit")
        time.sleep(1)
        
        try:
            choice = input(Fore.CYAN + f"Choose an option {user} (1-5): ")
            if choice not in ["1", "2", "3", "4", "5"]:
                raise ValueError(Fore.RED + f"Invalid choice, {user}. Please select a valid option.\n")
        except ValueError as e:
            print(e)
        else:
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                mark_task_complete(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print(Fore.RED + f"Exiting the To-Do List App. Goodbye, {user}!")
                time.sleep(1)
                break
        finally:
            if choice != '5':
                print(Fore.YELLOW + "Loading menu...\n")

if __name__ == "__main__":
    tasks = []  # List to store tasks
    show_menu(tasks)