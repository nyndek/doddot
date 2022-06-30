def home_section():
    banner = """\
 _____            _     _
(____ \          | |   | |      _
 _   \ \ ___   _ | | _ | | ___ | |_
| |   | / _ \ / || |/ || |/ _ \|  _)
| |__/ / |_| ( (_| ( (_| | |_| | |__
|_____/ \___/ \____|\____|\___/ \___)



[1] Tasks
[2] Help
[3] About
[0] Exit
    """
    print(banner)


def task_section():
    banner = """\



[1] Add Task
[2] Move Task
[3] Delete Task
[4] Empty All
[0] Back to Menu
    """
    print(banner)


def help_section():
    banner = """\
+------------------------------------------------+
|                   HOW TO USE                   |
+------------------------------------------------+
| A͟D͟D͟ ͟T͟A͟S͟K͟                                       |
|                                                |
| ~$ <task> <category_name>                      |
| e.g.: ~$ Improve the documentation todo        |
| Note: The category name must be in lowercase   |
|                                                |
| M͟O͟V͟E͟ ͟T͟A͟S͟K͟                                      |
|                                                |
| ~$ <task> <category_name>                      |
| e.g.: ~$ Remove deprecated modules done        |
| Note: The task must belong to a category       |
|                                                |
| D͟E͟L͟E͟T͟E͟ ͟T͟A͟S͟K͟                                    |
|                                                |
| ~$ <task>                                      |
| e.g.: ~$ Code review                           |
| Note: The task must belong to a category       |
+------------------------------------------------+


[0] Back to Menu
    """
    print(banner)


def about_section():
    banner = """\
+---------------------------------------------------+
| Name: Doddot                                      |
| Version: 1.0.0                                    |
| Description: To-Do CLI app to organize your tasks |
| Author: Kennedy                                   |
| Email: kennedy01101@gmail.com                     |
+---------------------------------------------------+


[0] Back to Menu
    """
    print(banner)
