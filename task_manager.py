import json
from pathlib import Path

FILE = Path("tasks.json")


def load_tasks():
    if not FILE.exists():
        return []
    with open(FILE, "r", encoding="UTF-8") as f:
        return json.load(f)


def add_tasks(tasks, title):

    new_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})


def save_task(tasks):
    with open(FILE, "w", encoding="UTF-8") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    for i, task in enumerate(tasks):
        if (task.get("done") is True):
            isDone = "✅"
        else:
            isDone = "❌"
        print(
            f"{task.get("id")}. Tarea: {task.get("title")} | Finalizada: {isDone}")


def complete_task(tasks):
    inp_title = input("Ingrese el nombre de la tarea a completar: ")

    for t in tasks:
        if (inp_title.lower().strip() == t["title"].lower()):
            inp_task_done = input(
                "Desea finalizar la tarea? Ingrese si o no\n\n")
            if (inp_task_done.strip().lower() == "si"):
                t["done"] = True
                print("\nLa tarea esta finalizada")
            elif (inp_task_done.strip().lower() == "no"):
                t["done"] = False
                print("\nLa tarea sigue pendiente")
            else:
                print("Ingrese una opcion valida")
            return
    print(f"No hay ninguna tarea con el nombre {inp_title}")


def delete_tasks(tasks):
    if (len(tasks) == 0):
        print("No hay tareas para eliminar")
        return
    inp_title = input("Ingrese el nombre de la tarea a eliminar: ")
    for i, task in enumerate(tasks):
        if (inp_title.strip().lower() == task.get("title").lower()):
            inp_task_delete = input(
                "Desea eliminar la tarea? Ingrese si o no\n\n")
            if (inp_task_delete.strip().lower() == "si"):
                print(
                    f"\nLa tarea {task.get("title")} se ha eliminado")
                tasks.pop(i)
            return
    print("No existe una tarea con ese nombre")


def end_program():
    quit()
