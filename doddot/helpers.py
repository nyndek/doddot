import os

FILEPATH = os.path.abspath(os.path.dirname(__file__))
DATAPATH = os.path.abspath(os.path.join(FILEPATH, '..', 'data'))
FILENAME = 'tasks.txt'
FULLPATH = os.path.join(DATAPATH, FILENAME)

todo = []
doing = []
done = []


def clear_screen():
    os.system('clear||cls')


def check_db():
    if not os.path.exists(DATAPATH):
        os.mkdir(DATAPATH)
    if not os.path.exists(FULLPATH):
        with open(FULLPATH, 'x') as teste:
            pass
    try:
        with open(FULLPATH, 'r+') as data:
            lines = data.readlines()
            if len(lines) > 0:
                todo_length = len(lines[0].split(','))
                if todo_length != 0:
                    for i in range(todo_length):
                        todo.append(lines[0].split(',')[i])
                        if '\n' in todo:
                            todo.remove('\n')
            if len(lines) > 1:
                doing_length = len(lines[1].split(','))
                if doing_length != 0:
                    for i in range(doing_length):
                        doing.append(lines[1].split(',')[i])
                        if '\n' in doing:
                            doing.remove('\n')
            if len(lines) > 2:
                done_length = len(lines[2].split(','))
                if done_length != 0:
                    for i in range(done_length):
                        done.append(lines[2].split(',')[i])
                        if '\n' in done:
                            done.remove('\n')
                        if '' in done:
                            done.remove('')
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def menu():
    banner = """\


[1] Add Task
[2] Move Task
[3] Delete Task
[4] Empty Tasks
[0] Exit
    """
    print(banner)
