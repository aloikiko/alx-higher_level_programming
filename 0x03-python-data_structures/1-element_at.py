375aa2:/alx-higher_level_programming/0x03-python-data_structures# emacs 2-replace_in_list.py
root@ff4dd5375aa2:/alx-higher_level_programming/0x03-python-data_structures# emacs 3-print_reversed_list_integer.py
root@ff4dd5375aa2:/alx-higher_level_programming/0x03-python-data_structures# emacs 4-new_in_list.py
root@ff4dd5375aa2:/alx-higher_level_programming/0x03-python-data_structures# emacs
77;30601;0c#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)

    length = len(my_list)

    if idx > length - 1:
        return (None)

    return(my_list[idx])





