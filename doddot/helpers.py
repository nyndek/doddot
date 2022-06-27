from commands import TODO, DOING, DONE
import os
import platform

def clear_screen():
    os.system('clear||cls')

def check_path():
    dir_path = 'data/'
    file_name = 'taskdb'
    full_path = dir_path + file_name
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if not os.path.exists(full_path):
        with open(os.path.join(dir_path, file_name), 'x') as teste:
            pass

def check_lines():
    try:
        with open('data/taskdb', 'r+') as data:
            lines = data.readlines()
            if len(lines) > 0:
                todo_tam = len(lines[0].split(','))
                if todo_tam != 0:
                    for i in range(todo_tam):
                        TODO.append(lines[0].split(',')[i])
                        if '\n' in TODO:
                            TODO.remove('\n')
            if len(lines) > 1:
                doing_tam = len(lines[1].split(','))
                if doing_tam != 0:
                    for i in range(doing_tam):
                        DOING.append(lines[1].split(',')[i])
                        if '\n' in DOING:
                            DOING.remove('\n')
            if len(lines) > 2:
                done_tam = len(lines[2].split(','))
                if done_tam != 0:
                    for i in range(done_tam):
                        DONE.append(lines[2].split(',')[i])
                        if '\n' in DONE:
                            DONE.remove('\n')
                        if '' in DONE:
                            DONE.remove('')
    except FileNotFoundError as err:
        print("Algum problema ao ler o arquivo {}".format(err.filename))
