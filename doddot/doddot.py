from commands import add_task, delete_all, delete_task, move_task, show_tasks
from helpers import check_db, clear_screen, read_db
from sections import about_section, help_section, home_section, task_section


def main():
    check_db()
    read_db()
    home_section()
    while True:
        option = input('[*] Option: ')
        number = 0
        while number != 10:
            if option == '1':
                clear_screen()
                show_tasks()
                task_section()
                sub_option = input('[*] Option: ')
                if sub_option == '1':
                    task = input('[-] ~$ ')
                    add_task(task)
                if sub_option == '2':
                    task = input('[-] ~$ ')
                    move_task(task)
                if sub_option == '3':
                    task = input('[-] ~$ ')
                    delete_task(task)
                if sub_option == '4':
                    delete_all()
                if sub_option == '0':
                    clear_screen()
                    home_section()
                    number = 10
            elif option == '2':
                clear_screen()
                help_section()
                sub_option = input('[*] Option: ')
                if sub_option == '0':
                    clear_screen()
                    home_section()
                    number = 10
            elif option == '3':
                clear_screen()
                about_section()
                sub_option = input('[*] Option: ')
                if sub_option == '0':
                    clear_screen()
                    home_section()
                    number = 10
            elif option == '0':
                print('\nBye!')
                return False
            else:
                print('\nInvalid option! Choose one of the options above.')
                return False


if __name__ == '__main__':
    main()
