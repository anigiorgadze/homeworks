#Build a function that returns an array of integers from n to 1 where n>0.


def reverse_seq(n):
    my_arr=[]
    for i in range(n):
        my_arr.append(n-i)
    return my_arr



#2
def reverse_seq(n):
    my_arr = []
    i = 1
    while i < n+1:
        my_arr.append(i)
        i += 1 
    return my_arr[::-1]