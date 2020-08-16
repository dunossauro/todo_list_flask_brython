from collections import namedtuple

task = namedtuple('Task', 'nome desc urgente')


def table_to_task(row):
    return task(row['nome'], row['descrição'], row.get('urgente', ''))


def check_stack(tasks, table):
    tasks = [task(x.name, x.desc, '') for x in tasks]

    return all(map(lambda task: task in tasks, table))


def move_task(po_column, task_name, action: "do|cancel"):
    selected_task = [
        task for task in po_column.get_tasks() if task.name == task_name
    ][0]
    getattr(selected_task, action)()
