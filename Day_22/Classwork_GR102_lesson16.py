# print(int(str(34.0//3)[:-2]))

# print(int(6//2.0))




my_arr = [5, 6, 4, 3]

# x = "#".join(my_arr)

# print(x)

def my_join(my_arr):

    my_str = ""
    for element in my_arr:
        my_str += str(element)
    print(my_str)


my_join(my_arr)