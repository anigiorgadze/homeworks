def count_sheep(n):
    my_str = ""
    if n == 0:
        print(my_str)
    for i in range(1,n+1):
        my_str += str(i) + " sheep..."
    print(my_str)

count_sheep(5)
         