import os

from commands import doing, done, todo


def clear_screen():
    os.system('clear||cls')


def check_db():
    dirname = 'data/'
    filename = 'taskdb'
    fullpath = dirname + filename
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    if not os.path.exists(fullpath):
        with open(os.path.join(dirname, filename), 'x') as teste:
            pass


def read_db():
    try:
        with open('data/taskdb', 'r+') as data:
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
