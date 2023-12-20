"""
Prueba de la clase TaskManager.
"""

from taskManager import TaskManager

objTM = TaskManager()

# Tareas predefinidas
objTM.add_task("Tender la cama", "Poner las colchas", 3)
objTM.add_task("Cenar", "A gusto", 3)
objTM.add_task("Programar", "Interesante", 2)
objTM.add_task("Pasear al perro", "Divertido", 2)
objTM.add_task("Limpiar la PC", "Laborioso", 1)
objTM.add_task("Lavar los trastes", "Aburrido", 1)


def get_int(msj: str):
    """
    Función que retona un número entero

    :param msj: Mensaje que muestra en bucle
    :type msj: str

    :return: Número entero introducido mediante teclado por el usuario
    :rtype: int
    """
    while True:
        try:
            entero = int(input(msj))
            return entero
        except ValueError:
            print("Por favor, selecciona un número entero.")

# Agregar tareas o manipularlas manualmente
while True:
    print("Bienvenido al Menú del Manejador de Tareas")
    print("Opción 1: Agregar una Tarea")
    print("Opción 2: Actualizar una Tarea")
    print("Opción 3: Eliminar una Tarea")
    print("Opción 4: Obtener las Tareas Completadas")
    print("Opción 5: Obtener las Tareas según su Estado")
    print("Opción 6: Salir")
    opcion = get_int("Selecciona una opción: ")
    print()

    # Agregando una tarea
    if opcion == 1:
        title = input("Escriba el título de la tarea: ")
        description = input("Escriba la descripción de la tarea: ")
        status = get_int("Selecciona el estado de la tarea:\n1. pendiente\n2. en progreso\n3. completada\t")
        task = objTM.add_task(title, description, status)
        if task:
            print("Tarea AGREGADA con éxito:", task, "\n")
        else:
            print("No se pudo agregar la tarea por uno de los siguientes motivos: "
                  "\n1. Revisa que los datos introducidos no están vacíos "
                  "\n2. Que el título no sea igual que el de otra tarea "
                  "\n3. Que el estado introducido sea válido", "\n")

    # Actualizando una tarea
    elif opcion == 2:
        title_to_update = input("Escriba el título de la tarea a actualizar: ")
        new_title = input("Escriba el nuevo título de la tarea: ")
        new_description = input("Escriba la nueva descripción de la tarea: ")
        new_status = get_int("Selecciona el nuevo estado de la tarea:\n1. pendiente\n2. en progreso\n3. completada\t")
        updated_task = objTM.update_task(title_to_update, new_title, new_description, new_status)
        if updated_task:
            print("Tarea ACTUALIZADA correctamente:", updated_task, "\n")
        else:
            print("No se pudo actualizar la tarea por uno de los siguientes motivos: "
                  "\n1. Revisa que los datos introducidos no están vacíos "
                  "\n2. Que el título de la tarea a actualizar exista "
                  "\n3. Que el título nuevo no sea igual que el de otra tarea existente"
                  "\n4. Que el estado introducido sea válido", "\n")

    # Eliminando una tarea
    elif opcion == 3:
        title_to_delete = input("Ingresa el título de la tarea a eliminar: ")
        deleted_task = objTM.delete_task(title_to_delete)
        if deleted_task:
            print("Tarea ELIMINADA correctamente:", deleted_task, "\n")
        else:
            print("No se pudo eliminar la tarea por uno de los siguientes motivos: "
                  "\n1. Revisa que los datos introducidos no están vacíos "
                  "\n2. Que el título de la tarea a eliminar exista ", "\n")

    # Obteniendo la lista de tareas completadas
    elif opcion == 4:
        tasks_completed = objTM.get_tasks_completed()
        if tasks_completed:
            print("Tareas con el estado 'completada':")
            for tarea in tasks_completed:
                print(tarea)
            print()
        elif isinstance(tasks_completed, list):
            print("No existen tareas con el estado 'completada'", "\n")

    # Obteniendo la lista de tareas según su estado
    elif opcion == 5:
        status_to_find = get_int("Selecciona el estado de la tarea:\n1. pendiente\n2. en progreso\n3. completada\t")
        tasks_by_status = objTM.get_task_by_status(status_to_find)
        if tasks_by_status:
            print("Tareas según su estado:")
            for tarea in tasks_by_status:
                print(tarea)
            print()
        elif isinstance(tasks_by_status, list):
            print("No se encontraron tareas con el estado solicitado.", "\n")
        else:
            print("El estado introducido no es válido", "\n")

    # Salir del menú y detener el bucle
    elif opcion == 6:
        break
