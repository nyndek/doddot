import os
import platform


todo_list = []
doing_list = []
done_list = []

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
                        todo_list.append(lines[0].split(',')[i])

                        if '\n' in todo_list:
                            todo_list.remove('\n')

            if len(lines) > 1:
                doing_tam = len(lines[1].split(','))

                if doing_tam != 0:
                    for i in range(doing_tam):
                        doing_list.append(lines[1].split(',')[i])

                        if '\n' in doing_list:
                            doing_list.remove('\n')

            if len(lines) > 2:
                done_tam = len(lines[2].split(','))

                if done_tam != 0:
                    for i in range(done_tam):
                        done_list.append(lines[2].split(',')[i])

                        if '\n' in done_list:
                            done_list.remove('\n')

                        if '' in done_list:
                            done_list.remove('')
    except FileNotFoundError as err:
        print("Algum problema ao ler o arquivo {}".format(err.filename))


def task_list():
    try:
        with open('data/taskdb', 'r') as data:
            lines = data.readlines()

            if len(lines) > 0:
                todo = lines[0]
                todo_len = len(lines[0].split(',')) - 1

                print('TODO:')

                for item in range(todo_len):
                    print("\t[ ] {}".format(lines[0].split(',')[item]))
                print('')
            else:
                print('TODO:')

            if len(lines) > 1:
                doing = lines[1]
                doing_len = len(lines[1].split(',')) - 1

                print('DOING:')

                for item in range(doing_len):
                    print("\t[..] {}".format(lines[1].split(',')[item]))
                print('')
            else:
                print('DOING:')

            if len(lines) > 2:
                done = lines[2]
                done_len = len(lines[2].split(',')) - 1

                print('DONE:')

                for item in range(done_len):
                    print("\t[x] {}".format(lines[2].split(',')[item]))
                print('')
            else:
                print('DONE:')
    except FileNotFoundError:
        pass


def add_task(task):
    if task == '':
        return

    command = task.split(' ')[-1]

    if command == 'todo':
        task_name = task.split(' ')
        task_name.remove('todo')
        s_task = ''

        for i in range(len(task_name)):
            s_task += task_name[i] + ' '

        todo_list.append(s_task)

    if command == 'doing':
        task_name = task.split(' ')
        task_name.remove('doing')
        s_task = ''

        for i in range(len(task_name)):
            s_task += task_name[i] + ' '

        doing_list.append(s_task)

    if command == 'done':
        task_name = task.split(' ')
        task_name.remove('done')
        s_task = ''

        for i in range(len(task_name)):
            s_task += task_name[i] + ' '

        done_list.append(s_task)

    try:
        with open('data/taskdb', 'r+') as data:
            for i in range(len(todo_list)):
                data.write("{},".format(todo_list[i]))
            data.write('\n')

            for i in range(len(doing_list)):
                data.write("{},".format(doing_list[i]))
            data.write('\n')

            for i in range(len(done_list)):
                data.write("{},".format(done_list[i]))
    except FileNotFoundError:
        pass


def move_task(task):
    if task == '':
        return

    command = task.split(' ')[-1]

    if command == 'todo':
        task_ = task.split(' ')
        task_.remove('todo')
        s_task = ''

        for i in range(len(task_)):
            s_task += task_[i] + ' '

        if s_task in doing_list:
            doing_list.remove(s_task)
        elif s_task in done_list:
            done_list.remove(s_task)

        todo_list.append(s_task)

    if command == 'doing':
        task_ = task.split(' ')
        task_.remove('doing')
        s_task = ''

        for i in range(len(task_)):
            s_task += task_[i] + ' '

        if s_task in todo_list:
            todo_list.remove(s_task)
        elif s_task in done_list:
            done_list.remove(s_task)

        doing_list.append(s_task)

    if command == 'done':
        task_ = task.split(' ')
        task_.remove('done')
        s_task = ''

        for i in range(len(task_)):
            s_task += task_[i] + ' '

        if s_task in todo_list:
            todo_list.remove(s_task)
        elif s_task in doing_list:
            doing_list.remove(s_task)

        done_list.append(s_task)

    try:
        with open('data/taskdb', 'w') as data:
            for i in range(len(todo_list)):
                data.write("{},".format(todo_list[i]))
            data.write('\n')

            for i in range(len(doing_list)):
                data.write("{},".format(doing_list[i]))
            data.write('\n')

            for i in range(len(done_list)):
                data.write("{},".format(done_list[i]))
    except FileNotFoundError:
        pass


