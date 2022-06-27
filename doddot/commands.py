TODO = []
DOING = []
DONE = []

def show_tasks():
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
        TODO.append(s_task)
    if command == 'doing':
        task_name = task.split(' ')
        task_name.remove('doing')
        s_task = ''
        for i in range(len(task_name)):
            s_task += task_name[i] + ' '
        DOING.append(s_task)
    if command == 'done':
        task_name = task.split(' ')
        task_name.remove('done')
        s_task = ''
        for i in range(len(task_name)):
            s_task += task_name[i] + ' '
        DONE.append(s_task)
    try:
        with open('data/taskdb', 'r+') as data:
            for i in range(len(TODO)):
                data.write("{},".format(TODO[i]))
            data.write('\n')
            for i in range(len(DOING)):
                data.write("{},".format(DOING[i]))
            data.write('\n')
            for i in range(len(DONE)):
                data.write("{},".format(DONE[i]))
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
        if s_task in DOING:
            DOING.remove(s_task)
        elif s_task in DONE:
            DONE.remove(s_task)
        TODO.append(s_task)
    if command == 'doing':
        task_ = task.split(' ')
        task_.remove('doing')
        s_task = ''
        for i in range(len(task_)):
            s_task += task_[i] + ' '
        if s_task in TODO:
            TODO.remove(s_task)
        elif s_task in DONE:
            DONE.remove(s_task)
        DOING.append(s_task)
    if command == 'done':
        task_ = task.split(' ')
        task_.remove('done')
        s_task = ''
        for i in range(len(task_)):
            s_task += task_[i] + ' '
        if s_task in TODO:
            TODO.remove(s_task)
        elif s_task in DOING:
            DOING.remove(s_task)
        DONE.append(s_task)
    try:
        with open('data/taskdb', 'w') as data:
            for i in range(len(TODO)):
                data.write("{},".format(TODO[i]))
            data.write('\n')
            for i in range(len(DOING)):
                data.write("{},".format(DOING[i]))
            data.write('\n')
            for i in range(len(DONE)):
                data.write("{},".format(DONE[i]))
    except FileNotFoundError:
        pass

def delete_task(task_):
    if task_ == '':
        return
    task = task_ + ' '
    if task in TODO:
        TODO.remove(task)
    if task in DOING:
        DOING.remove(task)
    if task in DONE:
        DONE.remove(task)
    try:
        with open('data/taskdb', 'w') as data:
            for i in range(len(TODO)):
                data.write("{},".format(TODO[i]))
            data.write('\n')
            for i in range(len(DOING)):
                data.write("{},".format(DOING[i]))
            data.write('\n')
            for i in range(len(DONE)):
                data.write("{},".format(DONE[i]))
    except FileNotFoundError:
        pass

def delete_all():
    TODO.clear()
    DOING.clear()
    DONE.clear()
    try:
        with open('data/taskdb', 'w') as data:
            data.write('')
    except FileNotFoundError:
        pass
