from task_manager import *


def menu():
    print("1.Agregar una tarea\n2.Mostrar tareas\n3.Completar tarea\n4.Eliminar tarea\n5.Salir")


def main():
    tasks = load_tasks()
    menu()
    while True:
        inp = input("\nSeleccione una opción: ")

        if (inp == "1"):
            title = input("Ingrese el nombre de la tarea: ")
            taskExist = [t for t in tasks if title == t["title"]]

            if taskExist:
                print("❌❌❌ YA EXISTE LA TAREA PA")
                menu()
            else:
                add_tasks(tasks, title)
                save_task(tasks)
                print(
                    f"\n✅ La tarea ha sido agregada a la lista correctamente con el nombre {tasks[len(tasks)-1:][0]["title"]}")
        elif (inp == "2"):
            print(" \nLISTA DE TAREAS:\n")
            show_tasks(tasks)
        elif (inp == "3"):
            print("Ha seleccionado la opción 3")
            complete_task(tasks)
            save_task(tasks)
        elif (inp == "4"):
            print("Ha seleccionado la opción 4")
        else:
            print("Ha seleccionado la opción 5")


main()
