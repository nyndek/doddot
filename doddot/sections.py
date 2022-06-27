def menu_section():
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
    print(menu_)


def task_section():
    submenu_ = '''\



[1] Add task
[2] Move task
[3] Delete task
[4] Delete all tasks
[5] Back to menu
    '''
    print(submenu_)


def help_section():
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


def about_section():
    about_ = '''\
+----------------------------------------------+
| Name: TODO CLI                               |
| Description: A TODO app on command line.     |
| Version: Undefined                           |
| Author: Kennedy Allyson                      |
| Email: kennedy01101@gmail.com                |
| Github: kennedyallyson                       |
+----------------------------------------------+


[1] Back to menu
    '''
    print(about_)
