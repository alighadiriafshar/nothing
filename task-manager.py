import json
import os
import platform
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

FILENAME = "tasks.json"

# -------------------- Clear Screen --------------------
def clear():
    sys_name = platform.system().lower()
    if sys_name == "windows":
        os.system("cls")
    elif sys_name in ["linux", "darwin"]:  # darwin = macOS
        os.system("clear")

# -------------------- File Management --------------------
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

# -------------------- Main Operations --------------------
def add_task():
    tasks = load_tasks()
    new_id = len(tasks) + 1
    title = input(Fore.CYAN + "Task Title: " + Style.RESET_ALL)
    description = input(Fore.CYAN + "Description: " + Style.RESET_ALL)
    deadline = input(Fore.CYAN + "Deadline (YYYY-MM-DD): " + Style.RESET_ALL)

    task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "Pending",
        "deadline": deadline
    }
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + "✅ Task added.\n")
    input("Press Enter to continue...")
    clear()

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "No tasks found.\n")
    else:
        for t in tasks:
            status_color = Fore.GREEN if t['status'] == "Done" else Fore.RED
            print(f"{Fore.CYAN}{t['id']}. {Fore.WHITE}{t['title']} - {status_color}{t['status']} {Fore.YELLOW}(Deadline: {t['deadline']})")
            print(f"   {Fore.MAGENTA}Description: {Fore.WHITE}{t['description']}\n")
    input("Press Enter to continue...")
    clear()

def mark_done():
    tasks = load_tasks()
    
    # نمایش تسک‌ها قبل از درخواست ID
    if not tasks:
        print(Fore.YELLOW + "No tasks found.\n")
        input("Press Enter to continue...")
        clear()
        return
    else:
        print(Fore.BLUE + "=== Current Tasks ===" + Style.RESET_ALL)
        for t in tasks:
            status_color = Fore.GREEN if t['status'] == "Done" else Fore.RED
            print(f"{Fore.CYAN}{t['id']}. {Fore.WHITE}{t['title']} - {status_color}{t['status']} {Fore.YELLOW}(Deadline: {t['deadline']})")
            print(f"   {Fore.MAGENTA}Description: {Fore.WHITE}{t['description']}\n")

    # درخواست ID تسک برای علامت‌گذاری به‌عنوان انجام‌شده
    try:
        task_id = int(input(Fore.CYAN + "Task ID to mark as done: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "❌ Invalid input.\n")
        input("Press Enter to continue...")
        clear()
        return

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Done"
            save_tasks(tasks)
            print(Fore.GREEN + "✅ Task marked as done.\n")
            input("Press Enter to continue...")
            clear()
            return
    print(Fore.RED + "❌ Task not found.\n")
    input("Press Enter to continue...")
    clear()

def delete_task():
    tasks = load_tasks()
    
    # نمایش تسک‌ها قبل از درخواست ID
    if not tasks:
        print(Fore.YELLOW + "No tasks found.\n")
        input("Press Enter to continue...")
        clear()
        return
    else:
        print(Fore.BLUE + "=== Current Tasks ===" + Style.RESET_ALL)
        for t in tasks:
            status_color = Fore.GREEN if t['status'] == "Done" else Fore.RED
            print(f"{Fore.CYAN}{t['id']}. {Fore.WHITE}{t['title']} - {status_color}{t['status']} {Fore.YELLOW}(Deadline: {t['deadline']})")
            print(f"   {Fore.MAGENTA}Description: {Fore.WHITE}{t['description']}\n")

    try:
        task_id = int(input(Fore.CYAN + "Task ID to delete: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "❌ Invalid input.\n")
        input("Press Enter to continue...")
        clear()
        return

    found = False
    new_tasks = []
    for t in tasks:
        if t["id"] == task_id:
            found = True
            continue
        new_tasks.append(t)

    if not found:
        print(Fore.RED + "❌ Task not found.\n")
    else:
        for i, t in enumerate(new_tasks, start=1):
            t["id"] = i
        save_tasks(new_tasks)
        print(Fore.GREEN + "✅ Task deleted.\n")

    input("Press Enter to continue...")
    clear()

def edit_task():
    tasks = load_tasks()
    
    # نمایش تسک‌ها قبل از درخواست ID
    if not tasks:
        print(Fore.YELLOW + "No tasks found.\n")
        input("Press Enter to continue...")
        clear()
        return
    else:
        print(Fore.BLUE + "=== Current Tasks ===" + Style.RESET_ALL)
        for t in tasks:
            status_color = Fore.GREEN if t['status'] == "Done" else Fore.RED
            print(f"{Fore.CYAN}{t['id']}. {Fore.WHITE}{t['title']} - {status_color}{t['status']} {Fore.YELLOW}(Deadline: {t['deadline']})")
            print(f"   {Fore.MAGENTA}Description: {Fore.WHITE}{t['description']}\n")

    # درخواست ID تسک برای ویرایش
    try:
        task_id = int(input(Fore.CYAN + "Task ID to edit: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "❌ Invalid input.\n")
        input("Press Enter to continue...")
        clear()
        return

    for t in tasks:
        if t["id"] == task_id:
            print(Fore.YELLOW + f"Current Task: {t}")
            t["title"] = input("New Title (leave blank to keep): ") or t["title"]
            t["description"] = input("New Description (leave blank to keep): ") or t["description"]
            t["deadline"] = input("New Deadline (YYYY-MM-DD, leave blank to keep): ") or t["deadline"]
            save_tasks(tasks)
            print(Fore.GREEN + "✅ Task updated.\n")
            input("Press Enter to continue...")
            clear()
            return
    print(Fore.RED + "❌ Task not found.\n")
    input("Press Enter to continue...")
    clear()

# -------------------- Menu --------------------
def menu():
    while True:
        print(Fore.BLUE + "=== Task Manager ===" + Style.RESET_ALL)
        print(Fore.CYAN + "1." + Fore.WHITE + " Add Task")
        print(Fore.CYAN + "2." + Fore.WHITE + " Show Tasks")
        print(Fore.CYAN + "3." + Fore.WHITE + " Mark Task as Done")
        print(Fore.CYAN + "4." + Fore.WHITE + " Edit Task")
        print(Fore.CYAN + "5." + Fore.WHITE + " Delete Task")
        print(Fore.CYAN + "0." + Fore.WHITE + " Exit")

        choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL)

        if choice == "1":
            clear()
            add_task()
        elif choice == "2":
            clear()
            show_tasks()
        elif choice == "3":
            clear()
            mark_done()
        elif choice == "4":
            clear()
            edit_task()
        elif choice == "5":
            clear()
            delete_task()
        elif choice == "0":
            print(Fore.GREEN + "Exiting program...")
            break
        else:
            print(Fore.RED + "❌ Invalid choice!\n")
            input("Press Enter to continue...")
            clear()

if __name__ == "__main__":
    clear()
    menu()
