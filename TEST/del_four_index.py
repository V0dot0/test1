my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def del_four_index(my_list):
    """
    Тех док
    """
    i = 3
    while i in range(len(my_list)):
        del my_list[i]
        i += 3
    return my_list

print(del_four_index(my_list))

help(del_four_index)

