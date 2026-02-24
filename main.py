from task_manager import load_tasks, add_tasks,save_task, show_tasks, complete_task, delete_tasks, end_program


def menu():
    print("1.Agregar una tarea\n2.Mostrar tareas\n3.Completar tarea\n4.Eliminar tarea\n5.Salir")


def main():
    menu()

    tasks = load_tasks()
    while True:
        inp = input("\nSeleccione una opción: ")

        if (inp == "1"):
            title = input("Ingrese el nombre de la tarea: ")
            if (len(title) == 0):
                print("Debe ingresar un nombre valido")
            else:
                taskExist = [t for t in tasks if title == t["title"]]

                if taskExist:
                    print("❌❌❌ YA EXISTE LA TAREA PA")
                else:
                    add_tasks(tasks, title)
                    save_task(tasks)
                    print(
                        f"\n✅ La tarea ha sido agregada a la lista correctamente con el nombre {tasks[-1]["title"]}")
        elif (inp == "2"):
            print(" \nLISTA DE TAREAS:\n")
            if (len(tasks) == 0):
                print("La lista de tareas esta vacia")
            else:
                show_tasks(tasks)
        elif (inp == "3"):
            complete_task(tasks)
            save_task(tasks)
        elif (inp == "4"):
            delete_tasks(tasks)
            save_task(tasks)
        elif (inp == "5"):
            end_program()


main()
