def find_multiples(integer, limit):
    my_str =[]
    for i in range(integer,limit+1,integer):
        my_str.append(i)
    return my_str
    

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))