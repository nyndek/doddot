from sections import menu_section, help_section, about_section, task_section
from helpers import check_lines, check_path, clear_screen
from commands import show_tasks, add_task, move_task, delete_task, delete_all


def main():
    check_path()
    check_lines()
    menu_section()
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
                if sub_option == '5':
                    clear_screen()
                    menu_section()
                    number = 10
            elif option == '2':
                clear_screen()
                help_section()
                sub_option = input('[*] Option: ')
                if sub_option == '1':
                    clear_screen()
                    menu_section()
                    number = 10
            elif option == '3':
                clear_screen()
                about_section()
                sub_option = input('[*] Option: ')
                if sub_option == '1':
                    clear_screen()
                    menu_section()
                    number = 10
            elif option == '4':
                print('\nBye!')
                return False
            else:
                print('\nInvalid option! Choose one of the options above.')
                return False


if __name__ == '__main__':
    main()
