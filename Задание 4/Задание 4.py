
class Task:
    def __init__(self, id, name, description, status):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__status = status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def update_status(self, st):
        if st in ['done', 'in progress']:
            self.__status = st


class Subtask(Task):
    # have comlex task id
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id


class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, id, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.subtasks = []
        self.complex_tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def create_subtask(self, subtask):
        self.subtasks.append(subtask)

    def create_complex_task(self, complex_task):
        self.complex_tasks.append(complex_task)

    def get_tasks(self):
        return self.tasks

    def get_subtasks(self):
        return self.subtasks

    def get_complex_tasks(self):
        return self.complex_tasks

    def get_tasks_by_id(self, id):
        return [task for task in self.tasks if task.id == id]

    def get_subtasks_by_id(self, id):
        return [subtask for subtask in self.subtasks if subtask.id == id]

    def get_complex_tasks_by_id(self, id):
        return [complex_task for complex_task in self.complex_tasks if complex_task.id == id]

    def remove_tasks(self):
        self.tasks = []

    def remove_subtasks(self):
        self.subtasks = []

    def remove_complex_tasks(self):
        self.complex_tasks = []

    def remove_task_by_id(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]

    def remove_subtask_by_id(self, id):
        self.subtasks = [subtask for subtask in self.subtasks if subtask.id != id]

    def remove_complex_task_by_id(self, id):
        self.complex_tasks = [complex_task for complex_task in self.complex_tasks if complex_task.id != id]

    def update_status(self, task):
        task_to_update = next(
            (t for t in self.tasks if t.id == task.id), None
        )
        if task_to_update:
            task_to_update.status = task.status