def delete_task(task_):
    if task_ == '':
        return

    task = task_ + ' '

    if task in todo_list:
        todo_list.remove(task)

    if task in doing_list:
        doing_list.remove(task)

    if task in done_list:
        done_list.remove(task)

    try:
        with open('data/taskdb', 'w') as data:
            for i in range(len(todo_list)):
                data.write("{},".format(todo_list[i]))
            data.write('\n')

            for i in range(len(doing_list)):
                data.write("{},".format(doing_list[i]))
            data.write('\n')

            for i in range(len(done_list)):
                data.write("{},".format(done_list[i]))
    except FileNotFoundError:
        pass


def delete_all():
    todo_list.clear()
    doing_list.clear()
    done_list.clear()

    try:
        with open('data/taskdb', 'w') as data:
            data.write('')
    except FileNotFoundError:
        pass


def clear_screen():
    os.system('clear||cls')


def menu():
    menu_='''\
████████╗ ██████╗ ██████╗  ██████╗      ██████╗██╗     ██╗
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗    ██╔════╝██║     ██║
   ██║   ██║   ██║██║  ██║██║   ██║    ██║     ██║     ██║
   ██║   ██║   ██║██║  ██║██║   ██║    ██║     ██║     ██║
   ██║   ╚██████╔╝██████╔╝╚██████╔╝    ╚██████╗███████╗██║
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝      ╚═════╝╚══════╝╚═╝






[1] Tasks list
[2] Help
[3] About
[4] Exit
    '''
    clear_screen()
    print(menu_)


def submenu():
    submenu_ = '''\



[1] Add task
[2] Move task
[3] Delete task
[4] Delete all tasks
[5] Back to menu
    '''
    print(submenu_)


def help():
    help_ = '''\
+==================   HOW TO USE   ====================+
|                                                      |
|------------------------------------------------------|
|                      ADD TASK                        |
|                                                      |
|~$ <task_name> <todo/doing/done>                      |
|                                                      |
|Example:                                              |
|   [-] ~$ frontend todo                               |
|------------------------------------------------------|
|                      MOVE TASK                       |
|                                                      |
|~$ <task_name> <todo/doing/done>                      |
|                                                      |
|Example:                                              |
|   [-] ~$ blog backend done                           |
|                                                      |
|NOTE: The task must already be added in some category.|
|------------------------------------------------------|
|                     DELETE TASK                      |
|                                                      |
|~$ <task_name>                                        |
|                                                      |
|Example:                                              |
|  [-] ~$ frontend                                     |
|                                                      |
|NOTE: The task must already be added in some category.|
+------------------------------------------------------+


[1] Back to menu
    '''
    print(help_)


def about():
    about_ = '''\
+----------------------------------------------+
| Name: TODO CLI                               |
| Description: A TODO app from command line.   |
| Version: Undefined                           |
| Author: Kennedy Allyson                      |
| Email: kennedy01101@gmail.com                |
| Github: kennedyallyson                       |
+----------------------------------------------+


[1] Back to menu
    '''
    print(about_)


def main():
    check_path()
    check_lines()
    menu()

    while True:
        op = input('[*] Choose one option: ')
        n = 0

        while n != 10:
            if op == '1':
                clear_screen()
                task_list()
                submenu()

                sub_op = input('[*] Choose one option: ')

                if sub_op == '1':
                    task_ = input('[-] ~$ ')
                    task = task_.lower()

                    add_task(task)

                if sub_op == '2':
                    task_ = input('[-] ~$ ')
                    task = task_.lower()

                    move_task(task)

                if sub_op == '3':
                    task_ = input('[-] ~$ ')
                    task = task_.lower()

                    delete_task(task)

                if sub_op == '4':
                    delete_all()

                if sub_op == '5':
                    clear_screen()
                    menu()

                    n = 10
            elif op == '2':
                clear_screen()
                help()

                sub_op = input('[*] Choose one option: ')

                if sub_op == '1':
                    clear_screen()
                    menu()

                    n = 10
            elif op == '3':
                clear_screen()
                about()

                sub_op = input('[*] Choose one option: ')

                if sub_op == '1':
                    clear_screen()
                    menu()

                    n = 10
            elif op == '4':
                print("\nGood Bye! :)")

                return False
            else:
                print('\nInvalid option! Choose one of the options above.')
                print(';(')

                return False


if __name__=='__main__':
    main()
