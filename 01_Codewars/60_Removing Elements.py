def remove_every_other(my_list):
    new_arr = []

    for i in range(0,len(my_list),2):
        new_arr.append(my_list[i])
    return new_arr

