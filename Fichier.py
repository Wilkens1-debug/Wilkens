todo_list = []

def add_task(deskripsyon, tasks):
    tasks.append(deskripsyon)

def display_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}- {task}")

def mark_task_done(index, tasks):
    try:
        index = int(index)
        if 1 <= index <= len(tasks):
            del tasks[index - 1]
            print("Tach fini.")
        else:
            print("Endis la pa bon.")
    except ValueError:
        print("Antre yon bon endis.")

def save_tasks(tasks):
    with open("task.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tach yo anrejistre nan yon fichye.")

def load_tasks(tasks):
    try:
        with open("task.txt", "r") as file:
            tasks.extend(line.strip() for line in file.readlines())
        print("Tach ki nan fichye .")
    except FileNotFoundError:
        print("Fichye sa a pa ekziste.")

def bad():
    todo_list = []
    load_tasks(todo_list)
    
    while True:
        print("\nMeni:")
        print("1- Ajoute yon tach")
        print("2- Afiche tach yo")
        print("3- Tach fini yo")
        print("4- Anrejistre e femen")

        chwa = input("Chwazi opsyon w : ")

        if chwa == "1":
            deskripsyon = input("Dekri tach ou  : ")
            add_task(deskripsyon, todo_list)
        elif chwa == "2":
            display_tasks(todo_list)
        elif chwa == "3":
            index = input("Antre endis ou vle fini an : ")
            mark_task_done(index, todo_list)
        elif chwa == "4":
            save_tasks(todo_list)
            break
        else:
            print("Opsyon an pa valid.")

if __name__ == "__main__":
    bad()
