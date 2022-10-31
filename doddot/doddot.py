from commands import (add_task, delete_task, empty_category, empty_tasks,
                      move_task, show_tasks)
from helpers import check_db, clear_screen, menu


def main():
    check_db()
    while True:
        clear_screen()
        show_tasks()
        menu()
        option = input('[*] Option: ')
        if option == '1':
            task = input('[*] ~$ ')
            add_task(task)
        if option == '2':
            task = input('[*] ~$ ')
            move_task(task)
        if option == '3':
            task = input('[*] ~$ ')
            delete_task(task)
        if option == '4':
            category = input('[*] ~$ ')
            empty_category(category)
        if option == '5':
            empty_tasks()
        if option == '0':
            print('Bye!')
            return False


if __name__ == '__main__':
    main()
