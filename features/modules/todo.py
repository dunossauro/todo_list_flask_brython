from collections import namedtuple

task = namedtuple('Task', 'nome desc urgente')


def table_to_task(row):
    return task(row['nome'], row['descrição'], row.get('urgente', ''))


def check_stack(tasks, table):
    tasks = [task(x.name, x.desc, '') for x in tasks]

    return list(map(lambda task: task in tasks, table))
