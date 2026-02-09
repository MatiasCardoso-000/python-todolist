import json
from pathlib import Path


FILE = Path("tasks.json")


def load_tasks():
    if not FILE.exists():
        open(FILE, "w")
    with open(FILE, "r", encoding="UTF-8") as f:
        return json.load(f)


def add_tasks(tasks, title):

    new_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})


def save_task(tasks):
    with open(FILE, "w", encoding="UTF-8") as f:
        json.dump(tasks, f, indent=4)

   


def show_tasks(tasks):
    for i in range(len(tasks)):
        if (tasks[i]["done"] is True):
            isDone = "✅"
        else:
            isDone = "❌"
        print(
            f"{tasks[i]["id"]}. Tarea: {tasks[i]["title"]} | Finalizada: {isDone}")


def complete_task(tasks):
    inpTitle = input("Ingrese el nombre de la tarea a completar: ")

    for t in tasks:
        if (inpTitle.lower().strip() == t["title"].lower()):
            inpDone = input("Desea finalizar la tarea? Ingrese si o no\n\n")
            if (inpDone == "si"):
                t["done"] = True
                print("\nLa tarea esta finalizada")
            elif (inpDone == "no"):
                t["done"] = False
                print("\nLa tarea sigue pendiente")
            else:
                print("Ingrese una opcion valida")
