#1
def digitize(n):
    new_n = str(n)
    my_arr = []

    for i in range(len(new_n)):
        my_arr.append(int(new_n[-i-1]))
    return my_arr

#
def digitize(n):
    arr= []
    for i in str(n):
        arr.append(int(i))
        
        
    arr.reverse()
    return arr