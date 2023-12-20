class TaskManager:
    """
    Esta clase es parte de la prueba técnica del proceso de reclutamiento de Swipall.

    La clase representa un sistema de gestión de tareas.  El sistema debe permite a los usuarios crear, actualizar,
    y eliminar tareas. Cada tarea tiene un título, una descripción y un estado (pendiente, en progreso, completada).
    """

    def __init__(self):
        """
        Constructor de la clase TaskManager

        Este constructor inicializa la variable __tasks, una lista que servirá para almacenar las tareas.
        Además, inicializa también __list_of_status con los valores ['pendiente', 'en progreso', 'completada'],
        que servirá para verificar los estados en las funciones de la clase.
        """
        self.__tasks = []
        self.__list_of_status = ['pendiente', 'en progreso', 'completada']

    def add_task(self, title: str, description: str, status: int):
        """
        Inserta una nueva tarea en la lista __tasks. Cada tarea tiene un título que es único, y servirá para
        identificar la tarea, una descripción y un estado, ninguno de los campos pueden quedar vacíos.

        :param title: Una cadena que será el título de la tarea.
        :type title: str

        :param description: Una cadena que será la descripción de la tarea.
        :type description: str

        :param status: Un entero que indique cuál es el estado de la tarea valiéndose de la función get_status().
        :type status: int

        :return: Un diccionario con los datos de la tarea si pudo ser insertada correctamente en la lista __tasks.
                 None si la tarea no pudo ser insertada en la lista __tasks.
        :rtype: dict or None

        Esta función recibe como argumentos un título y una descripción de la tarea, además de un estado que es int,
        cuyo valor servirá para mandárselo como argumento a la función get_status(), que regresa una cadena con el valor
        real del status, posteriormente se verifica que el estado sea válido y exista en la lista __list_of_status.
        Si el estado es válido, entonces se verifica que title y description no sean cadenas vacías, para posteriormente
        revisar que el title sea único y que no se repita en ninguna otra tarea, una vez comprobadas esas condiciones,
        se insertan los datos en un diccionario, y este es insertado en la lista __tasks, por último se retorna el dict.
        En caso de que haya fallado alguna de las condiciones, no se inserta nada en la lista __tasks y se retorna None.
        """
        title = title.upper().strip()  # mayus para tener congruencia con los demás títulos
        estado = self.__get_status(status)
        if estado in self.__list_of_status:  # valida que exista el estado
            if title and description:  # valida que no venga vacío title o description
                if not self.__get_task_by_title(title):  # valida que el título no se repita en otras tareas
                    task = {'title': title,
                            'description': description,
                            'status': estado
                            }
                    self.__tasks.append(task)
                    return task
        return None

    def update_task(self, current_title: str, new_title: str, new_description: str, new_status: int):
        """
        Actualiza y retorna una tarea de la lista __tasks.

        :param current_title: Una cadena que será el título actual de la tarea a actualizar.
        :type current_title: str

        :param new_title: Una cadena que será el nuevo título de la tarea a actualizar.
        :type new_title: str

        :param new_description: Una cadena que será la nueva descripción de la tarea a actualizar.
        :type new_description: str

        :param new_status: Un entero que indique cuál será el nuevo estado de la tarea a actualizar.
        :type new_status: int

        :return: Un diccionario con los datos de la tarea si pudo ser actualizada exitosamente.
                 None si la tarea no pudo ser actualizada.
        :rtype: dict or None

        La función recibe como argumento el título actual, que a su vez es pasado como argumento a get_task_by_title(),
        si el título fue encontrado, significa que también la tarea fue encontrada, entonces, se retorna la tarea para
        ser actualizada, primero comprobando que el estado sea válido mediante get_status(), después se valida que el
        nuevo título y la descripción no sean cadenas vacías; si alguna condición falla retorna None.
        Además, se revisa el título, si este es igual que el actual entonces se deja igual pero los demás valores se
        sustituyen; o si es diferente que cualquier título existente entonces los valores también se sustituyen, se
        retorna la tarea en ambos casos.
        En caso de que el título sea igual a uno existente, entonces no se hará nada y se retorna None.
        """
        current_title = current_title.upper().strip()  # mayus para tener congruencia con los demás títulos
        new_title = new_title.upper().strip()
        task = self.__get_task_by_title(current_title)
        if task:
            new_estado = self.__get_status(new_status)
            if new_estado in self.__list_of_status:  # valida que el estado sea válido
                if new_title and new_description:  # valida que no venga vacío title o description
                    if new_title == current_title:  # en caso de que se quiera conservar el mismo título en la tarea
                        task['description'] = new_description
                        task['status'] = new_estado
                        return task
                    elif not self.__get_task_by_title(new_title):  # valida que new_title no se repita en otras tareas
                        task['title'] = new_title
                        task['description'] = new_description
                        task['status'] = new_estado
                        return task
        return None

    def delete_task(self, title: str):
        """
        Elimina y retorna una tarea de la lista __tasks.

        :param title: Una cadena que será el título de la tarea a eliminar de la lista __tasks.
        :type title: str

        :return: Un diccionario con los datos de la tarea si pudo ser eliminado de la lista __tasks exitosamente.
                 None si la tarea no pudo ser eliminada.
        :rtype: dict or None

        La función recibe como argumento un título, el cual a su vez es pasado como argumento a get_task_by_title(),
        si el título fue encontrado, significa que también la tarea fue encontrada, entonces, se retorna la tarea para
        ser eliminada de la lista __tasks y posteriormente retornada, de lo contrario, no hará nada y se retornará None.
        """
        title = title.upper().strip()  # mayus para tener congruencia con los demás títulos
        task = self.__get_task_by_title(title)
        if task:
            index = self.__tasks.index(task)
            return self.__tasks.pop(index)
        return None

    def get_task_by_status(self, status: int):
        """
        Busca y retorna una lista task_by_status con las tareas que se encuentren en la lista existente __tasks cuyo
        estado coincida con el estado recibido como argumento

        :param status: Un entero que indique cual es el estado de la tarea por medio de la función get_status().
        :type status: int

        :return: lista con las tareas cuyo estado coincida con el que fue pasado como argumento.
                 lista vacía si no encontraron tareas que su status coincida con el pasado como argumento.
                 None si el estado pasado como argumento es inválido.
        :rtype: list or None

        Esta función recibe como argumento un estado como int, cuyo valor servirá para mandárselo como argumento a la
        función get_status() para obtener su valor real, posteriormente se verifica que exista y sea válido
        en la lista __list_of_status.
        Si el estado es válido, entonces busca en la lista __tasks las tareas que coincidan con el estado recibido como
        argumento, las que encuentren serán insertadas en la lista task_by_status, para al final ser retornada.
        En caso de que el estado sea inválido, no recorre la lista __tasks y se retorna None.
        """
        tasks_by_status = []
        estado = self.__get_status(status)
        if estado in self.__list_of_status:
            for task in self.__tasks:
                if task['status'] == estado:
                    tasks_by_status.append(task)
            return tasks_by_status
        else:
            return None

    def get_tasks_completed(self):
        """
        Busca y retorna una lista tasks_completed con las tareas que se encuentren en la lista __tasks cuyo estado sea
        el de 'completada'

        :return: lista con las tareas cuyo status sea 'completada'.
                 lista vacía si no existen tareas con el status 'completada'.
        :rtype: list
        """
        tasks_completed = []
        for task in self.__tasks:
            if task['status'] == 'completada':
                tasks_completed.append(task)
        return tasks_completed

    def __get_status(self, status: int):
        """
        Esta función privada retorna el valor real del estado de una tarea, según el valor del índice que recibe
        como argumento.

        :param status: Un entero que representa la posición de la lista donde se encuentra el valor real del estado.
        :type status: int

        :returns: str con el valor real del estado.
                  None si indice recibido como argumento no existe dentro de la lista __list_of_status.
        :rtype: str or None

        Primero, se verifica que el status recibido sea un entero, en caso de serlo, entonces verifica que no se exceda
        de los límites de la lista, para después pasar a sacar el valor real del estado. Si no cumple con esas
        dos condiciones, entonces retorna None.
        El valor real funciona de la siguiente manera: si se recibe un 1, entonces su valor real es 'pendiente'; si se
        recibe un 2, entonces su valor real será 'en progreso', y si se recibe un 3, su valor real es 'completada'.
        (Al int que se recibe como argumento se le resta 1 para obtener su posición real en la lista __list_of_status).
        """
        if isinstance(status, int) and not isinstance(status, bool):  # valida que no sea booleano porque es 1 o 0
            if 1 <= status <= len(self.__list_of_status):
                return self.__list_of_status[status - 1]
        return None

    def __get_task_by_title(self, title: str):
        """
        Función privada que busca en la lista __tasks una tarea en base a un título recibido como argumento, si
        la encuentra, es retornada.

        :param title: Una cadena que sea el título de la tarea a buscar en la lista __tasks.
        :type title: str

        :return: Un diccionario con los datos de la tarea si fue encontrado en la lista __tasks.
                 None en caso de no encontrar la tarea con ese título en la lista __tasks.
        :rtype: dict or None
        """
        for task in self.__tasks:
            if task['title'] == title:
                return task
        return None
