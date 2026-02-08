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
    print("✅ La tarea ha sido agregada a la lista correctamente.")


def show_tasks(tasks):

    checkIsDone = list(filter(lambda t: t["done"] == True, tasks))

    for i in range(len(checkIsDone)):
         if (tasks[i]["id"] == checkIsDone[i]["id"]):
            isDone = "✅"
         elif (tasks[i]["id"] != checkIsDone[i]["id"]):
            isDone = "❌"
    print(f"LISTA DE TAREAS:\n\n{tasks[i]["id"]}. Tarea: {tasks[i]["title"]} | Finalizada: {isDone}")
