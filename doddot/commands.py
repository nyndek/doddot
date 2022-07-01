todo = []
doing = []
done = []


def show_tasks():
    try:
        with open('data/tasks.txt', 'r') as data:
            lines = data.readlines()
            if len(lines) > 0:
                todo_length = len(lines[0].split(',')) - 1
                print('T͟O͟D͟O͟')
                for item in range(todo_length):
                    print('    ☐  {}'.format(lines[0].split(',')[item]))
                print('')
            else:
                print('T͟O͟D͟O͟')
            if len(lines) > 1:
                doing_length = len(lines[1].split(',')) - 1
                print('D͟O͟I͟N͟G͟')
                for item in range(doing_length):
                    print('    ☒  {}'.format(lines[1].split(',')[item]))
                print('')
            else:
                print('D͟O͟I͟N͟G͟')
            if len(lines) > 2:
                done_length = len(lines[2].split(',')) - 1
                print('D͟O͟N͟E͟')
                for item in range(done_length):
                    print('    ☑  {}'.format(lines[2].split(',')[item]))
                print('')
            else:
                print('D͟O͟N͟E͟')
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def add_task(text):
    if text == '':
        return
    command = text.split(' ')[-1]
    if command == 'todo':
        words = text.split(' ')
        words.remove('todo')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        todo.append(task)
    if command == 'doing':
        words = text.split(' ')
        words.remove('doing')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        doing.append(task)
    if command == 'done':
        words = text.split(' ')
        words.remove('done')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        done.append(task)
    try:
        with open('data/tasks.txt', 'r+') as data:
            for i in range(len(todo)):
                data.write('{},'.format(todo[i]))
            data.write('\n')
            for i in range(len(doing)):
                data.write('{},'.format(doing[i]))
            data.write('\n')
            for i in range(len(done)):
                data.write('{},'.format(done[i]))
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def move_task(text):
    if text == '':
        return
    command = text.split(' ')[-1]
    if command == 'todo':
        words = text.split(' ')
        words.remove('todo')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in doing:
            doing.remove(task)
        elif task in done:
            done.remove(task)
        todo.append(task)
    if command == 'doing':
        words = text.split(' ')
        words.remove('doing')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in todo:
            todo.remove(task)
        elif task in done:
            done.remove(task)
        doing.append(task)
    if command == 'done':
        words = text.split(' ')
        words.remove('done')
        task = ''
        for i in range(len(words)):
            task += words[i] + ' '
        if task in todo:
            todo.remove(task)
        elif task in doing:
            doing.remove(task)
        done.append(task)
    try:
        with open('data/tasks.txt', 'w') as data:
            for i in range(len(todo)):
                data.write('{},'.format(todo[i]))
            data.write('\n')
            for i in range(len(doing)):
                data.write('{},'.format(doing[i]))
            data.write('\n')
            for i in range(len(done)):
                data.write('{},'.format(done[i]))
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def delete_task(text):
    if text == '':
        return
    task = text + ' '
    if task in todo:
        todo.remove(task)
    if task in doing:
        doing.remove(task)
    if task in done:
        done.remove(task)
    try:
        with open('data/tasks.txt', 'w') as data:
            for i in range(len(todo)):
                data.write('{},'.format(todo[i]))
            data.write('\n')
            for i in range(len(doing)):
                data.write('{},'.format(doing[i]))
            data.write('\n')
            for i in range(len(done)):
                data.write('{},'.format(done[i]))
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))


def delete_all():
    todo.clear()
    doing.clear()
    done.clear()
    try:
        with open('data/tasks.txt', 'w') as data:
            data.write('')
    except FileNotFoundError as err:
        print('An error has occurred: {}'.format(err.filename))
