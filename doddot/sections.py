def home_section():
    banner = """\
████████╗ ██████╗ ██████╗  ██████╗      ██████╗██╗     ██╗
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗    ██╔════╝██║     ██║
   ██║   ██║   ██║██║  ██║██║   ██║    ██║     ██║     ██║
   ██║   ██║   ██║██║  ██║██║   ██║    ██║     ██║     ██║
   ██║   ╚██████╔╝██████╔╝╚██████╔╝    ╚██████╗███████╗██║
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝      ╚═════╝╚══════╝╚═╝






[1] Tasks
[2] Help
[3] About
[0] Exit
    """
    print(banner)


def task_section():
    banner = """\



[1] Add task
[2] Move task
[3] Delete task
[4] Delete all tasks
[5] Back to menu
    """
    print(banner)


def help_section():
    banner = """\
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


[0] Back to Menu
    """
    print(banner)


def about_section():
    banner = """\
+----------------------------------------------+
| Name: TODO CLI                               |
| Description: A TODO app on command line.     |
| Version: Undefined                           |
| Author: Kennedy Allyson                      |
| Email: kennedy01101@gmail.com                |
| Github: kennedyallyson                       |
+----------------------------------------------+


[1] Back to menu
    """
    print(banner)
