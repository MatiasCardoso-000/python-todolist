from task_manager import *


def menu():
    print("1.Agregar una tarea\n2.Mostrar tareas\n3.Completar tarea\n4.Eliminar tarea\n5.Salir")


def main():
    tasks = load_tasks()
    menu()
    while True:
        inp = input("\nSeleccione una opción: ")

        if (inp == "1"):
            title = input("Título: ")
            taskExist = [t for t in tasks if title == t["title"]]
            if taskExist:
                print("❌❌❌ YA EXISTE LA TAREA PA")
                menu()
            else:
                add_tasks(tasks, title)
                save_task(tasks)
        elif (inp == "2"):
            print("Ha seleccionado la opción 2\n")
            show_tasks(tasks)
        elif (inp == "3"):
            print("Ha seleccionado la opción 3")
        elif (inp == "4"):
            print("Ha seleccionado la opción 4")
        else:
            print("Ha seleccionado la opción 5")


main()
